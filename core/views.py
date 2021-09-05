from django.shortcuts import HttpResponse

# Create your views here.


def TaskView(request):
    return HttpResponse('It is working')