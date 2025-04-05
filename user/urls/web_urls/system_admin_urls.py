from django.urls import path

from user.views.web_views.system_admin_views import logout_view, AuthenticationProcessorView

urlpatterns = [
    path(
        'authentication_processor/',
        AuthenticationProcessorView.as_view(),
        name='authentication_processor'
    ),
    path(
        'logout/',
        logout_view,
        name='logout'
    ),
]