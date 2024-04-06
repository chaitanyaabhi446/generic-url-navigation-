from django.shortcuts import render

# Create your views here.
def state(request):
    return render(request,'static.html')