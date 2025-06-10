from collections import OrderedDict

from django.http import HttpResponseBadRequest, JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_POST

from .models import Quest, Bobblehead, SkillBook, RareItem, AlienCaptiveLog, NukaColaQuantum, Clothing, Weapon, \
    TeddyBear, Achievement

FALLOUT3_MENU_ITEMS = [
    ("Quests", "fallout3_quests"),
    ("Bobbleheads", "fallout3_bobbleheads"),
    ("Skill Books", "fallout3_skillbooks"),
    ("Rare Items", "fallout3_rareitems"),
    ("Alien Captive Logs", "fallout3_alienlogs"),
    ("Nuka Cola Quantums", "fallout3_nukacolaquantums"),
    ("Clothing", "fallout3_clothing"),
    ("Weapons", "fallout3_weapons"),
    ("Teddy Bears", "fallout3_teddybears"),
    ("Achievements/Trophies", "fallout3_achievements"),
]


def home(request):
    return render(request, "home.html")


def fallout3_dashboard(request):
    sections = []
    total_completed = 0
    total_items = 0

    # Quests: found and completed (as separate entries)
    quests = Quest.objects.all()
    found_count = quests.filter(found=True).count()
    completed_count = quests.filter(completed=True).count()
    quest_total = quests.count()
    found_percent = round(100 * found_count / quest_total) if quest_total else 0
    completed_percent = round(100 * completed_count / quest_total) if quest_total else 0
    sections.append({"label": "Quests Found", "x": found_count, "y": quest_total, "percent": found_percent})
    sections.append({"label": "Quests Completed", "x": completed_count, "y": quest_total, "percent": completed_percent})
    total_completed += completed_count
    total_items += quest_total

    # Bobbleheads: acquired
    bobs = Bobblehead.objects.all()
    acquired = bobs.filter(acquired=True).count()
    count = bobs.count()
    percent = round(100 * acquired / count) if count else 0
    sections.append({"label": "Bobbleheads", "x": acquired, "y": count, "percent": percent})
    total_completed += acquired
    total_items += count

    # Skill Books: count_found (sum), count_total (sum)
    books = SkillBook.objects.all()
    found = sum(b.count_found for b in books)
    total = sum(b.count_total for b in books)
    percent = round(100 * found / total) if total else 0
    sections.append({"label": "Skill Books", "x": found, "y": total, "percent": percent})
    total_completed += found
    total_items += total

    # Rare Items: acquired
    rareitems = RareItem.objects.all()
    acquired = rareitems.filter(acquired=True).count()
    count = rareitems.count()
    percent = round(100 * acquired / count) if count else 0
    sections.append({"label": "Rare Items", "x": acquired, "y": count, "percent": percent})
    total_completed += acquired
    total_items += count

    # Alien Captive Logs: acquired
    logs = AlienCaptiveLog.objects.all()
    acquired = logs.filter(acquired=True).count()
    count = logs.count()
    percent = round(100 * acquired / count) if count else 0
    sections.append({"label": "Alien Captive Logs", "x": acquired, "y": count, "percent": percent})
    total_completed += acquired
    total_items += count

    # Nuka Cola Quantums: count_found (sum), count_total (sum)
    quantums = NukaColaQuantum.objects.all()
    found = sum(q.count_found for q in quantums)
    total = sum(q.count_total for q in quantums)
    percent = round(100 * found / total) if total else 0
    sections.append({"label": "Nuka Cola Quantums", "x": found, "y": total, "percent": percent})
    total_completed += found
    total_items += total

    # Clothing: acquired
    clothing = Clothing.objects.all()
    acquired = clothing.filter(acquired=True).count()
    count = clothing.count()
    percent = round(100 * acquired / count) if count else 0
    sections.append({"label": "Clothing", "x": acquired, "y": count, "percent": percent})
    total_completed += acquired
    total_items += count

    # Weapons: acquired
    weapons = Weapon.objects.all()
    acquired = weapons.filter(acquired=True).count()
    count = weapons.count()
    percent = round(100 * acquired / count) if count else 0
    sections.append({"label": "Weapons", "x": acquired, "y": count, "percent": percent})
    total_completed += acquired
    total_items += count

    # Teddy Bears: count_found (sum), count_total (sum)
    bears = TeddyBear.objects.all()
    found = sum(b.count_found for b in bears)
    total = sum(b.count_total for b in bears)
    percent = round(100 * found / total) if total else 0
    sections.append({"label": "Teddy Bears", "x": found, "y": total, "percent": percent})
    total_completed += found
    total_items += total

    # Final overall stats
    total_percent = round(100 * total_completed / total_items) if total_items else 0

    return render(request, "dashboard.html", {
        "sections": sections,
        "total_completed": total_completed,
        "total_items": total_items,
        "total_percent": total_percent,
        "menu_items": FALLOUT3_MENU_ITEMS,
    })



