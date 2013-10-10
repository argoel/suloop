from customers.models import *
from mongoengine import *
from django.utils import simplejson
from django.http import HttpResponse
from tastypie import authorization
from tastypie.resources import *
from suloop.models import BackBoneCompatibleResource
import copy

connect('suloop')

class CustomerResource(BackBoneCompatibleResource):
	class Meta:
		queryset = Customer.objects.all()
		# print queryset
		resource_name = 'customer'
		allowed_methods = ('get', 'post', 'put', 'delete', 'patch', 'options')
		authorization = authorization.Authorization()