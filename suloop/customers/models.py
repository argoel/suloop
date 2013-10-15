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
		return self.firstname + " " + self.lastname

	email = EmailField(required=True)
	firstname = StringField(max_length=50)
	lastname = StringField(max_length=50)
	time_created = DateTimeField(default=datetime.datetime.now)
	time_updated = DateTimeField(default=datetime.datetime.now)