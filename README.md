# recipe-app-api-drf

Recipe app api source code.

# Create project from docker-compose

docker-compose run app sh -c "django-admin.py startproject app ."

# Run test and flake8

docker-compose run app sh -c "python manage.py test && flake8"
