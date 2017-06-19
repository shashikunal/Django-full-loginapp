from django.db import models
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.db.models.signals import pre_save
from django.db.models.signals import post_save
from django.dispatch import receiver
import requests
import json
from datetime import date
import datetime
from django.utils.translation import gettext as _


# Create your models here.

class UserProfile(models.Model):
	user = models.OneToOneField(User , related_name='userprofile' , on_delete=models.CASCADE , primary_key=True)
	description = models.CharField(max_length=100, default='')
	city = models.CharField(max_length=100 , default='')
	phone = models.IntegerField(default=0)
	Website = models.URLField(default='')
	uid = models.CharField(max_length=10 , default='')
	# image = models.ImageField(upload_to='profile_image' , null=True , blank=True ,default='/profile_image/user.png')
	image = models.FileField(null=True , blank=True , default='/profile_image/user.png')
	date = models.DateField(_("Date"), default=datetime.date.today)

	def __str__(self):
		return self.user.username

def create_profile(sender , **kwargs):
	if kwargs['created']:
		user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile , sender=User)
# User.profile = property(lambda u:UserProfile.objects.get_or_create(user=u)[0])



# // end of profile

@receiver(post_save, sender=User)
def reg_user_raspberry(sender, instance, created, **kwargs):
	if created:
		url = "http://192.168.0.18:8080/users/"
		token = "8f720b8004b0a686f2bbe41cb32944851d9710e7"
		data = { 'username': instance.username, 'password': instance.username, 'email': instance.email,}
		response = requests.post(url, data=data, headers={'Authorization': 'Token {}'.format(token)})
		content = response.content
		if instance.id > 0:
			raw_data = content.decode('utf-8')
			python_obj=json.loads(raw_data)
			print(python_obj["id"])
			prof = User.objects.get(id=instance.id)
			prof.userprofile.uid = python_obj["id"]
			prof.userprofile.save(update_fields=['uid'])
