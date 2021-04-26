from django.shortcuts import render,redirect

def listed(request):
    return render(request,'base/index.html')

