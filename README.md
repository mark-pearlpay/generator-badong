# Badong - The PearlPay Backend API Code Generator

> Yeoman generator for creating PearlPay backend code using python, django and mysql. Lets you quickly set up a project following best practices.

## Usage

Install `yo`, and `generator-badong`:

```ssh
$ npm install -g yo generator-badong
```

**TODO**: Add how to run

## Generators

Available generators:

* App
  * badong
    ```bash
    Usage:
        $ yo badong
        ? Project name: new_app_name
        ? Are you sure you want to create new project? (Y/n) y
    ```
    ```bash
    Produces:
        new_app_name/app/__init__.py
        new_app_name/app/manage.py
        new_app_name/app/requirements.txt
        new_app_name/app/new_app_name/__init__.py
        new_app_name/app/new_app_name/asgi.py
        new_app_name/app/new_app_name/settings.py
        new_app_name/app/new_app_name/urls.py
        new_app_name/app/new_app_name/wsgi.py
        new_app_name/app/application/__init__.py
        new_app_name/app/domain/__init__.py
        new_app_name/app/infrastructure/__init__.py
        new_app_name/app/infrastructure/admin.py
        new_app_name/app/infrastructure/apps.py
        new_app_name/app/infrastructure/models.py
        new_app_name/app/infrastructure/tests.py
        new_app_name/app/infrastructure/views.py
        new_app_name/app/infrastructure/migrations/__init__.py
        new_app_name/docker-compose.yml
        new_app_name/Dockerfile
        new_app_name/README.md
        new_app_name/tests/pytest.ini
        new_app_name/tests/requirements.txt
        new_app_name/tests/test_settings.py
    ```
