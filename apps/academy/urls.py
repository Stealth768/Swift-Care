from django.urls import path
from .views import tutorial_list, tutorial_detail, tutorial_first_aid, tutorial_diagnostic, tutorial_operations

urlpatterns = [
    path('', tutorial_list, name='academy'),
    path('<int:tutorial_id>/', tutorial_detail, name='academy_detail'),
    path('procedures/', tutorial_detail, {'tutorial_id': 1}, name='academy_procedures'),
    path('first-aid/', tutorial_first_aid, name='tutorial_first_aid'),
    path('diagnostic/', tutorial_diagnostic, name='tutorial_diagnostic'),
    path('operations/', tutorial_operations, name='tutorial_operations'),
]