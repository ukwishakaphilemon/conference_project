from django.urls import path, re_path
from core import views
urlpatterns = [
    # www.conference.rw
    path('', views.home_view, name='home'),
    path('<str:number>/', views.testing_stuff, name='testing'),
    path('conferences/', views.conference_list, name='conf_list'),
    path('conferences/create/', views.conference_create, name='conf_create'),
    path('conferences/<int:conference_id>/', views.conference_details, name='conf_details'),
    path('conferences/<int:conference_id>/update/', views.conference_update, name='conf_update'),
    path('conferences/<int:conference_id>/delete/', views.conference_delete, name='conf_delete'),

    path('about/', views.about_view, name='about'),

]