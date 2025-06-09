from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Quest, Bobblehead, SkillBook, RareItem, AlienCaptiveLog, NukaColaQuantum, Clothing, Weapon, \
    TeddyBear, Achievement


class QuestResource(resources.ModelResource):
    class Meta:
        model = Quest

@admin.register(Quest)
class QuestAdmin(ImportExportModelAdmin):
    resource_class = QuestResource
    list_display = ('title', 'name', 'found', 'completed')
    list_filter = ('found', 'completed')


class BobbleheadResource(resources.ModelResource):
    class Meta:
        model = Bobblehead

@admin.register(Bobblehead)
class BobbleheadAdmin(ImportExportModelAdmin):
    resource_class = BobbleheadResource
    list_display = ('name', 'location', 'acquired')
    list_filter = ('acquired',)


class SkillBookResource(resources.ModelResource):
    class Meta:
        model = SkillBook

@admin.register(SkillBook)
class SkillBookAdmin(ImportExportModelAdmin):
    resource_class = SkillBookResource
    list_display = ('name', 'title', 'count_found', 'count_total')


class RareItemResource(resources.ModelResource):
    class Meta:
        model = RareItem

@admin.register(RareItem)
class RareItemAdmin(ImportExportModelAdmin):
    resource_class = RareItemResource
    list_display = ('title', 'note', 'acquired')
    list_filter = ('acquired',)


class AlienCaptiveLogResource(resources.ModelResource):
    class Meta:
        model = AlienCaptiveLog

@admin.register(AlienCaptiveLog)
class AlienCaptiveLogAdmin(ImportExportModelAdmin):
    resource_class = AlienCaptiveLogResource
    list_display = ('name', 'location', 'acquired')
    list_filter = ('acquired',)


class NukaColaQuantumResource(resources.ModelResource):
    class Meta:
        model = NukaColaQuantum

@admin.register(NukaColaQuantum)
class NukaColaQuantumAdmin(ImportExportModelAdmin):
    resource_class = NukaColaQuantumResource
    list_display = ('title', 'location', 'count_found', 'count_total')
    list_filter = ('title',)



class ClothingResource(resources.ModelResource):
    class Meta:
        model = Clothing

@admin.register(Clothing)
class ClothingAdmin(ImportExportModelAdmin):
    resource_class = ClothingResource
    list_display = ('title', 'name', 'acquired')
    list_filter = ('title', 'acquired')


class WeaponResource(resources.ModelResource):
    class Meta:
        model = Weapon

@admin.register(Weapon)
class WeaponAdmin(ImportExportModelAdmin):
    resource_class = WeaponResource
    list_display = ('title', 'name', 'acquired')
    list_filter = ('title', 'acquired')


class TeddyBearResource(resources.ModelResource):
    class Meta:
        model = TeddyBear

@admin.register(TeddyBear)
class TeddyBearAdmin(ImportExportModelAdmin):
    resource_class = TeddyBearResource
    list_display = ('title', 'location', 'count_found', 'count_total')
    list_filter = ('title',)


class AchievementResource(resources.ModelResource):
    class Meta:
        model = Achievement

@admin.register(Achievement)
class AchievementAdmin(ImportExportModelAdmin):
    resource_class = AchievementResource
    list_display = ('title', 'name', 'unlocked')
    search_fields = ('title', 'name')
    list_filter = ('unlocked',)
