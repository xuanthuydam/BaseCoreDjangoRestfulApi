# BaseCoreDjangoRestfulApi

# Authorization for sh file and config hooks git
chmod +x hooks/pre-push
git config core.hooksPath hooks

# init project
django-admin startproject core_app

# create new app
python manage.py startapp app_name

# migrate db
python manage.py migrate

# create init supper user
python manage.py createsuperuser

# create file gitinore
touch .gitignore

# requiment
pip install -r requirements.txt
pip freeze > requirements.txt

# check code before commit
ruff check

# format commit message 
<type>(<scope>): <short description>

Type        | Use
------------|-----------------------------------------------------
feat        | New feature
fix         | Fix bug
docs        | Change documentation
style       | Format, lint, no logic change
refactor    | Update code, no behavior change
test        | Add/update tests
chore       | Config, cleanup, gitignore...
