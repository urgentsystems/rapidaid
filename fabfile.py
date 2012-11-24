from fabric.api import local
from fabric.context_managers import lcd

def send_heroku():

    #local('python manage.py test')
    local('git push heroku master')
    #local('heroku run python manage.py syncdb')
    #local('heroku run python manage.py migrate')



def getLibYAML():
    local('mkdir build')
    lcd('./build')
    local('curl -O http://pyyaml.org/download/libyaml/yaml-0.1.4.tar.gz')
    local('tar -xzf *.gz')
    lcd('./yaml-0.1.4')