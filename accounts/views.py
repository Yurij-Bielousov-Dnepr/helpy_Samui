from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.utils.translation import gettext_lazy as _
from django.contrib import messages
from django.views import generic
from .forms import CustomUserCreationForm, CustomPasswordChangeForm
from . import forms
from .forms import AddEmailForm, RemoveEmailForm, EditVisitorProfileForm, EmailForm
from .forms import VisitorForm, CustomAuthenticationForm
from django.contrib.auth import views as auth_views, authenticate
from django.views.generic import TemplateView, FormView, CreateView
from django.contrib.auth import login as auth_login
from .models import MyUser
from django.contrib.auth.views import (
    LoginView, LogoutView, PasswordChangeView, PasswordResetView,
    PasswordResetConfirmView, PasswordResetCompleteView, PasswordResetDoneView
)
from .forms import CustomAuthenticationForm  # Импортируйте вашу кастомную форму аутентификации, если она используется
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth import login




class EmailConfirmView(TemplateView):
    template_name = 'accounts/email_confirm.html'


class VIPView(TemplateView):
    template_name = 'VIP.html'
class AccountInactiveView(TemplateView):
    template_name = 'accounts/account_inactive.html'
class EmailView(View):
    @method_decorator(login_required)
    def get(self, request):
        form = EmailForm()
        return render(request, 'email.html', {'form': form})

    class EmailView( TemplateView ):
        template_name = 'accounts/email.html'

    @method_decorator(login_required)
    def post(self, request):
        form = EmailForm(request.POST)
        if form.is_valid():
            # Здесь должна быть логика для отправки подтверждающего письма на указанный email
            return HttpResponseRedirect(reverse('email_confirm'))
        else:
            messages.error(request, 'Пожалуйста, проверьте свой адрес электронной почты и попробуйте снова.')
            return render(request, 'email.html', {'form': form})

class SignInView(LoginView):
    template_name = 'accounts/sign_in.html'  # Укажите путь к вашему шаблону аутентификации
    form_class = CustomAuthenticationForm  # Укажите вашу кастомную форму аутентификации, если она используется

    def sign_in_user(self, request, user_object):
        login( request, user_object )



class CustomPasswordChangeView(PasswordChangeView):
    form_class = CustomPasswordChangeForm
    template_name = 'change_password.html'
    success_url = '/password_change_done/'
class AuthLoginView(LoginView):
    template_name = 'accounts/sign_in.html'


class PasswordSetView(PasswordChangeView):
    template_name = 'accounts/password_set.html'
    success_url = 'accounts:password_change_done'  # замените на ваш URL

class PasswordResetFromKeyView(PasswordResetConfirmView):
    template_name = 'accounts/password_reset_confirm.html'
    success_url = 'accounts:password_reset_complete'  # замените на ваш URL

class PasswordResetFromKeyDoneView(PasswordResetCompleteView):
    template_name = 'accounts/password_reset_complete.html'

class PasswordChangeView(PasswordChangeView):
    template_name = 'accounts/password_change.html'
    success_url = 'accounts:password_change_done'  # замените на ваш URL


@login_required
def edit_visitor_profile(request):
    visitor = request.MyUser
    if request.method == "POST":
        form = EditVisitorProfileForm(request.POST, instance=visitor)
        if form.is_valid():
            form.save()
            return redirect("profile")
    else:
        form = EditVisitorProfileForm(instance=visitor)
    return render(request, "accounts/edit_visitor_profile.html", {"form": form})


@login_required
def account_email(request):
    visitor = request.MyUser
    visitor_form = AddEmailForm(request.POST or None)
    remove_form = RemoveEmailForm(request.POST or None)

    if request.method == "POST":
        if "action_add" in request.POST and visitor_form.is_valid():
            email = visitor_form.cleaned_data["email"]
            visitor.email_user(
                subject=_("Verify your email address"),
                message=_(
                    "Please click on the following link to verify your email address: {0}{1}"
                ).format(
                    request.build_absolute_uri(reverse_lazy("account_email_verify")),
                    "?email={}".format(email),
                ),
                from_email="no-reply@example.com",
            )
            messages.success(request, _("Verification email sent to {0}").format(email))
            return redirect(reverse_lazy("account_email"))

        if "action_remove" in request.POST and remove_form.is_valid():
            email = remove_form.cleaned_data["email"]
            if email == visitor.email:
                messages.error(
                    request, _("You cannot remove your primary email address")
                )
            else:
                visitor.emailaddress_set.filter(email=email).delete()
                messages.success(request, _("Email address {0} removed").format(email))
            return redirect(reverse_lazy("account_email"))

    context = {
        "visitor": MyUser,
        "visitor_form": visitor_form,
        "remove_form": remove_form,
    }
    return render(request, "accounts/email.html", context)


def success(request):
    return render(request, "offer/success.html")

class LoginView(generic.FormView):
    form_class = CustomAuthenticationForm
    template_name = "accounts/sign_in.html"
    success_url = reverse_lazy("index")

class LogoutView(auth_views.LogoutView):
    template_name = "accounts/sign_in.html"
    next_page = reverse_lazy("sign_in")

class SignupView(CreateView):
    form_class = forms.CustomUserCreationForm  # замените на вашу форму регистрации
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy( 'accounts:verification_sent' )

    def form_valid(self, form):
        response = super().form_valid( form )
        sign_in_view = SignInView()
        sign_in_view.sign_in_user( self.request, self.object )  # Замените login на ваш метод sign_in_user
        return response

# запасная вьюха навырост
# class SignupView(FormView):
#     form_class = UserCreationForm
#     template_name = "accounts/signup.html"
#     success_url = reverse_lazy("index")  # здесь нужно указать URL главной страницы
#
#     def form_valid(self, form):
#         response = super().form_valid(form)
#         user = form.save()
#         auth_login(self.request, user)  # авторизуем пользователя
#         return response
#
#     def get(self, request):
#         form = self.form_class()
#         return render(request, self.template_name, {"form": form})
#
#     def post(self, request):
#         form = self.form_class(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get("username")
#             password = form.cleaned_data.get("password1")
#             user = authenticate(username=username, password=password)
#             auth_login(request, user)  # авторизуем пользователя
#             return redirect("home")
#         else:
#             messages.error(request, "Invalid form submission.")
#             return render(request, self.template_name, {"form": form})
#
#
# login_view = LoginView.as_view()
# logout_view = LogoutView.as_view()
# signup_view = SignupView.as_view()


