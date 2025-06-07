from django.urls import path
from . import views


urlpatterns = [
    path('quests/', views.fallout3_quests, name='fallout3_quests'),
    path('quests/toggle/', views.toggle_quest_field, name='toggle_quest_field'),
    path('bobbleheads/', views.fallout3_bobbleheads, name='fallout3_bobbleheads'),
    path('bobbleheads/toggle/', views.toggle_bobblehead_field, name='toggle_bobblehead_field'),
    path('skillbooks/', views.fallout3_skillbooks, name='fallout3_skillbooks'),
    path('skillbooks/update/', views.update_skillbook_count, name='update_skillbook_count'),
    path('rareitems/', views.fallout3_rareitems, name='fallout3_rareitems'),
    path('rareitems/toggle/', views.toggle_rareitem_field, name='toggle_rareitem_field'),
    path('alienlogs/', views.fallout3_alienlogs, name='fallout3_alienlogs'),
    path('alienlogs/toggle/', views.toggle_alienlog_field, name='toggle_alienlog_field'),
    path('nukacolaquantums/', views.fallout3_nukacolaquantums, name='fallout3_nukacolaquantums'),
    path('nukacolaquantums/update/', views.update_nukacola_count, name='update_nukacola_count'),
    path('clothing/', views.fallout3_clothing, name='fallout3_clothing'),
    path('clothing/toggle/', views.toggle_clothing_field, name='toggle_clothing_field'),
    path('weapons/', views.fallout3_weapons, name='fallout3_weapons'),
    path('weapons/toggle/', views.toggle_weapon_field, name='toggle_weapon_field'),
    path('teddybears/', views.fallout3_teddybears, name='fallout3_teddybears'),
    path('teddybears/update/', views.update_teddybear_count, name='update_teddybear_count'),
]
