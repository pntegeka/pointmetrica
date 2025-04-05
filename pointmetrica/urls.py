from django.urls import path, include, reverse_lazy
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import RedirectView

urlpatterns = [
    path("", RedirectView.as_view(url=reverse_lazy("kagi:login")), name="index"),
    path("", include("kagi.urls")),
    # Business Specific Web URLs
    path("business/", include("business.urls.web_urls.system_admin")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
