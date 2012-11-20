from fabric.api import local

def send_heroku():

    #local('python manage.py test')
    local('git push heroku master')
    #local('heroku run python manage.py syncdb')
    #local('heroku run python manage.py migrate')
