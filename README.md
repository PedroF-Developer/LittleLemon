# LittleLemon
Project for the Meta's Back-End Developer Capstone course using Django. This project is an implementation of both a website and an API for the Little Lemon restaurant along with some API points to help manage the restaurant's menu and booking appointments.
## Installation
**Clone this repository**
```bash
git clone https://github.com/PedroF-Developer/LittleLemon.git && cd littlelemon
```
**Create a virtual environment and install the dependencies**  
This project uses "pipenv" for the virtual environment and to manage and install the dependencies, if you don't got "pipenv" installed you can install it by using:
```bash
pip install --user pipenv
```
And then to install the project dependencies:
```bash
pipenv install
```  
## Setting up the Database
This project uses the MySQL Database with the follow configuration:
```python
DATABASES = {
    'default': {  
        'ENGINE': 'django.db.backends.mysql',
        # Change the NAME, USER and PASSWORD values to your local MySQL database  
        'NAME': 'LittleLemon',  
        'USER': 'root',  
        'PASSWORD': 'password',  
        'HOST': '127.0.0.1',  
        'PORT': '3306',  
        'OPTIONS': {  
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",  
        }  
    }
}
```
You must replace 'NAME, 'USER' and 'PASSWORD' to those configured in your local MySQL database.  
If you don't got a database setted up, you can setup one by using:
```bash
mysql -u root -p
```  
You will be prompted to input the "root" password, after that you'll be in the "mysql" shell which you can then run:
```sql
CREATE DATABASE <DATABASE_NAME>;
```  
After that you can then choose between using the "root" user to manage the database (which is not recommended), or create a new user by using:
```sql
CREATE USER <USER_NAME> IDENTIFIED BY <PASSWORD>;
```
And then setting up the new user's privilegies:
```sql
GRANT ALL ON *.* TO <USER_NAME>;
```
Don't forget to also refresh the priveligies with:
```sql
flush privileges;
```
And then exit the mysql shell with
```sql
exit;
```
Done! Now all you gotta do is replace the values of "NAME", "USER" and "PASSWORD" with their respective values!
## Running the Application
After all the dependencies have been installed and the database is set up and running, perform the necessary migrations with:
```bash
python manage.py migrate
```
And then run the server with:
```bash
python manage.py runserver
```
Additionally, you can run the unit tests included in this project with
```bash
python manage.py test
```
## API Endpoints
This project comes with a basic static html page along with some API endpoints which can be accessed on the localhost url: http://127.0.0.1:8000/  
Here's a table containing all the endpoints and what they do:
| Page Path | Type | Description | Requires Authentication | Allowed Methods |
| -------- | ---- | ----------- | ----------------------- | - |
| /restaurant/ | HTML | Static page "index.html" of the restaurant | No |
| /restaurant/booking/tables/ | API | API Endpoint responsible to list and manage the booking appointments | Yes | GET, POST
| /restaurant/menu/ | API | API Endpoint responsible to list and manage the menu items | Yes | GET, POST
| /restaurant/menu/<menu_item_id>/ | API | API Endpoint responsible to display and manage a single menu item | Yes | GET, PUT, PATCH, DELETE
| /auth/users/ | API | API Endpoint responsible to list, manage and register users | Partial (No need authentication to register new users) | GET, POST
| /auth/token/login/ | API | API Endpoint responsible to generate a login token for an user. Requires username and password | No | POST
| /auth/token/logout/ | API | API Endpoint responsible to logout the current logged in user. It will delete the user's token if it has one | Yes | POST
| /restaurant/api-token-auth/ | API | Alternative API Endpoint to generate a login token for an user. Requires username and password | No | POST
| /restaurant/message/ | API | Test API Endpoint to check if user is authenticated | Yes | GET
