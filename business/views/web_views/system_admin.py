from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from django.urls import reverse
from django.core.exceptions import PermissionDenied
from datetime import date, timedelta
from django.db.models import Q

from business.forms import BusinessForm, SearchForm, DateFilterForm
from business.models import Business, Location


class SystemAdminInActiveBusinessList(LoginRequiredMixin, ListView):
    model = Business
    context_object_name = 'businesses'
    paginate_by = 25
    template_name = 'business/inactive_business_list.html' # noqa

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
        queryset = Business.objects.filter(is_active=False)

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


class SystemAdminBusinessSettingsView(LoginRequiredMixin, DetailView):
    model = Business
    template_name = 'business/settings/business_settings.html'
    context_object_name = 'business'

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied


class SystemAdminActiveBusinessList(LoginRequiredMixin, ListView):
    model = Business
    context_object_name = 'businesses'
    paginate_by = 25
    template_name = 'business/active_business_list.html' # noqa

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
    template_name = 'business/create_business.html'
    form_class = BusinessForm

    def get_success_url(self):
        return reverse('system_admin_active_business_list')

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
        return reverse('system_admin_active_business_list')

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
        return reverse('system_admin_active_business_list')

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied


class SystemAdminBusinessDetailView(LoginRequiredMixin, DetailView):
    model = Business
    template_name = 'business/business_detail.html' # noqa
    context_object_name = 'business'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Check if filters are applied
        get_data = self.request.GET

        if 'starting_date' in get_data or 'ending_date' in get_data:
            # Form will use the submitted GET values
            form = DateFilterForm(get_data)
        else:
            # Default to last 14 days
            today = date.today()
            two_weeks_ago = today - timedelta(days=14)
            form = DateFilterForm(initial={
                'starting_date': two_weeks_ago,
                'ending_date': today
            })

        context['form'] = form
        return context

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied


class SystemAdminBusinessInventoryView(LoginRequiredMixin, DetailView):
    model = Business
    template_name ='business/business_inventory.html' # noqa
    context_object_name = 'business'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = DateFilterForm()
        return context

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied


class SystemAdminBusinessSalesView(LoginRequiredMixin, DetailView):
    model = Business
    template_name = 'business/business_sales.html' # noqa
    context_object_name = 'business'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = DateFilterForm()
        return context

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied


class SystemAdminBusinessReportingView(LoginRequiredMixin, DetailView):
    model = Business
    template_name = 'business/business_reporting.html' # noqa
    context_object_name = 'business'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = DateFilterForm()
        return context

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied


class SystemAdminBusinessTeamPerformanceView(LoginRequiredMixin, DetailView):
    model = Business
    template_name = 'business/business_team_performance.html' # noqa
    context_object_name = 'business'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = DateFilterForm()
        return context

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied




