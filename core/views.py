from django.shortcuts import render

# Create your views here.
def home(request):
    ctx = {'n' : range(7) }
    return render(request, 'index.html', ctx)

def about(request):
    ctx = {}
    return render(request, 'about.html', ctx)

def contact(request):
    ctx = {}
    return render(request, 'contacts.html', ctx)