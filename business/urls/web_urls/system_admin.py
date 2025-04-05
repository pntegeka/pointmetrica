from django.urls import path

from business.views.web_views.system_admin import SystemAdminActiveBusinessList

urlpatterns = [
    path(
        'system_admin_business_list/',
        SystemAdminActiveBusinessList.as_view(),
        name="system_admin_business_list"
    ),
]