from django.views.decorators.http import require_GET
from django.http import HttpResponse


@require_GET
def status(request):
    return HttpResponse("ok")