def fallout3_quests(request):
    quests = Quest.objects.all().order_by('id')
    grouped = OrderedDict()
    section_stats = {}

    # Group by quest title, calculate per-section and overall stats
    for q in quests:
        grouped.setdefault(q.title, []).append(q)

    total_found = 0
    total_completed = 0
    total_quests = 0

    for title, qs in grouped.items():
        found = sum(1 for quest in qs if quest.found)
        completed = sum(1 for quest in qs if quest.completed)
        count = len(qs)
        found_percent = round(100 * found / count) if count else 0
        completed_percent = round(100 * completed / count) if count else 0
        section_stats[title] = {
            "found": found, "completed": completed, "count": count,
            "found_percent": found_percent, "completed_percent": completed_percent,
        }
        total_found += found
        total_completed += completed
        total_quests += count

    # Overall stats
    overall_found_percent = round(100 * total_found / total_quests) if total_quests else 0
    overall_completed_percent = round(100 * total_completed / total_quests) if total_quests else 0

    return render(request, "fallout3/quests.html", {
        "grouped": grouped,
        "section_stats": section_stats,
        "total_found": total_found,
        "total_completed": total_completed,
        "total_quests": total_quests,
        "overall_found_percent": overall_found_percent,
        "overall_completed_percent": overall_completed_percent,
        "menu_items": FALLOUT3_MENU_ITEMS,
        "active_menu": "fallout3_quests",
    })


@require_POST
def toggle_quest_field(request):
    quest_id = request.POST.get("id")
    field = request.POST.get("field")
    value = request.POST.get("value") == "true"
    if field not in ("found", "completed"):
        return HttpResponseBadRequest("Invalid field.")
    try:
        quest = Quest.objects.get(id=quest_id)
        setattr(quest, field, value)
        quest.save()
        return JsonResponse({"success": True})
    except Quest.DoesNotExist:
        return JsonResponse({"success": False, "error": "Quest not found"}, status=404)


def fallout3_bobbleheads(request):
    bobbleheads = Bobblehead.objects.all().order_by('id')
    total = bobbleheads.count()
    acquired = bobbleheads.filter(acquired=True).count()
    percent = round(100 * acquired / total) if total else 0
    return render(request, "fallout3/bobbleheads.html", {
        "bobbleheads": bobbleheads,
        "total": total,
        "acquired": acquired,
        "percent": percent,
        "menu_items": FALLOUT3_MENU_ITEMS,
        "active_menu": "fallout3_bobbleheads",
    })


@require_POST
def toggle_bobblehead_field(request):
    bobblehead_id = request.POST.get("id")
    value = request.POST.get("value") == "true"
    try:
        bob = Bobblehead.objects.get(id=bobblehead_id)
        bob.acquired = value
        bob.save()
        return JsonResponse({"success": True})
    except Bobblehead.DoesNotExist:
        return JsonResponse({"success": False, "error": "Bobblehead not found"}, status=404)


def fallout3_skillbooks(request):
    skillbooks = SkillBook.objects.all().order_by('id')
    total = sum(b.count_total for b in skillbooks)
    found = sum(b.count_found for b in skillbooks)
    percent = round(100 * found / total) if total else 0
    return render(request, "fallout3/skillbooks.html", {
        "skillbooks": skillbooks,
        "total": total,
        "found": found,
        "percent": percent,
        "menu_items": FALLOUT3_MENU_ITEMS,
        "active_menu": "fallout3_skillbooks",
    })


@require_POST
def update_skillbook_count(request):
    book_id = request.POST.get("id")
    direction = request.POST.get("direction")
    try:
        book = SkillBook.objects.get(id=book_id)
        if direction == "up" and book.count_found < book.count_total:
            book.count_found += 1
            book.save()
        elif direction == "down" and book.count_found > 0:
            book.count_found -= 1
            book.save()
        return JsonResponse({"success": True, "count_found": book.count_found})
    except SkillBook.DoesNotExist:
        return JsonResponse({"success": False, "error": "Skill Book not found"}, status=404)


def fallout3_rareitems(request):
    rareitems = RareItem.objects.all().order_by('id')
    grouped = OrderedDict()
    section_stats = {}

    total_acquired = 0
    total_items = 0

    for item in rareitems:
        grouped.setdefault(item.title, []).append(item)
    for title, items in grouped.items():
        acquired = sum(1 for i in items if i.acquired)
        count = len(items)
        percent = round(100 * acquired / count) if count else 0
        section_stats[title] = {"acquired": acquired, "count": count, "percent": percent}
        total_acquired += acquired
        total_items += count

    overall_percent = round(100 * total_acquired / total_items) if total_items else 0

    return render(request, "fallout3/rareitems.html", {
        "grouped": grouped,
        "section_stats": section_stats,
        "total_acquired": total_acquired,
        "total_items": total_items,
        "overall_percent": overall_percent,
        "menu_items": FALLOUT3_MENU_ITEMS,
        "active_menu": "fallout3_rareitems",
    })


