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

	name = StringField(required=True)
	costofgood = FloatField(required=True)
	numeraire = FloatField(required=True)
	time_created = DateTimeField(default=datetime.datetime.now)
	time_updated = DateTimeField(default=datetime.datetime.now)