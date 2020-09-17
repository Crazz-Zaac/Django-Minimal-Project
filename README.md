# Django-Minimal-Project
This is a minimal project covering almost all aspect of web development
using django restframework.

## Installing the essentials
First you'll need to create a virtual environment. Activate it and 
simply run
~~~
pip3 install -r requirements.txt
~~~

## Necessary step
You'll first need to delete files inside folder Migrations. This is necessary 
to rebuild model and populated it with your own data. Once it's done make migrations
and migrate.
```
python3 manage.py makemigrations
# after that
python3 manage.py migrate
```


## Running the project
Now before running the project, you can check if there are some errors and then run the 
localhost.
```
python3 manage.py check
python3 manage.py runserver
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

