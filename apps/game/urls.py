
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import BoardView, MoveView
from .apiview import BoardApi

urlpatterns = [
    path('board/', BoardView.as_view(), name='board'),
    path('move/', MoveView.as_view(), name='move'),
    path('api_game/<int:id>/', BoardApi.as_view(), name='apiboard'),
]

urlpatterns = format_suffix_patterns(urlpatterns)