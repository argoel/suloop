from points.models import *
from mongoengine import *
from django.utils import simplejson
from django.http import HttpResponse

connect('suloop')