# Django-full-loginapp
Its based on  django-registration Login App with Profile integration 


Installation

create virtualenv:<br> 
virtualenv justtest

activate virualenv :<br>
source justtest/bin/activate<br>
after activate virtualenv install modules :

Download sourcecode form github https://github.com/shashikunal/Django-full-loginapp.git
After just change directory to whatever downloaded from github.

Then install these modules:

pip install django<br>
pip install django-bootstrap-form<br>
pip install django-registration<br>
pip install django-cors-headers<br>
pip install djangorestframework<br>
pip install django-filter<br>
pip install MySQL-python<br>
pip install requests<br>
pip install json<br>
pip install receiver<br>
pip install send_mail<br>
pip install datetime<br>

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



