from fabric.api import local

def prepare_deploy():
    local("./manage.py makemigrations --settings=settings.dev")
    local("./manage.py migrate --settings=settings.dev")
    local("./manage.py test apps.account --settings=settings.dev")
    #local("git add -p && git commit")
    local("git add .")
    local("git commit -am 'fab file introduced'")
    local("git push origin master")


