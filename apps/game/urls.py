
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import BoardView
from .apiview import BoardApiCreate,BoardApiUpdate

urlpatterns = [
    path('board/', BoardView.as_view(), name='board'),
    path('api_game/', BoardApiCreate.as_view(), name='api_post'),
    path('api_game/<int:id>/', BoardApiUpdate.as_view(), name='api_put'),
]

urlpatterns = format_suffix_patterns(urlpatterns)