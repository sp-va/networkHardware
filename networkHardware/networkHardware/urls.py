"""
URL configuration for networkHardware project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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

from ..equipment import views as equipment_views
from ..users import views as users_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/equipment', equipment_views.get_equipment_list, name='equipment-list'),
    path('api/equipment/<uuid:id>', equipment_views.get_equipment_detail, name='equipment-detail'),
    path('api/equipment', equipment_views.create_equipment, name='equipment-create'),
    path('api/equipment/<uuid:id>', equipment_views.update_equipment, name='equipment-update'),
    path('api/equipment/<uuid:id>', equipment_views.delete_equipment, name='equipment-delete'),

    path('api/equipment-type', equipment_views.get_equipment_type_list, name='equipment-type-list'),

    path('api/user/login', users_views.user_login, name='user-login'),
]
