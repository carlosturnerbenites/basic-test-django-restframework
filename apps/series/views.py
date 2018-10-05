from .models import Genre, Serie
from rest_framework import viewsets
from .serializers import GenreSerializer, SerieSerializer
from django.http import HttpResponse

class GenreViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Genre.objects.all() #.order_by('-date_joined')
    serializer_class = GenreSerializer


class SerieViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Serie.objects.all()
    serializer_class = SerieSerializer

from zeep import Client
def soap_request (request):
    client = Client('http://localhost:8080/servicio2/calculadora?WSDL')
    print(client)
    result = client.service.suma(3,4)
    # return render(request, 'blog/post_list.html', {})
    return HttpResponse(result)

