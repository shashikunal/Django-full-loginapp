from django.contrib import admin
from attendanceMgnt.models import UserProfile

# Register your models here.
class UserProfileAdmin(admin.ModelAdmin):
	list_display = ('user', 'user_info' , 'city' , 'phone' ,'Website')
	def user_info(self , obj):
		return obj.description

admin.site.register(UserProfile , UserProfileAdmin)
admin.site.site_header = 'Qspiders Attendance App Admin'
