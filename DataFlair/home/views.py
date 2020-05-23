from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'base.html')

def other(request):
    context = {
        'k1' : 'welcome to second page',
    }
    return render(request, 'others.html', context)

import datetime
def about(request):
    time = datetime.datetime.now()
    return render(request, 'about.html', {'time':time})

