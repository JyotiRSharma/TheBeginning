from django.http import HttpResponse
from django.shortcuts import render
from .models import Album

def index(request):

    album_list = Album.objects.all()
    context = {'album_list': album_list}

    return render(request, 'music/index.html', context)

def details(request, album_id):
    return HttpResponse("This is for the album ID: " + str(album_id))
