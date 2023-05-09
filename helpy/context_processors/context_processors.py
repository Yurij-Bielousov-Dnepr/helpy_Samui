# context_processors.py
from django.shortcuts import render
from django.urls import reverse
from accounts.models import Sponsor
import traceback
from .get_languages_with_flags import get_languages_with_flags
from django.conf import settings
from django.templatetags.static import static

# def footer_context(request):
#     sponsors = Sponsor.objects.all()
#     return {'sponsors': sponsors}
#
# def menu_items(request):
#     items = [
#         {'title': 'Helpy', 'url': reverse('index')},
#         {'title': 'Offer help', 'url': reverse('offer_help')},
#         {'title': 'Articles', 'url': reverse('articles')},
#         {'title': 'Events', 'url': reverse('events')},
#         {'title': 'About', 'url': reverse('about')},
#     ]
#
#     return {'menu_items': items}
#


def languages_with_flags(request):
    languages = get_languages_with_flags(settings.LANGUAGES)
    languages_with_flags = []
    for language in languages:
        language_with_flag = {
            'code': language['code'],
            'name': language['name'],
            'flag': static(f'flags/{language["flag"]}.svg'),
        }
        languages_with_flags.append(language_with_flag)
    return {'languages_with_flags': languages_with_flags}

def footer_context(request):
    try:
        sponsors = Sponsor.objects.all()
        return {'sponsors': sponsors}
    except Exception as e:
        print(f"Error in footer_context: {e}")
        print(traceback.format_exc())
        return {}

def my_view(request):
    current_view_name = 'home'
    menu_items = [
        {'title': 'Helpy', 'url': reverse('index')},
        {'title': 'Offer help', 'url': reverse('offer_help')},
        {'title': 'Articles', 'url': reverse('articles')},
        {'title': 'Events', 'url': reverse('events')},
        {'title': 'About', 'url': reverse('about')},
    ]
    if request.user.is_authenticated:
        menu_items.append( {'label': 'Favorites', 'url': reverse( 'favorites' )} )
        return render( request, 'header.html', {'menu_items': menu_items, 'current_view_name': current_view_name} )
    else:
        return render( request, 'header.html', {'menu_items': menu_items, 'current_view_name': current_view_name} )