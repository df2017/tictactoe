
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import getlist, move,reset
from .apiview import BoardApiUpdate,BoardList,BoardDetail, MoveDetail, PlayerList, PlayerApiUpdate


urlpatterns = [
    path('board/', getlist, name='board'),
    path('move/<int:mov>/', move, name='move'),
    path('reset/', reset, name='reset'),
    path('api_game/', PlayerList.as_view(), name='apiplayerget'),
    path('api_game/list/', BoardList.as_view(), name='apilistget'),
    path('api_game/list/<int:pk>/', BoardDetail.as_view(), name="apidetailget"),
    path('api_game/position/<int:id>/', BoardApiUpdate.as_view(), name='apipositionput'),
    path('api_game/move/<int:pk>/', MoveDetail.as_view(), name='apipmoveget'),
    path('api_game/<int:id>/', PlayerApiUpdate.as_view(), name='apiplayerput'),
]

urlpatterns = format_suffix_patterns(urlpatterns)