from django.shortcuts import render

# Create your views here.
def loukya(request):
    d={'name':'priya'}
    return render(request,'loukya.html',context=d)
