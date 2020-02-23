# create a virtual environemt: run teh command in terminal after navigatinfg to the project folder
python -m venv ll_env

# activate the virtual environment on windows
ll_env\Scripts\activate


#To stop using a virtual environment, enter deactivate:
deactivate


# to run the server
python manage.py runserver

#modify models.py, run the command 
python manage.py makemigrations app_name
# and then run the command
python manage.py migrate



