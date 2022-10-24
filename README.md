# MotoDodo  
  
## Description:  
MotoDodo is a web application allowing motorcyclists to find suitable accommodation for themselves and their motorcycles.  
MotoDodo is available at : https://www.motododo.azurewebapp.fr
  
### Install PostgreSQL and configure a database


### Create the virtual environment and install the devDependencies 
```sh
$ pip intall pipenv  
$ pipenv shell  
$ pipenv install
```
  
### Initialize project  
Position yourself in the openrider folder  
Then initialize db:  

```sh
$ ./manage.py makemigrations  
$ ./manage.py migrate
$ ./manage.py initdb
```  
  
Your can now create a superuser by typing:  

```sh
$ ./manage.py createsuperuser
``` 

Finally, launch with : 
  
```sh
$ ./manage.py runserver
``` 
  
### Tests  
  
In the **motododo folder**, you can launch test typing:  
```sh
$ coverage run --source='.' manage.py test
``` 
  
To view the test report :
```sh
$ coverage report
``` 
