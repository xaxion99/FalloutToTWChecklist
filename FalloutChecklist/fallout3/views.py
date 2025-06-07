from collections import OrderedDict

from django.http import HttpResponseBadRequest, JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_POST

from .models import Quest, Bobblehead, SkillBook, RareItem, AlienCaptiveLog, NukaColaQuantum, Clothing, Weapon, \
    TeddyBear

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
]


def home(request):
    return render(request, "home.html")


def fallout3_quests(request):
    quests = Quest.objects.all().order_by('id')

    section_order = []
    grouped = OrderedDict()
    for q in quests:
        if q.title not in grouped:
            section_order.append(q.title)
            grouped[q.title] = []
        grouped[q.title].append(q)

    return render(request, "fallout3/quests.html", {
        "grouped": grouped,
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
    return render(request, "fallout3/bobbleheads.html", {
        "bobbleheads": bobbleheads,
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
    return render(request, "fallout3/skillbooks.html", {
        "skillbooks": skillbooks,
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
    for item in rareitems:
        grouped.setdefault(item.title, []).append(item)
    return render(request, "fallout3/rareitems.html", {
        "grouped": grouped,
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
    return render(request, "fallout3/alienlogs.html", {
        "logs": logs,
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
    for q in quantums:
        grouped.setdefault(q.title, []).append(q)
    return render(request, "fallout3/nukacolaquantums.html", {
        "grouped": grouped,
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
    for item in clothing:
        grouped.setdefault(item.title, []).append(item)
    return render(request, "fallout3/clothing.html", {
        "grouped": grouped,
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
    for item in weapons:
        grouped.setdefault(item.title, []).append(item)
    return render(request, "fallout3/weapons.html", {
        "grouped": grouped,
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
    for bear in bears:
        grouped.setdefault(bear.title, []).append(bear)
    return render(request, "fallout3/teddybears.html", {
        "grouped": grouped,
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
