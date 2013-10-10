from customers.models import *
from mongoengine import *
from django.utils import simplejson
from django.http import HttpResponse
from tastypie import authorization
from tastypie_mongoengine import resources
from tastypie.resources import *

connect('suloop')

class CustomerResource(resources.MongoEngineResource):
	class Meta:
		queryset = Customer.objects.all()
		print queryset
		resource_name = 'customer'
		allowed_methods = ('get', 'post', 'put', 'delete', 'patch')
		# authorization = authorization.Authorization()

def get_customers(request):
	# get information about requested customer
	custid = request.GET.get()
	print custid
	if custid is None:
		return HttpResponse(Customer.objects.all().to_json(), content_type="application/json")
	return HttpResponse(Customer.objects.filter(pk=custid).to_json(), content_type="application/json")

