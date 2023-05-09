from django.urls import path
from django.conf.urls.i18n import i18n_patterns
from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView
from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.admin.views.decorators import staff_member_required
from . import views

app_name = "offer"  # добавьте это, если используете пространства имен


urlpatterns = [
    path("admin/", admin.site.urls),
    path("helpers/", views.HelperListView.as_view(), name="helper_list"),
    path("helpers/add/", views.helper_form, name="add_helper"),
    path(
        "helpers/<int:pk>/update/",
        views.HelperUpdateView.as_view(),
        name="update_helper_info",
    ),
    path(
        "helpers/<int:pk>/delete/",
        views.HelperDeleteView.as_view(),
        name="delete_helper",
    ),
    path("success/", views.success, name="success"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    # + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
