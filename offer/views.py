# views.py
from datetime import date
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.admin.views.decorators import staff_member_required
from django.core.paginator import Paginator
from django.db.models import Count, Q
from django.forms import ModelForm
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy, reverse
from django.utils.translation import gettext as _
from django.views import View
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.views.generic.edit import FormView
from django_countries import countries
from accounts.models import MyUser
from .decorators import admin_only
from .forms import LanguageForm, RegionForm, Tag_helpForm, SupportLevelForm, HelpForm, HelpRequestForm, HelperCreateForm, HelperUpdateForm
from .models import Helper

from helpy.forms import *
from helpy.models import *

from .my_menu import *

@login_required
class CreateHelper(CreateView):
    model = Helper
    form_class = HelperCreateForm
    template_name = "offer/helper_form.html"
    success_url = reverse_lazy("helper_profile")

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.user_type = "helper"
        messages.success(
            self.request, _("Your helper data has been created successfully.")
        )
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, _("Please correct the errors below."))
        return super().form_invalid(form)


def add_tag(request):
    if request.method == "POST":
        form = Tag_helpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("tags_list")
    else:
        form = Tag_helpForm()

    context = {"form": form}

    # Если форма не прошла валидацию, добавляем в контекст список ошибок
    if form.errors:
        context["errors"] = form.errors

    return render(request, "offer/helper_form.html", context)


def helper_form(request):
    if request.method == "POST":
        form = HelperCreateForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Helper added successfully!")
            return redirect("offer:success")
    else:
        form = HelperCreateForm()
    return render(request, "helper_form.html", {"form": form})


def success(request):
    return render(request, "offer/success.html")


def language_form(request):
    if request.method == "POST":
        form = LanguageForm(request.POST)
        if form.is_valid():
            languages = form.cleaned_data["languages"]
            for language in languages:
                Language.objects.create(language=language)
            return redirect("helper_form")
    else:
        form = LanguageForm()
    return render(request, "offer/helper_form.html", {"form": form})



# Классы-представления для помощников (Helper)
class HelperListView(ListView):
    model = Helper
    template_name = "offer/helper_list.html"
    context_object_name = "helpers"


class HelperDeleteView(LoginRequiredMixin, DeleteView):
    model = Helper
    success_url = reverse_lazy("helper_list")
    template_name = "offer/helper_confirm_delete.html"

    def get_object(self):
        return get_object_or_404(Helper, pk=self.kwargs["pk"], user=self.request.user)

class HelperUpdateView(LoginRequiredMixin, UpdateView):
    model = Helper
    form_class = HelperUpdateForm
    template_name = "offer/update_helper.html"
    success_url = reverse_lazy("helper_profile")

    def get_object(self):
        return get_object_or_404(Helper, pk=self.kwargs["pk"], user=self.request.user)

    def form_valid(self, form):
        messages.success(
            self.request, "Your helper data has been updated successfully."
        )
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Please correct the errors below.")
        return super().form_invalid(form)
