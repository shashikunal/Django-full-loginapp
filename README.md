# Django-full-loginapp
Its based on  django-registration Login App with Profile integration 


<strong>Installation</strong>

virtualenv justtest<br>
activate virualenv :<br>
source justtest/bin/activate<br>

<strong>After activate virtualenv install modules :<br></strong>

Download sourcecode form github https://github.com/shashikunal/Django-full-loginapp.git<br>
After just change directory to whatever downloaded from github.<br>

<strong>Then install these modules:<br></strong>

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

<strong>After Pip Installation</strong> 

<strong>config database:<br></strong>
databasename , database username , and database password in settings.py
 
<strong>after database settings </strong>

<strong>Config Mail configaration : <br /></strong>
gmail username and password in settings.py

migrate database in terminal:
python manage.py migrate

create admin user in shell:
python manage.py createsuperuser

finally run server
python manage.py runserver



