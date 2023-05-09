import traceback
from accounts.models import Sponsor


def footer_context(request):
    try:
        sponsors = Sponsor.objects.all()
        return {'sponsors': sponsors}
    except Exception as e:
        print(f"Error in footer_context: {e}")
        print(traceback.format_exc())
        return {}