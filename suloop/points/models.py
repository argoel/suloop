from mongoengine import *
from djangotoolbox.fields import ListField, EmbeddedModelField
import datetime
from customers.models import *
from stores.models import *

class Point(Document):
	'''
	Point class, keeps track of points of customer and store()
	'''
	def __unicode__(self):
		return self.customer + " : " + self.store
		
	customer = ReferenceField(Customer)
	store = ReferenceField(Store)
	value = FloatField(default=0.0)
	time_created = DateTimeField(default=datetime.datetime.now)
	time_updated = DateTimeField(default=datetime.datetime.now)