from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello world!")
def reje(request):
    return HttpResponse('tu bedzie reje')