from django.test import TestCase, Client
from django.urls import reverse
from .models import (
    Quest,
    Bobblehead,
    SkillBook,
    RareItem,
    AlienCaptiveLog,
    NukaColaQuantum,
    Clothing,
    Weapon,
    TeddyBear,
    Achievement,
)
from .views import (
    calculate_quest_stats,
    calculate_bobblehead_stats,
    calculate_skillbook_stats,
    calculate_rareitem_stats,
    calculate_alienlog_stats,
    calculate_nukacola_stats,
    calculate_clothing_stats,
    calculate_weapon_stats,
    calculate_teddybear_stats,
    calculate_achievement_stats,
)


class ModelStrTests(TestCase):
    def test_quest_str_and_defaults(self):
        quest = Quest.objects.create(
            title="Tutorial",
            name="Future Imperfect",
            note="Final tutorial mission in Fallout 3",
            acquired="Dad",
            location="Vault 101",
            rewards="Tagging 3 skills"
        )
        self.assertEqual(str(quest), "Tutorial")
        self.assertEqual(quest.name, "Future Imperfect")
        self.assertEqual(quest.note, "Final tutorial mission in Fallout 3")
        self.assertEqual(quest.acquired, "Dad")
        self.assertEqual(quest.location, "Vault 101")
        self.assertEqual(quest.rewards, "Tagging 3 skills")
        self.assertFalse(quest.found)
        self.assertFalse(quest.completed)

    def test_bobblehead_str_and_default(self):
        bob = Bobblehead.objects.create(
            name="Strength",
            location="Megaton: Lucas Simms' house, on the desk in the bedroom (the door to the immediate left at the "
                     "top of stairs) on the second floor. His house is directly to the right when entering Megaton."
        )
        self.assertEqual(str(bob), "Strength")
        self.assertEqual(
            bob.location,
            "Megaton: Lucas Simms' house, on the desk in the bedroom (the door to the immediate left at the top of "
            "stairs) on the second floor. His house is directly to the right when entering Megaton."
        )
        self.assertFalse(bob.acquired)

    def test_skillbook_str_and_defaults(self):
        book = SkillBook.objects.create(
            title="U.S. Army: 30 Handy Flamethrower Recipes",
            name="Big Guns",
            count_found=1,
            count_total=5
        )
        self.assertEqual(str(book), "Big Guns: U.S. Army: 30 Handy Flamethrower Recipes")
        self.assertEqual(book.title, "U.S. Army: 30 Handy Flamethrower Recipes")
        self.assertEqual(book.name, "Big Guns")
        self.assertEqual(book.count_found, 1)
        self.assertEqual(book.count_total, 5)

    def test_rareitem_str_and_default(self):
        item = RareItem.objects.create(
            title="Museum of History Items",
            note="Lincoln’s Hat"
        )
        self.assertEqual(str(item), "Museum of History Items - Lincoln’s Hat")
        self.assertEqual(item.title, "Museum of History Items")
        self.assertEqual(item.note, "Lincoln’s Hat")
        self.assertFalse(item.acquired)

    def test_alienlog_str_and_default(self):
        log = AlienCaptiveLog.objects.create(
            name="Log #19",
            location="Waste Disposal",
            notes="Log #19 is only accessible once!"
        )
        self.assertEqual(str(log), "Log #19")
        self.assertEqual(log.location, "Waste Disposal")
        self.assertEqual(log.notes, "Log #19 is only accessible once!")
        self.assertFalse(log.acquired)

    def test_nukacola_str_and_defaults(self):
        quantum = NukaColaQuantum.objects.create(
            title="Mothership Zeta",
            location="Engineering Core",
            count_found=4,
            count_total=6
        )
        self.assertEqual(str(quantum), "Mothership Zeta - Engineering Core")
        self.assertEqual(quantum.title, "Mothership Zeta")
        self.assertEqual(quantum.location, "Engineering Core")
        self.assertEqual(quantum.count_found, 4)
        self.assertEqual(quantum.count_total, 6)

    def test_clothing_str_and_default(self):
        clothing = Clothing.objects.create(
            title="Capital Wasteland",
            name="Shady Hat"
        )
        self.assertEqual(str(clothing), "Capital Wasteland - Shady Hat")
        self.assertEqual(clothing.title, "Capital Wasteland")
        self.assertEqual(clothing.name, "Shady Hat")
        self.assertFalse(clothing.acquired)

    def test_weapon_str_and_default(self):
        weapon = Weapon.objects.create(
            title="Point Lookout",
            name="The Dismemberer"
        )
        self.assertEqual(str(weapon), "Point Lookout - The Dismemberer")
        self.assertEqual(weapon.title, "Point Lookout")
        self.assertEqual(weapon.name, "The Dismemberer")
        self.assertFalse(weapon.acquired)

    def test_teddybear_str_and_defaults(self):
        bear = TeddyBear.objects.create(
            title="Capital Wasteland",
            location="Agatha’s House",
            notes="All must be stolen",
            count_found=1,
            count_total=1
        )
        self.assertEqual(str(bear), "Capital Wasteland - Agatha’s House")
        self.assertEqual(bear.title, "Capital Wasteland")
        self.assertEqual(bear.location, "Agatha’s House")
        self.assertEqual(bear.notes, "All must be stolen")
        self.assertEqual(bear.count_found, 1)
        self.assertEqual(bear.count_total, 1)

    def test_achievement_str_and_defaults(self):
        ach = Achievement.objects.create(
            title="Capital Wasteland",
            name="Vault‑Tec C.E.O.",
            requirement="Collected 20 Vault‑Tec bobbleheads",
            points=30
        )
        self.assertEqual(str(ach), "Capital Wasteland - Vault‑Tec C.E.O.")
        self.assertEqual(ach.title, "Capital Wasteland")
        self.assertEqual(ach.name, "Vault‑Tec C.E.O.")
        self.assertEqual(ach.requirement, "Collected 20 Vault‑Tec bobbleheads")
        self.assertEqual(ach.points, 30)
        self.assertFalse(ach.acquired)


class StatsTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Quests
        Quest.objects.create(title="Main", name="Quest 1", found=True, completed=True)
        Quest.objects.create(title="Main", name="Quest 2")

        # Bobbleheads
        Bobblehead.objects.create(name="Strength", location="Vault 101", acquired=True)
        Bobblehead.objects.create(name="Perception", location="Rivet City", acquired=False)

        # Skill Books
        SkillBook.objects.create(title="Lockpick", name="DC Journal", count_found=1, count_total=2)
        SkillBook.objects.create(title="Science", name="Test Manual", count_found=1, count_total=1)

        # Rare Items
        RareItem.objects.create(title="Ant's Sting", note="Unique", acquired=True)
        RareItem.objects.create(title="The Shocker", note="Unique", acquired=False)

        # Alien Captive Logs
        AlienCaptiveLog.objects.create(name="Log1", location="Ship", acquired=True)
        AlienCaptiveLog.objects.create(name="Log2", location="Ship", acquired=False)

        # Nuka Cola Quantums
        NukaColaQuantum.objects.create(title="Supermarket", location="Aisle", count_found=1, count_total=2)
        NukaColaQuantum.objects.create(title="Factory", location="Room", count_found=0, count_total=1)

        # Clothing
        Clothing.objects.create(title="Armor", name="Vault Suit", acquired=True)
        Clothing.objects.create(title="Armor", name="Jumpsuit", acquired=False)

        # Weapons
        Weapon.objects.create(title="Melee", name="Knife", acquired=True)
        Weapon.objects.create(title="Melee", name="Club", acquired=False)

        # Teddy Bears
        TeddyBear.objects.create(title="Home", location="Bedroom", count_found=1, count_total=2)
        TeddyBear.objects.create(title="Home", location="Kitchen", count_found=0, count_total=1)

        # Achievements
        Achievement.objects.create(title="Story", name="Complete Quest", points=10, acquired=True)
        Achievement.objects.create(title="Story", name="Kill 100", points=20, acquired=False)

    def test_dashboard_stats(self):
        client = Client()
        response = client.get(reverse("fallout3_dashboard"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["total_completed"], 11)
        self.assertEqual(response.context["total_items"], 23)
        self.assertEqual(response.context["total_percent"], 48)
        self.assertEqual(response.context["total_points_acquired"], 10)
        self.assertEqual(response.context["total_points"], 30)
        self.assertEqual(response.context["total_points_percent"], 33)

    def test_quest_stats(self):
        stats = calculate_quest_stats(Quest.objects.all())
        self.assertEqual(stats["total_found"], 1)
        self.assertEqual(stats["total_completed"], 1)
        self.assertEqual(stats["total_quests"], 2)
        self.assertEqual(stats["overall_found_percent"], 50)
        self.assertEqual(stats["overall_completed_percent"], 50)
        self.assertEqual(stats["section_stats"]["Main"]["found"], 1)

    def test_bobblehead_stats(self):
        stats = calculate_bobblehead_stats()
        self.assertEqual(stats["total_acquired"], 1)
        self.assertEqual(stats["total_items"], 2)
        self.assertEqual(stats["overall_percent"], 50)

    def test_skillbook_stats(self):
        stats = calculate_skillbook_stats()
        self.assertEqual(stats["total_found"], 2)
        self.assertEqual(stats["total"], 3)
        self.assertEqual(stats["overall_percent"], 67)

    def test_rareitem_stats(self):
        stats = calculate_rareitem_stats()
        self.assertEqual(stats["total_acquired"], 1)
        self.assertEqual(stats["total_items"], 2)
        self.assertEqual(stats["overall_percent"], 50)
        self.assertEqual(stats["section_stats"]["Ant's Sting"]["percent"], 100)

    def test_alienlog_stats(self):
        stats = calculate_alienlog_stats()
        self.assertEqual(stats["total_acquired"], 1)
        self.assertEqual(stats["total_items"], 2)
        self.assertEqual(stats["overall_percent"], 50)

    def test_nukacola_stats(self):
        stats = calculate_nukacola_stats()
        self.assertEqual(stats["total_found"], 1)
        self.assertEqual(stats["total_total"], 3)
        self.assertEqual(stats["overall_percent"], 33)

    def test_clothing_stats(self):
        stats = calculate_clothing_stats(Clothing.objects.all())
        self.assertEqual(stats["total_acquired"], 1)
        self.assertEqual(stats["total_items"], 2)
        self.assertEqual(stats["overall_percent"], 50)

    def test_weapon_stats(self):
        stats = calculate_weapon_stats(Weapon.objects.all())
        self.assertEqual(stats["total_acquired"], 1)
        self.assertEqual(stats["total_items"], 2)
        self.assertEqual(stats["overall_percent"], 50)

    def test_teddybear_stats(self):
        stats = calculate_teddybear_stats()
        self.assertEqual(stats["total_found"], 1)
        self.assertEqual(stats["total_total"], 3)
        self.assertEqual(stats["overall_percent"], 33)

    def test_achievement_stats(self):
        stats = calculate_achievement_stats()
        self.assertEqual(stats["total_acquired"], 1)
        self.assertEqual(stats["total_items"], 2)
        self.assertEqual(stats["overall_percent"], 50)
        self.assertEqual(stats["total_points_acquired"], 10)
        self.assertEqual(stats["total_points"], 30)
