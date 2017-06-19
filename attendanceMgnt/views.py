
from django.shortcuts import render ,redirect ,HttpResponse ,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from attendanceMgnt .forms import RegistrationForm , EditProfileForm , UserProfileForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm , PasswordChangeForm


from django.http import Http404
from attendanceMgnt.serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

import csv

from attendanceMgnt .models import UserProfile

from django.shortcuts import render
from attendanceMgnt .filters import UserFilter



from django.shortcuts import render


# Create your views here.
def home(request):
	return render(request , 'index.html')

# registration form

def register(request):
	if request.method =='POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/profile')
	else:
		form = RegistrationForm()
		args = {'form' : form}
		return render(request, 'accounts/register.html' , args)	




@login_required(login_url='/login')
def profile(request):
	args = {'user':request.user}
	return render(request , 'accounts/profile.html' , args)

@login_required(login_url='/login')
def addprofile(request):
	args = {'user':request.user}
	return render(request , 'accounts/addprofile.html' , args)	
@login_required(login_url='/login')
def edit_profile(request):
	if request.method == ('POST'):
		form = EditProfileForm(request.POST , instance=request.user)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/profile')
	else:
		form = EditProfileForm(instance=request.user)
		args = {'form' : form}	
		return render(request , 'accounts/editprofile.html' , args) 

# add profile		

@login_required(login_url='/login')
def user_profile(request):
	if request.method == 'POST':
		form = UserProfileForm(request.POST or None, request.FILES or None ,instance=request.user.userprofile)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/profile')
	else:
		user = request.user
		profile = user.userprofile
		form = UserProfileForm(instance=profile)
	args = {'form' :form}
	return render(request , 'accounts/addprofile.html' , args) 
	

# Change Password form
# @login_required(login_url='/login')
def password_change(request):
	if request.method == ('POST'):
		form = PasswordChangeForm(data=request.POST , user=request.user)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/profile')
	else:
		form = PasswordChangeForm(user=request.user)
		args = {'form' : form}	
		return render(request , 'accounts/change_password.html' , args) 


# Rest Framework View

# //User List

class UserList(APIView):
	def get(self, request, format=None):
		users = User.objects.all()
		serializer = UserSerializer(users, many=True)
		return Response(serializer.data)
	def post(self, request, format=None):
		serializer = UserSerializer(data=request.DATA)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
        	# return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	
	def delete(self, request, pk, format=None):
		user = self.get_object(pk)
		user.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

class UserDetail(APIView):
    """
    Retrieve, update or delete a user instance.
    """
    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        user = UserSerializer(user)
        return Response(user.data)

    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




# csv code

def export_users_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="users.csv"'

    writer = csv.writer(response)
    writer.writerow(['Website', 'city', 'description', 'image' , 'phone' , 'user'])

    users = Session.objects.all().values_list('Website', 'city', 'description', 'image' , 'phone' , 'user')
    for user in users:
        writer.writerow(user)

    return response





