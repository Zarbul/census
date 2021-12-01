
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.PeopleListView.as_view(), name='list'),
    path('add/', views.PeopleCreateView.as_view(), name='add_people'),
    path('edit/<int:pk>/', views.PeopleUpdateView.as_view(), name='edit_people'),
    path('delete/<int:pk>/', views.PeopleDeleteView.as_view(), name='delete_people'),
    path('add_language/', views.LanguageCreateView.as_view(), name='add_language'),
    path('add_department/', views.DepartmentCreateView.as_view(), name='add_department'),
    # path('', PeopleListView.as_view(), name='list'),
    # path('', PeopleListView.as_view(), name='list'),
    # path('', PeopleListView.as_view(), name='list'),
]
