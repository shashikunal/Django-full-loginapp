from django.conf.urls import url
from . import views
from django.contrib.auth.views import login , logout





urlpatterns = [
     url(r'^$', views.home),
     url(r'^login/$', login , {'template_name':'accounts/login.html'}),
     url(r'^logout/$', logout , {'template_name':'accounts/logout.html'}),
     url(r'^register/$', views.register , name='register'),
     url(r'^profile/$', views.profile , name='profile'),
     url(r'^profile/add$', views.user_profile , name='user_profile'),
     url(r'^profile/edit$', views.edit_profile , name='editprofile'),
     url(r'^password-change$', views.password_change , name='password_change'),
     url(r'^export/csv/$', views.export_users_csv, name='export_users_csv'),
     

    
]

