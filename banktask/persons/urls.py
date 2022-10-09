from django.urls import path

from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_page, name='logout'),
    path('register/', views.register, name='register'),
    path('apply/', views.apply, name='apply'),
    path('add/', views.person_create_view, name='person_add'),
    path('<int:pk>/', views.person_update_view, name='person_change'),


    path('ajax/load-cities/', views.load_cities, name='ajax_load_cities'), # AJAX
]