@require_POST
def toggle_rareitem_field(request):
    item_id = request.POST.get("id")
    value = request.POST.get("value") == "true"
    try:
        item = RareItem.objects.get(id=item_id)
        item.acquired = value
        item.save()
        return JsonResponse({"success": True})
    except RareItem.DoesNotExist:
        return JsonResponse({"success": False, "error": "Rare Item not found"}, status=404)


def fallout3_alienlogs(request):
    logs = AlienCaptiveLog.objects.all().order_by('id')
    total = logs.count()
    acquired = logs.filter(acquired=True).count()
    percent = round(100 * acquired / total) if total else 0
    return render(request, "fallout3/alienlogs.html", {
        "logs": logs,
        "acquired": acquired,
        "total": total,
        "percent": percent,
        "menu_items": FALLOUT3_MENU_ITEMS,
        "active_menu": "fallout3_alienlogs",
    })


@require_POST
def toggle_alienlog_field(request):
    log_id = request.POST.get("id")
    value = request.POST.get("value") == "true"
    try:
        log = AlienCaptiveLog.objects.get(id=log_id)
        log.acquired = value
        log.save()
        return JsonResponse({"success": True})
    except AlienCaptiveLog.DoesNotExist:
        return JsonResponse({"success": False, "error": "Log not found"}, status=404)


def fallout3_nukacolaquantums(request):
    quantums = NukaColaQuantum.objects.all().order_by('id')
    grouped = OrderedDict()
    section_stats = {}

    total_found = 0
    total_total = 0

    for q in quantums:
        grouped.setdefault(q.title, []).append(q)
    for title, qs in grouped.items():
        found = sum(q.count_found for q in qs)
        count = sum(q.count_total for q in qs)
        percent = round(100 * found / count) if count else 0
        section_stats[title] = {"found": found, "count": count, "percent": percent}
        total_found += found
        total_total += count

    overall_percent = round(100 * total_found / total_total) if total_total else 0

    return render(request, "fallout3/nukacolaquantums.html", {
        "grouped": grouped,
        "section_stats": section_stats,
        "total_found": total_found,
        "total_total": total_total,
        "overall_percent": overall_percent,
        "menu_items": FALLOUT3_MENU_ITEMS,
        "active_menu": "fallout3_nukacolaquantums",
    })


@require_POST
def update_nukacola_count(request):
    quantum_id = request.POST.get("id")
    direction = request.POST.get("direction")
    try:
        quantum = NukaColaQuantum.objects.get(id=quantum_id)
        if direction == "up" and quantum.count_found < quantum.count_total:
            quantum.count_found += 1
            quantum.save()
        elif direction == "down" and quantum.count_found > 0:
            quantum.count_found -= 1
            quantum.save()
        return JsonResponse({"success": True, "count_found": quantum.count_found})
    except NukaColaQuantum.DoesNotExist:
        return JsonResponse({"success": False, "error": "Nuka Cola Quantum not found"}, status=404)


def fallout3_clothing(request):
    clothing = Clothing.objects.all().order_by('id')
    grouped = OrderedDict()
    section_stats = {}
    total_acquired = 0
    total_items = 0

    for item in clothing:
        grouped.setdefault(item.title, []).append(item)
    for title, items in grouped.items():
        acquired = sum(1 for i in items if i.acquired)
        count = len(items)
        percent = round(100 * acquired / count) if count else 0
        section_stats[title] = {"acquired": acquired, "count": count, "percent": percent}
        total_acquired += acquired
        total_items += count

    overall_percent = round(100 * total_acquired / total_items) if total_items else 0

    return render(request, "fallout3/clothing.html", {
        "grouped": grouped,
        "section_stats": section_stats,
        "total_acquired": total_acquired,
        "total_items": total_items,
        "overall_percent": overall_percent,
        "menu_items": FALLOUT3_MENU_ITEMS,
        "active_menu": "fallout3_clothing",
    })


@require_POST
def toggle_clothing_field(request):
    clothing_id = request.POST.get("id")
    value = request.POST.get("value") == "true"
    try:
        item = Clothing.objects.get(id=clothing_id)
        item.acquired = value
        item.save()
        return JsonResponse({"success": True})
    except Clothing.DoesNotExist:
        return JsonResponse({"success": False, "error": "Clothing not found"}, status=404)


