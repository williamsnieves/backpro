from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Track
# Create your views here.

def track_view(request, title):

    track = get_object_or_404(Track, title=title)

    return render(request,"track.html",{'tracks': track})