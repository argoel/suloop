from card.models import *
from mongoengine import *
from django.utils import simplejson
from django.http import HttpResponse
from tastypie_mongoengine import resources
from tastypie import authorization
from tastypie.resources import *

connect('suloop')

class CardResource(resources.MongoEngineResource):
	class Meta:
		queryset = Card.objects.all()
		print queryset
		resource_name = 'card'
		allowed_methods = ('get', 'post', 'put', 'delete', 'patch')
		# authorization = authorization.Authorization()

def get_cards(request):
	# get info about all cards this customer holds
	cardid = request.GET.get('cardid')
	if cardid is None:
		return HttpResponse(Cards.objects.all().to_json(), content_type="application/json")
	return HttpResponse(Cards.objects.filter(pk=custid).to_json(), content_type="application/json")