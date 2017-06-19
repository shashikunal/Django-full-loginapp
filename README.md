# Django-full-loginapp
Its based on  django-registration Login App with Profile integration 


Installation

create virtualenv: 
virtualenv justtest

activate virualenv :
source justtest/bin/activate
after activate virtualenv install modules :

Download sourcecode form github https://github.com/shashikunal/Django-full-loginapp.git
After just change directory to whatever downloaded from github.

Then install these modules:

pip install django<br>
pip install django-bootstrap-form
pip install django-registration
pip install django-cors-headers
pip install djangorestframework
pip install django-filter
pip install MySQL-python
pip install requests
pip install json
pip install receiver
pip install send_mail
pip install datetime

After Pip Installation 

config database:
databasename , database username , and database password in settings.py
 
after database settings 

Config Mail configaration : 
gmail username and password in settings.py

migrate database in terminal:
python manage.py migrate

create admin user in shell:
python manage.py createsuperuser

finally run server
python manage.py runserver



