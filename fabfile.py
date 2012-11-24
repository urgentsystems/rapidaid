from fabric.api import local
from fabric.api import lcd

def send_heroku():

    #local('python manage.py test')
    local('git push heroku master')
    #local('heroku run python manage.py syncdb')
    #local('heroku run python manage.py migrate')



def getLibYAML():
    local('mkdir build')
    with lcd('./build'):
        local('curl -O http://pyyaml.org/download/libyaml/yaml-0.1.4.tar.gz')
        local('tar -xzf *.gz')

def compileLibYAML():
        with lcd('./build/yaml-0.1.4'):
            local("./configure")
            local("make")
            local("sudo make install")



def InstallLibYAML():
    getLibYAML()
    compileLibYAML()
    local("rm -rf build/")
