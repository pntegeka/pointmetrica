from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views.generic import View


class AuthenticationProcessorView(View, LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_superuser:
            return redirect('system_admin_active_business_list')
        else:
            return redirect('tenant_user_landing')


def user_logged_in(request):
    if request.user.is_authenticated:
        username = request.user.get_username
    else:
        username = None
    return username


def logout_view(request):
    username = user_logged_in(request)
    if username is not None:
        logout(request)
        return redirect("kagi:login")