# from django.utils.translation import ugettext_lazy as _ ugettext_lazy

def _(text):
    return text

TAG_ARTICLE_MOTO_RENT = 'moto_rent'
TAG_ARTICLE_MOTO_BEGINNER = 'moto_beginner'
TAG_ARTICLE_MOTO_SOS = 'moto_sos'
TAG_ARTICLE_RENT_ESTATE = 'rent_estate'
TAG_ARTICLE_PUBLIC_SERV = 'public_serv'
TAG_ARTICLE_LANG_SCHOL = 'lang_schol'
TAG_ARTICLE_MED_HELP = 'med_help'
TAG_ARTICLE_SERV_TRANSL = 'serv_transl'
TAG_ARTICLE_SHOPPING_DESTINATION = 'shopping_destination'
TAG_ARTICLE_SOUVENIRS = 'souvenirs'

TAG_ARTICLE_CHOICES = (
    (TAG_ARTICLE_MOTO_RENT, _("Moto Rent")),
    (TAG_ARTICLE_MOTO_BEGINNER, _("Moto Beginner")),
    (TAG_ARTICLE_MOTO_SOS, _("Moto SOS")),
    (TAG_ARTICLE_RENT_ESTATE, _("Rent Estate")),
    (TAG_ARTICLE_PUBLIC_SERV, _("Public Service")),
    (TAG_ARTICLE_LANG_SCHOL, _("Language School")),
    (TAG_ARTICLE_MED_HELP, _("Medical Help")),
    (TAG_ARTICLE_SERV_TRANSL, _("Translation Services")),
    (TAG_ARTICLE_SHOPPING_DESTINATION, _("Shopping Destination")),
    (TAG_ARTICLE_SOUVENIRS, _("Souvenirs")),
)

REVIEW_RATING_1_STAR = 1
REVIEW_RATING_2_STARS = 2
REVIEW_RATING_3_STARS = 3
REVIEW_RATING_4_STARS = 4
REVIEW_RATING_5_STARS = 5

REVIEW_RATING_CHOICES = (
    (REVIEW_RATING_1_STAR, _('1 star')),
    (REVIEW_RATING_2_STARS, _('2 stars')),
    (REVIEW_RATING_3_STARS, _('3 stars')),
    (REVIEW_RATING_4_STARS, _('4 stars')),
    (REVIEW_RATING_5_STARS, _('5 stars')),
)

TAG_HELP_MOTO_RENT = 'moto_rent'
TAG_HELP_MOTO_BEGINNER = 'moto_beginner'
TAG_HELP_MOTO_SOS = 'moto_sos'
TAG_HELP_RENT_ESTATE = 'rent_estate'
TAG_HELP_PUBLIC_SERV = 'public_serv'
TAG_HELP_LANG_SCHOL = 'lang_schol'
TAG_HELP_TRABL = 'trabl'
TAG_HELP_MED_HELP = 'med_help'
TAG_HELP_SERV_TRANSL = 'serv_transl'
TAG_HELP_SHOPPING_DESTINATION = 'shopping_destination'
TAG_HELP_CLOTHING = 'clothing'
TAG_HELP_FOOD = 'food'
TAG_HELP_SOUVENIRS = 'souvenirs'
TAG_HELP_IND_TOUR = 'ind_tour'
TAG_HELP_ESCORT = 'escort'

TAG_HELP_NAME_CHOICES = (
    (TAG_HELP_MOTO_RENT, _("Moto Rent")),
    (TAG_HELP_MOTO_BEGINNER, _("Moto Beginner")),
    (TAG_HELP_MOTO_SOS, _("Moto SOS")),
    (TAG_HELP_RENT_ESTATE, _("Rent Estate")),
    (TAG_HELP_PUBLIC_SERV, _("Public Service")),
    (TAG_HELP_LANG_SCHOL, _("Language School")),
    (TAG_HELP_TRABL, _("Travel")),
    (TAG_HELP_MED_HELP, _("Medical Help")),
    (TAG_HELP_SERV_TRANSL, _("Translation Services")),
    (TAG_HELP_SHOPPING_DESTINATION, _("Shopping Destination")),
    (TAG_HELP_CLOTHING, _("Clothing")),
    (TAG_HELP_FOOD, _("Food")),
    (TAG_HELP_SOUVENIRS, _("Souvenirs")),
    (TAG_HELP_IND_TOUR, _("Individual Tour")),
    (TAG_HELP_ESCORT, _("Escort")),
)
REGION_CHOICES = [("", "Choose all"), ("Chaweng", "Chaweng"), ("Lamai", "Lamai"), ("Lipa Noi", "Lipa Noi"),
                  ("Nathon", "Nathon"), ("Bang Bor", "Bang Bor"), ("Maenam", "Maenam"), ("Bophut", "Bophut"),
                  ("Choeng Mon", "Choeng Mon"), ("Hua Thanon", "Hua Thanon"), ]

LANGUAGE_CHOICES = [("uk", "Українська"), ("th", "ไทย"), ("en", "English"), ("fr", "Français"), ("it", "Italiano"),
                    ("de", "Deutsch"), ("ru", "Русский"), ]

LEVEL_CHOICES = [(1, "Level 1"), (2, "Level 2"), (3, "Level 3"), ]

# TAG_HELP_CHOICES = [("moto_rent", "Moto Rent"), ("moto_beginner", "Moto Beginner"), ("moto_sos", "Moto SOS"),
#                     ("rent_estate", "Rent Estate"), ("public_serv", "Public Service"),
#                     ("lang_schol", "Language School"), ("trabl", "Travel"), ("med_help", "Medical Help"),
#                     ("serv_transl", "Translation Services"), ("shopping_destination", "Shopping Destination"),
#                     ("clothing", "Clothing"), ("food", "Food"), ("souvenirs", "Souvenirs"),
#                     ("ind_tour", "Individual Tour"), ("escort", "Escort"), ]
