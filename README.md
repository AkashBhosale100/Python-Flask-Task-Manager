# Python-Flask-Task-Manager
 Simple Task Manager developed using Flask and Knockout JS
## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for link to view the deployed application.  
To run this application locally clone repository: https://github.com/AkashBhosale100/Python-Flask-Task-Manager.git  
Navigate to 'Python Rest Server' folder  
Open command prompt in this folder and run the following commands:
```
cd env/Scripts  
activate  
cd ../  
pip install -r requirements.txt  
flask run
```
This should start the python-flask server on localhost at port:5000  
Now navigate to 'Javascript client' folder  
Open another command prompt here and run the following command:  
```
python -m http.server  
```
This should start the client on localhost at port:8000  
Now to view the Task Manager application, open a browser and type the following in the address bar:
```
http://localhost:8000/  
```
and then click on 'tasks.html'  
The table should display all tasks present in the database
## Deployment 
Python-Flask server is currently deployed on PythonAnywhere (https://www.pythonanywhere.com/)  
Knockout JS client is currently deployed on 000Webhost (https://www.000webhost.com/)  

To see the deployed application navigate to https://bhosaleakash-tasks.000webhostapp.com/index.html

## Build With
-Python-Flask: A micro web framework written in Python  
-SQLALCHEMY:   Open source python SQL toolkit  
-Knockout JS:  A standalone JavaScript implementation of the Model-View-ViewModel pattern  
