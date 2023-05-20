from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def srujana(request):
    return HttpResponse('<h1><marquee>vadilestunnava tinnavaa raa</marquee></h1>')