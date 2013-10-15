from points.models import *
from mongoengine import *
from django.utils import simplejson
from django.http import HttpResponse
from tastypie import authorization
from tastypie.resources import *
from suloop.models import BackBoneCompatibleResource
from customers.models import *
from stores.models import *
from tastypie_mongoengine import fields

connect('suloop')

class PointResource(BackBoneCompatibleResource):
	customer = fields.ReferenceField(to="customers.api.CustomerResource", attribute="customer", full=True)
	store = fields.ReferenceField(to="stores.api.StoreResource", attribute="store", full=True)
	class Meta:
		queryset = Point.objects.all()
		# print queryset
		resource_name = 'point'
		excludes = ['resource_uri', 'time_created', 'time_updated']
		allowed_methods = ('get', 'post', 'put', 'delete', 'patch', 'options')
		authorization = authorization.Authorization()