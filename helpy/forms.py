from django import forms
from django.utils.translation import gettext as _
from .models import HelpRequest, Language, SupportLevel, Region, Level, Tag_help
from offer.models import Helper
from django.forms.widgets import CheckboxSelectMultiple
from django.urls import reverse_lazy
from django.views.generic import CreateView
from helpySamui.constants import TAG_HELP_NAME_CHOICES, REVIEW_RATING_CHOICES, LANGUAGE_CHOICES, LEVEL_CHOICES


class DeleteProfileForm(forms.Form):
    confirm = forms.BooleanField(
        label=_("Confirm deletion"),
        help_text=_(
            "Are you sure you want to delete your profile? This cannot be undone."
        ),
        required=True,
    )


class RegionForm(forms.ModelForm):
    class Meta:
        model = Region
        fields = ["name"]
        widgets = {
            "name": forms.CheckboxSelectMultiple,
        }


# Это предупреждение, а не ошибка. Оно связано с тем, что ваша форма TagForm наследуется от forms.ModelForm,
# который уже имеет базовый класс ModelForm и метакласс ModelFormMetaclass. Поэтому вы можете опустить указание метакласса
# в вашем коде. Попробуйте изменить первую строку на следующую:
# class TagForm(forms.ModelForm):


class Tag_helpForm(forms.ModelForm):
    class Meta:
        model = Tag_help
        fields = ["name"]
        labels = {"name": _("Name")}


class SupportLevelForm(forms.ModelForm):
    class Meta:
        model = SupportLevel
        fields = ["level"]
        widgets = {
            "level": forms.CheckboxSelectMultiple(),
        }


class HelpForm(forms.ModelForm):
    class Meta:
        model = HelpRequest
        fields = [
            "user_nick",
            "category",
            "problem_description",
            "district",
            "level",
            "language",
            "contacts",
        ]

        widgets = {
            "language": forms.CheckboxSelectMultiple(
                attrs={"class": "inline-checkbox"}
            ),
            "level": forms.RadioSelect(attrs={"class": "inline-radio"}),
            "category": forms.SelectMultiple(attrs={"size": 15}),
            "district": forms.SelectMultiple(attrs={"size": 9}),
        }

    user_nick = forms.CharField(label="User Nickname")
    category = forms.ModelChoiceField(
        queryset=Tag_help.objects.all(), label="Category", widget=forms.Select
    )
    problem_description = forms.CharField(label="Describe problem")
    district = forms.ModelChoiceField(
        queryset=Region.objects.all(), label="District", widget=forms.Select
    )
    level = forms.ModelChoiceField(
        queryset=Level.objects.all(), label="Level", widget=forms.RadioSelect
    )
    LANGUAGE_CHOICES = [(lang, lang) for lang in LANGUAGE_CHOICES]

    language = forms.MultipleChoiceField(
        choices=LANGUAGE_CHOICES,
        label="Language",
        widget=forms.CheckboxSelectMultiple,
    )
    contacts = forms.CharField(label="Contacts")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if "language" in self.fields:
            language_choices = dict(LANGUAGE_CHOICES)
            self.fields["language"].widget = forms.CheckboxSelectMultiple(
                attrs={"class": "inline-checkbox"}
            )
            self.fields["language"].choices = [
                (code, language_choices[code]) for code in language_choices
            ]


