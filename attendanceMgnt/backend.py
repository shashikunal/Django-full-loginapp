from attendanceMgnt.models import CustomUser

class CustomUserAuth(obect):

	def authenticate(self , username=None , password=None):
		try:
			user = CustomUser.obejects.get(email=username)
			if user.check_password(password):
				return user
		except CustomUser.DoesNotExit:
			return None

	def get_user(self , user_id):
		try:
			user = CustomUser.obejects.get(pk=user_id)
			if user.is_active:
				return user
			return None
		except CustomUser.DoesNotExit:
			return None		
