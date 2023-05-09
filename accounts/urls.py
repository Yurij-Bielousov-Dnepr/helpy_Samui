from django.urls import path
from django.conf.urls.i18n import i18n_patterns
from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView
from django.contrib import admin
from django.contrib.auth.views import (
     LogoutView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
)
from django.views.generic import TemplateView
# from telegram_bot.telegram_bot import set_webhook, webhook
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.admin.views.decorators import staff_member_required
from . import views
from .views import (
    AccountInactiveView,
    EmailView,
    EmailConfirmView,
    SignInView,
    SignupView,
    PasswordSetView,
    PasswordResetFromKeyView,
    PasswordResetFromKeyDoneView,
    PasswordChangeView,
    VIPView,
)


app_name = "accounts"  # добавьте это, если используете пространства имен

urlpatterns = [
    path( 'signup_closed/', TemplateView.as_view( template_name='signup_closed.html' ), name='signup_closed' ),
    path( 'logout/', LogoutView.as_view(), name='logout' ),
    path( 'verification_sent/', TemplateView.as_view( template_name='verification_sent.html' ),
          name='verification_sent' ),
    path( 'verified_email_required/', TemplateView.as_view( template_name='verified_email_required.html' ),
          name='verified_email_required' ),
    path( "account_inactive/", views.AccountInactiveView.as_view(), name="account_inactive" ),
    path( "email/", views.EmailView.as_view(), name="email" ),
    path( "email_confirm/", views.EmailConfirmView.as_view(), name="email_confirm" ),
    path( 'sign_in/', views.SignInView.as_view(), name='sign_in' ),
    path( 'signup/', views.SignupView.as_view(), name='signup' ),
    path( 'password_set/', views.PasswordSetView.as_view(), name='password_set' ),
    path( 'password_reset_from_key/', views.PasswordResetFromKeyView.as_view(), name='password_reset_from_key' ),
    path( 'password_reset_from_key_done/', views.PasswordResetFromKeyDoneView.as_view(),
          name='password_reset_from_key_done' ),
    path( 'password_change/', views.PasswordChangeView.as_view(), name='password_change' ),
    path( 'vip/', VIPView.as_view(), name='vip' ),
]

# urlpatterns = [
#     path('signup_closed/', TemplateView.as_view(template_name='signup_closed.html'), name='signup_closed'),
#     path('login/', LoginView.as_view(template_name='login.html'), name='login'),
#     path('logout/', LogoutView.as_view(), name='logout'),
#     path('verification_sent/', TemplateView.as_view(template_name='verification_sent.html'), name='verification_sent'),
#     path('verified_email_required/', TemplateView.as_view(template_name='verified_email_required.html'),
#          name='verified_email_required'),
#     path('password-reset/', PasswordResetView.as_view(template_name='password_reset.html'), name='password_reset'),
#     path('password-reset/done/', PasswordResetDoneView.as_view(template_name='password_reset_done.html'),
#          name='password_reset_done'),
#     path('password-reset/confirm/<uidb64>/<token>/',
#          PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
#     path('password-reset/complete/', PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
#          name='password_reset_complete'),
#     path( "account_inactive/", views.AccountInactiveView.as_view(), name="account_inactive" ),
#     path( "email/", views.EmailView.as_view(), name="email" ),
#     path( "email_confirm/", views.EmailConfirmView.as_view(), name="email_confirm" ),
#     path( 'sign_in/', views.SignInView.as_view(), name='sign_in' ),
#     path( 'signup/', views.SignupView.as_view(), name='signup' ),
#     path( 'password_set/', views.PasswordSetView.as_view(), name='password_set' ),
#     path( 'password_reset_from_key/', views.PasswordResetFromKeyView.as_view(), name='password_reset_from_key' ),
#     path( 'password_reset_from_key_done/', views.PasswordResetFromKeyDoneView.as_view(),
#           name='password_reset_from_key_done' ),
#     path( 'password_change/', views.PasswordChangeView.as_view(), name='password_change' ),
#     path( 'vip/', VIPView.as_view(), name='vip' ),
# ]
#    path( 'set_webhook/', set_webhook ),
#    path('webhook/', webhook, name='webhook'),
#    path('telegram_bot/', telegram_bot, name='telegram_bot'),

if settings.DEBUG:
    urlpatterns += static( settings.STATIC_URL, document_root=settings.STATIC_ROOT )
    # + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