def fallout3_weapons(request):
    weapons = Weapon.objects.all().order_by('id')
    grouped = OrderedDict()
    section_stats = {}
    total_acquired = 0
    total_items = 0

    for item in weapons:
        grouped.setdefault(item.title, []).append(item)
    for title, items in grouped.items():
        acquired = sum(1 for i in items if i.acquired)
        count = len(items)
        percent = round(100 * acquired / count) if count else 0
        section_stats[title] = {"acquired": acquired, "count": count, "percent": percent}
        total_acquired += acquired
        total_items += count

    overall_percent = round(100 * total_acquired / total_items) if total_items else 0

    return render(request, "fallout3/weapons.html", {
        "grouped": grouped,
        "section_stats": section_stats,
        "total_acquired": total_acquired,
        "total_items": total_items,
        "overall_percent": overall_percent,
        "menu_items": FALLOUT3_MENU_ITEMS,
        "active_menu": "fallout3_weapons",
    })


@require_POST
def toggle_weapon_field(request):
    weapon_id = request.POST.get("id")
    value = request.POST.get("value") == "true"
    try:
        item = Weapon.objects.get(id=weapon_id)
        item.acquired = value
        item.save()
        return JsonResponse({"success": True})
    except Weapon.DoesNotExist:
        return JsonResponse({"success": False, "error": "Weapon not found"}, status=404)


def fallout3_teddybears(request):
    bears = TeddyBear.objects.all().order_by('id')
    grouped = OrderedDict()
    section_stats = {}
    total_found = 0
    total_total = 0

    for bear in bears:
        grouped.setdefault(bear.title, []).append(bear)
    for title, items in grouped.items():
        found = sum(b.count_found for b in items)
        count = sum(b.count_total for b in items)
        percent = round(100 * found / count) if count else 0
        section_stats[title] = {"found": found, "count": count, "percent": percent}
        total_found += found
        total_total += count

    overall_percent = round(100 * total_found / total_total) if total_total else 0

    return render(request, "fallout3/teddybears.html", {
        "grouped": grouped,
        "section_stats": section_stats,
        "total_found": total_found,
        "total_total": total_total,
        "overall_percent": overall_percent,
        "menu_items": FALLOUT3_MENU_ITEMS,
        "active_menu": "fallout3_teddybears",
    })


@require_POST
def update_teddybear_count(request):
    bear_id = request.POST.get("id")
    direction = request.POST.get("direction")
    try:
        bear = TeddyBear.objects.get(id=bear_id)
        if direction == "up" and bear.count_found < bear.count_total:
            bear.count_found += 1
            bear.save()
        elif direction == "down" and bear.count_found > 0:
            bear.count_found -= 1
            bear.save()
        return JsonResponse({"success": True, "count_found": bear.count_found})
    except TeddyBear.DoesNotExist:
        return JsonResponse({"success": False, "error": "Teddy Bear not found"}, status=404)


def fallout3_achievements(request):
    achievements = Achievement.objects.all().order_by('id')
    grouped = OrderedDict()
    section_stats = {}
    total_acquired = 0
    total_items = 0
    total_points_acquired = 0
    total_points = 0

    for a in achievements:
        grouped.setdefault(a.title, []).append(a)
    for title, items in grouped.items():
        acquired = sum(1 for i in items if getattr(i, "acquired", False))
        count = len(items)
        # Points calculations:
        points_acquired = sum(getattr(i, "points", 0) for i in items if getattr(i, "acquired", False))
        points_total = sum(getattr(i, "points", 0) for i in items)
        percent = round(100 * acquired / count) if count else 0
        section_stats[title] = {
            "acquired": acquired,
            "count": count,
            "percent": percent,
            "points_acquired": points_acquired,
            "points_total": points_total,
        }
        total_acquired += acquired
        total_items += count
        total_points_acquired += points_acquired
        total_points += points_total

    overall_percent = round(100 * total_acquired / total_items) if total_items else 0
    overall_points_percent = round(100 * total_points_acquired / total_points) if total_points else 0

    return render(request, "fallout3/achievements.html", {
        "grouped": grouped,
        "section_stats": section_stats,
        "total_acquired": total_acquired,
        "total_items": total_items,
        "overall_percent": overall_percent,
        "total_points_acquired": total_points_acquired,
        "total_points": total_points,
        "overall_points_percent": overall_points_percent,
        "menu_items": FALLOUT3_MENU_ITEMS,
        "active_menu": "fallout3_achievements",
    })


@require_POST
def toggle_achievement_field(request):
    achievement_id = request.POST.get("id")
    value = request.POST.get("value") == "true"
    try:
        achievement = Achievement.objects.get(id=achievement_id)
        achievement.unlocked = value
        achievement.save()
        return JsonResponse({"success": True})
    except Achievement.DoesNotExist:
        return JsonResponse({"success": False, "error": "Achievement not found"}, status=404)
