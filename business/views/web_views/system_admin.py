from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.urls import reverse
from django.core.exceptions import PermissionDenied
from django.db.models import Q

from business.forms import BusinessForm, SearchForm
from business.models import Business


class SystemAdminActiveBusinessList(LoginRequiredMixin, ListView):
    model = Business
    context_object_name = 'businesses'
    paginate_by = 25
    template_name = 'business/business_list.html'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.search_term = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_term'] = self.search_term
        context['search_form'] = SearchForm()
        return context

    def get_queryset(self):
        search_query = self.request.GET.get('search_query')
        queryset = Business.objects.filter(is_active=True)

        if search_query:
            queryset = queryset.filter(name__icontains=search_query)
            self.search_term = search_query
        else:
            self.search_term = None

        return queryset

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied


class SystemAdminBusinessCreate(LoginRequiredMixin, CreateView):
    model = Business
    # template_name = ''
    form_class = BusinessForm

    def get_success_url(self):
        return reverse('system_admin_active_company_list')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied


class SystemAdminBusinessUpdate(LoginRequiredMixin, UpdateView):
    model = Business
    # template_name = ''
    form_class = BusinessForm

    def get_success_url(self):
        return reverse('system_admin_active_company_list')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied


class SystemAdminBusinessDelete(LoginRequiredMixin, DeleteView):
    model = Business
    # template_name = ''

    def get_success_url(self):
        return reverse('system_admin_active_company_list')

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied