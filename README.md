# instagram
A clone of the website for the popular photo app [Instagram](https://www.instagram.com/)

## Getting Started

To get a copy of the project up and running on your local machine for development and testing purposes, 
1. **clone** this repository 
   ``` 
   git clone https://github.com/Amin1014/instagram.git
   ```
2. Create a **virtual environment** 
   ```
   python3.9 -m venv virtual

   source virtual/bin/activate
   ```
3. Install project **dependencies**
   ```sh
    (virtual) $ pip install -r requirements.txt
    ```
* See deployment for notes on how to deploy the project on a live system.



### Installing

1.  To get a development env running, use the **.env.example** file to create your own **.env** file.
2.  Create a **postgres** db and add the credentials to .env file
3.  Apply all migrations
```sh 
(virtual) $ python manage.py migrate 
```
4. Create admin account
```
(virtual) $ python manage.py createsuperuser
```
5. Make migrations to your database
```sh
(virtual) $ python manage.py makemigrations inst
(virtual) $ python manage.py migrate
```
6.  Start development server
```
 (virtual) $ python3 manage.py runserver
 ```

## Built With

* [Django 3.2](https://www.djangoproject.com/) - The web framework used
* [Heroku](https://www.heroku.com/platform) -  Deployment platform
* [Python3.9](https://www.python.org/) - Backend logic
* [Postresql](https://www.postgresql.org/) - Database system


## Authors

* [Mohamed Amin](https://github.com/Amin1014/instagram.git)


## License