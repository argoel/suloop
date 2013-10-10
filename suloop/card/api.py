from card.models import *
from mongoengine import *
from django.utils import simplejson
from django.http import HttpResponse
from tastypie import authorization
from tastypie.resources import *
from suloop.models import BackBoneCompatibleResource

connect('suloop')

class CardResource(BackBoneCompatibleResource):
	class Meta:
		queryset = Card.objects.all()
		# print queryset
		resource_name = 'card'
		allowed_methods = ('get', 'post', 'put', 'delete', 'patch', 'options')
		authorization = authorization.Authorization()