class HelperCreateForm(forms.ModelForm):
    user_type = forms.CharField(widget=forms.HiddenInput(), initial="helper")

    class Meta:
        model = Helper
        fields = (
            "name",
            "user_offer_is_free",
            "tags",
            "support_levels",
            "regions",
            "contacts",
            "languages",
            "email",
            "phone",
        )
        labels = {
            "user_offer_is_free": "Free offer",
            "name": "Name",
            "tags": "Tags",
            "support_levels": "Support levels",
            "regions": "Regions",
            "contacts": "Contacts",
            "languages": "Languages",
            "email": "Email",
            "phone": "Phone",
        }
        widgets = {
            "tags": forms.CheckboxSelectMultiple,
            "support_levels": forms.CheckboxSelectMultiple,
            "regions": forms.CheckboxSelectMultiple,
            "language": forms.CheckboxSelectMultiple(
                attrs={"class": "inline-checkbox"}
            ),
        }
        # Add the following line to define the soft_skills field
        soft_skills = forms.CharField(
            required=False, label="Soft skills", widget=forms.Textarea
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if "language" in self.fields:
            language_choices = dict(Language.LANGUAGE_CHOICES)
            self.fields["language"].widget = forms.CheckboxSelectMultiple(
                attrs={"class": "inline-checkbox"}
            )
            self.fields["language"].choices = [
                (code, language_choices[code]) for code in language_choices
            ]


class HelperUpdateForm(forms.ModelForm):
    class Meta:
        model = Helper
        fields = (
            "name",
            "user_offer_is_free",
            "tags",
            "support_levels",
            "regions",
            "contacts",
            "languages",
            "email",
            "soft_skills",
            "phone",
        )
        labels = {
            "user_offer_is_free": _("Free offer"),
            "name": _("Name"),
            "tags": _("Tags"),
            "support_levels": _("Support levels"),
            "regions": _("District"),
            "contacts": _("Contacts"),
            "languages": _("Languages"),
            "email": _("Email"),
            "soft_skills": _("soft_skills"),
            "phone": _("Phone"),
        }
        widgets = {
            "tags": forms.CheckboxSelectMultiple,
            "support_levels": forms.CheckboxSelectMultiple,
            "regions": forms.CheckboxSelectMultiple,
            "languages": forms.CheckboxSelectMultiple,
        }
from .models import UserRequest, Level

class UserRequestForm(forms.ModelForm):
    class Meta:
        model = UserRequest
        fields = [
            "selected_service",
            "comment",
            "district",
            "level_of_help",
            "languages",
            "contacts",
        ]
        widgets = {
            "comment": forms.Textarea(attrs={"rows": 5}),
            "contacts": forms.TextInput(attrs={"placeholder": "Enter your phone number"}),
        }

    selected_service = forms.ChoiceField(choices=TAG_HELP_NAME_CHOICES, widget=forms.RadioSelect())
    level_of_help = forms.ChoiceField(choices=LEVEL_CHOICES, initial="1")
    rating = forms.ChoiceField(choices=REVIEW_RATING_CHOICES, initial="1")
    languages = forms.ModelMultipleChoiceField(
        queryset=Language.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )
    contacts = forms.CharField(max_length=50)
class HelpRequestForm(forms.ModelForm):
    class Meta:
        model = HelpRequest
        fields = [
            "category",
            "problem_description",
            "district",
            "level",
            "language",
            "contacts",
            "languages",
        ]
        labels = {
            "category": _("Category"),
            "problem_description": _("Describe the problem"),
            "district": _("District"),
            "level": _("Level"),
            "language": _("Preferred language"),
            "contacts": _("Contacts"),
            "languages": _("Additional languages"),
        }
        widgets = {
            "problem_description": forms.Textarea(attrs={"rows": 5}),
            "contacts": forms.TextInput(attrs={"placeholder": "Enter your phone number"}),
            "languages": forms.CheckboxSelectMultiple(choices=LANGUAGE_CHOICES),
        }

    category = forms.ModelChoiceField(
        queryset=Tag_help.objects.all(),
        empty_label="Select category",
        widget=forms.Select(attrs={"class": "form-select"}),
    )
    district = forms.ModelChoiceField(
        queryset=Region.objects.all(),
        empty_label="Select district",
        widget=forms.Select(attrs={"class": "form-select"}),
    )
    level = forms.ChoiceField(
        choices=LEVEL_CHOICES,
        initial="1",
        widget=forms.Select(attrs={"class": "form-select"}),
    )
    language = forms.ModelChoiceField(
        queryset=Language.objects.all(),
        empty_label="Select language",
        widget=forms.Select(attrs={"class": "form-select"}),
    )
    languages = forms.ModelMultipleChoiceField(
        queryset=Language.objects.all(),
        widget=forms.CheckboxSelectMultiple(),
    )
