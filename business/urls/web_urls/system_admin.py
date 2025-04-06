from django.urls import path

from business.views.web_views.system_admin import SystemAdminActiveBusinessList, SystemAdminInActiveBusinessList, \
    SystemAdminBusinessCreate, SystemAdminBusinessUpdate, SystemAdminBusinessDelete, SystemAdminBusinessDetailView, \
    SystemAdminBusinessInventoryView, SystemAdminBusinessSalesView, SystemAdminBusinessReportingView, \
    SystemAdminBusinessTeamPerformanceView, SystemAdminBusinessSettingsView

urlpatterns = [
    path(
        'system_admin_active_business_list/',
        SystemAdminActiveBusinessList.as_view(),
        name="system_admin_active_business_list"
    ),
    path(
        'system_admin_business_settings/<uuid:pk>',
        SystemAdminBusinessSettingsView.as_view(),
        name="system_admin_business_settings"
    ),





    path(
        'system_admin_create_business/',
        SystemAdminBusinessCreate.as_view(),
        name="system_admin_create_business"
    ),
    path(
        'system_admin_update_business/<uuid:business_id>',
        SystemAdminBusinessUpdate.as_view(),
        name="system_admin_update_business"
    ),
    path(
        'system_admin_business_delete/<uuid:business_id>',
        SystemAdminBusinessDelete.as_view(),
        name="system_admin_business_delete"
    ),
    path(
        'system_admin_business_detail/<uuid:pk>',
        SystemAdminBusinessDetailView.as_view(),
        name="system_admin_business_detail"
    ),

    path(
        'system_admin_business_inventory/<uuid:pk>',
        SystemAdminBusinessInventoryView.as_view(),
        name="system_admin_business_inventory"
    ),
    path(
        'system_admin_business_sales/<uuid:pk>',
        SystemAdminBusinessSalesView.as_view(),
        name="system_admin_business_sales"
    ),
    path(
        'system_admin_business_reporting/<uuid:pk>',
        SystemAdminBusinessReportingView.as_view(),
        name="system_admin_business_reporting"
    ),
    path(
        'system_admin_team_performance/<uuid:pk>',
        SystemAdminBusinessTeamPerformanceView.as_view(),
        name="system_admin_team_performance"
    ),

















    path(
        'system_admin_inactive_business_list/',
        SystemAdminInActiveBusinessList.as_view(),
        name="system_admin_inactive_business_list"
    ),
]