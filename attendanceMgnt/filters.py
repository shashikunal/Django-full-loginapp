from django.contrib.auth.models import User

from attendanceMgnt .models import UserProfile
import django_filters

class UserFilter(django_filters.FilterSet):
    class Meta:
        model = UserProfile
        fields = ['date' , 'city']