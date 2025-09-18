from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home.html')
    # return HttpResponse('this is homepage')

def subject(request):
    return render(request, 'chapters.html')

def chapter(request):
    return render(request, 'lessions.html')