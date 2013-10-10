from mongoengine import *
from djangotoolbox.fields import ListField, EmbeddedModelField
import datetime

class Customer(Document):
	'''
	Generic customer class to store information
	Each customer carries 1 or more store cards
	In class card (/cards) this is provided as
	reference
	'''
	def __unicode__(self):
		return self.first_name + " " + self.last_name

	email = EmailField(required=True)
	first_name = StringField(required=True, max_length=50)
	last_name = StringField(required=True, max_length=50)
	time_created = DateTimeField(default=datetime.datetime.now)
	time_updated = DateTimeField(default=datetime.datetime.now)