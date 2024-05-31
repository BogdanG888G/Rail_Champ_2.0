from django.urls import path
from web_site.views import start, rules, maps, create_room, room_detail, check_room_existence, choose_railway, manage_railway, view_railways_by_room_number, railway_calculation_view, end_game, room_railways_graph, rules_in_game, room_railways_graph_view

urlpatterns = [
    path('', start, name='start'),
    path('rules/', rules, name='rules'),
    path('maps/', maps, name='maps'),
    path('create_room/', create_room, name='create_room'),
    path('room/<int:room_id>/', room_detail, name='room_detail'),
    path('check_room_existence/', check_room_existence, name='check_room_existence'),
    path('choose_railway/<int:room_id>/', choose_railway, name='choose_railway'),
    path('manage_railway/<int:railway_id>/', manage_railway, name='manage_railway'),
    path('view_railways/<str:room_number>/', view_railways_by_room_number, name='view_railways_by_room_number'),
    path('railway_calculation/<int:railway_id>/', railway_calculation_view, name='railway_calculation'),
    path('end_game/<int:railway_id>/', end_game, name='end_game'),
    path('manage_railway/<int:railway_id>/', manage_railway, name='manage_railway'),
    path('room_railways_graph/<int:room_id>/', room_railways_graph, name='room_railways_graph'),
    path('room_railways_graph/<int:room_id>/', room_railways_graph_view, name='room_railways_graph'),
    path('rules_in_game/<int:railway_id>/', rules_in_game, name='rules_in_game'),
]
