from django.urls import path
from .views import tutorial_list, tutorial_detail

urlpatterns = [
    path('', tutorial_list, name='academy'),
    path('<int:tutorial_id>/', tutorial_detail, name='academy_detail'),
    path('procedures/', tutorial_detail, {'tutorial_id': 1}, name='academy_procedures'),
]