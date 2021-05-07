from django.http import HttpResponse
from .models import Album

def index(request):

    album_list = Album.objects.all()
    html = ''

    for album in album_list:
        url = '/music/' + str(album.id)
        html += '<a href="'+ url +'">' + album.album_name + '</a></br>'
    return HttpResponse(html)

def details(request, album_id):
    return HttpResponse("This is for the album ID: " + str(album_id))