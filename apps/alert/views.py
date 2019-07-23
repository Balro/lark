from django.views.decorators.http import require_POST
from django.http import HttpResponse

from .utills import sender


# Create your views here.

# @require_POST
def ding(request):
    sender.ding(request.POST.get("tos"), request.POST.get("content"))
    return HttpResponse("Alert received.")


@require_POST
def phone(request):
    # TODO
    return HttpResponse("Not supported yet.")


@require_POST
def mail(request):
    # TODO
    return HttpResponse("Not supported yet.")
