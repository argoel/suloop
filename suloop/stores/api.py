from stores.models import *
from mongoengine import *
from django.utils import simplejson
from django.http import HttpResponse
from tastypie import authorization
from tastypie_mongoengine import resources
from tastypie.resources import *

connect('suloop')

class StoreResource(resources.MongoEngineResource):
	class Meta:
		queryset = Store.objects.all()
		print queryset
		resource_name = 'store'
		allowed_methods = ('get', 'post', 'put', 'delete', 'patch')
		# authorization = authorization.Authorization()

def get_stores(request):
	# get info of requested store
	storeid = request.GET.get('storeid')
	if storeid is None:
		return HttpResponse(Store.objects.all().to_json(), content_type="application/json")
	return HttpResponse(Store.objects.filter(pk=storeid).to_json(), content_type="application/json")
