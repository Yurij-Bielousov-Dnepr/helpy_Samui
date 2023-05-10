from django.middleware.csrf import CsrfViewMiddleware
from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


from django.middleware.csrf import CsrfViewMiddleware
from django.template.context_processors import csrf
from django.http import HttpResponseForbidden

class CustomCsrfViewMiddleware(CsrfViewMiddleware):
    def process_response(self, request, response):
        reason_phrase = getattr(response, 'reason_phrase', '')
        if response.status_code == 403 and reason_phrase == 'Forbidden' and not request.is_ajax():
            context = {'request': request}
            context.update(csrf(request))
            return render(request, 'accounts/csrf_failure.html', context=context, status=403)

        return response


class CustomPermissionDeniedMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    @method_decorator(csrf_exempt, name='__call__')
    def __call__(self, request):
        response = self.get_response(request)

        if isinstance(response, PermissionDenied):
            response.content = 'Custom 403 error message'

        return response
