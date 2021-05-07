from django.http import HttpResponse
from django.template import loader
from .models import Album

def index(request):

    album_list = Album.objects.all()
    template = loader.get_template('music/index.html')

    context = {
        'album_list': album_list,
    }

    return HttpResponse(template.render(context, request))

def details(request, album_id):
    return HttpResponse("This is for the album ID: " + str(album_id))
