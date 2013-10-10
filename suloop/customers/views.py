from customers.models import *
from mongoengine import *
from django.utils import simplejson
from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from django.template.loader import render_to_string

connect('suloop')

