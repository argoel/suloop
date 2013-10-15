from stores.models import *
from mongoengine import *
from django.utils import simplejson
from django.http import HttpResponse
from tastypie import authorization
from tastypie.resources import *
from suloop.models import BackBoneCompatibleResource
from tastypie_mongoengine import fields

connect('suloop')

class StoreResource(BackBoneCompatibleResource):
	class Meta:
		queryset = Store.objects.all()
		# print queryset
		resource_name = 'store'
		excludes = ['resource_uri', 'time_created', 'time_updated']
		allowed_methods = ('get', 'post', 'put', 'delete', 'patch', 'options')
		detail_allowed_method = ['patch']
		authorization = authorization.Authorization()

class StoreNetworkResource(BackBoneCompatibleResource):
	store1 = fields.ReferenceField(to="stores.api.StoreResource", attribute="store1", full=True)
	store2 = fields.ReferenceField(to="stores.api.StoreResource", attribute="store2", full=True)
	class Meta:
		queryset = StoreNetwork.objects.all()
		# print queryset
		resource_name = 'storenetwork'
		excludes = ['resource_uri', 'time_created', 'time_updated']
		allowed_methods = ('get', 'post', 'put', 'delete', 'patch', 'options')
		detail_allowed_method = ['patch']
		authorization = authorization.Authorization()