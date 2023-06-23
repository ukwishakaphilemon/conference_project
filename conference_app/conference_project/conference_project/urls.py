"""
URL configuration for conference_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view, name='home'),
    path('<str:number>/', views.testing_stuff, name='testing'),
    path('conferences/', views.conference_list, name='conf_list'),
    path('conferences/create/', views.conference_create, name='conf_create'),
    path('conferences/<int:conference_id>/', views.conference_details, name='conf_details'),
    path('conferences/<int:conference_id>/update/', views.conference_update, name='conf_update'),
    path('conferences/<int:conference_id>/delete/', views.conference_delete, name='conf_delete'),
]
