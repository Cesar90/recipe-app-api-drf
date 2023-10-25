# recipe-app-api-drf

Recipe app api source code.

# Install packages

docker-compose build

# Create project from docker-compose

docker-compose run app sh -c "django-admin.py startproject app ."

# Run test and flake8

docker-compose run app sh -c "python manage.py test && flake8"

# Create core app

docker-compose run app sh -c "python manage.py startapp core"

# Run migrations just for core app

docker-compose run app sh -c "python manage.py makemigrations core"

# Create superuser

docker-compose run app sh -c "python manage.py createsuperuser"

# Create new app and remove container

docker-compose run --rm app sh -c "python manage.py startapp user"
