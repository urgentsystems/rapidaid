from fabric.api import local

def send_heroku():

    local('python manage.py test urgentapp')
    local('git add -p && git commit')
    local('git push heroku master')
    local('heroku run python manage.py syncdb')
