from mongoengine import *
from djangotoolbox.fields import ListField, EmbeddedModelField
import datetime

class Store(Document):
	'''
	Generic Class to Replicate Shopping Stores
	Assuming single good sold in each store at fixed price
	'''
	def __unicode__(self):
		return self.name

	name = StringField()
	costofgood = FloatField()
	numeraire = FloatField()
	time_created = DateTimeField(default=datetime.datetime.now)
	time_updated = DateTimeField(default=datetime.datetime.now)

class StoreNetwork(Document):
	'''
	Generic class to implement Network of Stores
	Each directed edge has a credit capacity and
	and exchange rate. This exchange rate in current
	scenario is just ratio of numeraires of the two
	stores
	'''
	store1 = ReferenceField(Store)
	store2 = ReferenceField(Store)
	credit = FloatField()
	exrate = FloatField()
	time_created = DateTimeField(default=datetime.datetime.now)
	time_updated = DateTimeField(default=datetime.datetime.now)
