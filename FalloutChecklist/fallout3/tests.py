from django.test import TestCase
from .models import Quest, Bobblehead, SkillBook, RareItem, AlienCaptiveLog, NukaColaQuantum, Clothing, Weapon, TeddyBear, Achievement


class ModelStrTests(TestCase):
    def test_quest_str_and_defaults(self):
        quest = Quest.objects.create(title="Main Quest", name="Escape")
        self.assertEqual(str(quest), "Main Quest")
        self.assertFalse(quest.found)
        self.assertFalse(quest.completed)

    def test_bobblehead_str_and_default(self):
        bob = Bobblehead.objects.create(name="Strength", location="Vault 101")
        self.assertEqual(str(bob), "Strength")
        self.assertFalse(bob.acquired)

    def test_skillbook_str_and_defaults(self):
        book = SkillBook.objects.create(title="Lockpick", name="DC Journal", count_total=5)
        self.assertEqual(str(book), "DC Journal: Lockpick")
        self.assertEqual(book.count_found, 0)

    def test_rareitem_str_and_default(self):
        item = RareItem.objects.create(title="Ant's Sting", note="Unique Weapon")
        self.assertEqual(str(item), "Ant's Sting - Unique Weapon")
        self.assertFalse(item.acquired)

    def test_alienlog_str_and_default(self):
        log = AlienCaptiveLog.objects.create(name="Log 1", location="Mothership")
        self.assertEqual(str(log), "Log 1")
        self.assertFalse(log.acquired)

    def test_nukacola_str_and_defaults(self):
        quantum = NukaColaQuantum.objects.create(title="Supermarket", location="Aisle")
        self.assertEqual(str(quantum), "Supermarket - Aisle")
        self.assertEqual(quantum.count_found, 0)
        self.assertEqual(quantum.count_total, 1)

    def test_clothing_str_and_default(self):
        clothing = Clothing.objects.create(title="Armor", name="Vault Suit")
        self.assertEqual(str(clothing), "Armor - Vault Suit")
        self.assertFalse(clothing.acquired)

    def test_weapon_str_and_default(self):
        weapon = Weapon.objects.create(title="Melee", name="Shishkebab")
        self.assertEqual(str(weapon), "Melee - Shishkebab")
        self.assertFalse(weapon.acquired)

    def test_teddybear_str_and_defaults(self):
        bear = TeddyBear.objects.create(title="Tenpenny", location="Suite", count_total=2)
        self.assertEqual(str(bear), "Tenpenny - Suite")
        self.assertEqual(bear.count_found, 0)
        self.assertEqual(bear.count_total, 2)

    def test_achievement_str_and_defaults(self):
        ach = Achievement.objects.create(title="Story", name="Complete Quest", points=10)
        self.assertEqual(str(ach), "Story - Complete Quest")
        self.assertFalse(ach.acquired)
