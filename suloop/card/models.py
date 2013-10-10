from mongoengine import *
from djangotoolbox.fields import ListField, EmbeddedModelField
import datetime
from customers.models import *
from stores.models import *

class Card(Document):
	'''
	Card class, each card is associated to a unique customer (pk)
	Each customer could have multiple cards (Original Loyalty System)
	Each card could be associated with 1 or more Stores (ListField)
	'''
	def __unicode__(self):
		return self.customer.name
		
	customer = ReferenceField(Customer, primary_key=True)
	stores = ListField(Store)
	time_created = DateTimeField(default=datetime.datetime.now)
	time_updated = DateTimeField(default=datetime.datetime.now)