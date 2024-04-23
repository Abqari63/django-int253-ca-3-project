# Django Project Setup Guide

This guide will walk you through the steps required to set up and run a Django project that utilizes PostgreSQL as the database.

## Prerequisites

Before you begin, ensure you have the following installed on your system:

- Python (3.x recommended)
- PostgreSQL
- pip (Python package installer)

## Setup

1. Clone the repository:
    ```
    git clone https://github.com/Abqari63/django-int253-ca-3-project
    cd django-int253-ca-3-project
    ```

2. Create a PostgreSQL database from the psql shell:
    ```
    sudo -u postgres psql
    CREATE DATABASE <database_name>;
    CREATE USER <username> WITH PASSWORD '<password>';
    ALTER ROLE <username> SET client_encoding TO 'utf8';
    ALTER ROLE <username> SET default_transaction_isolation TO 'read committed';
    ALTER ROLE <username> SET timezone TO 'UTC';
    GRANT ALL PRIVILEGES ON DATABASE <database_name> TO <username>;
    \q
    ```

3. Configure Django settings:
    - Open `settings.py` of the cloned directory.
    - Update the database settings with your PostgreSQL credentials:
        ```python
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.postgresql',
                'NAME': '<database_name>',
                'USER': '<username>',
                'PASSWORD': '<password>',
                'HOST': 'localhost',
                'PORT': '5432',
            }
        }
        ```

4. Run migrations:
    ```
    python manage.py migrate
    ```

## Running the Server

    ```
    python manage.py migrate
    ```
You can now run the Django development server:

The server will start running locally at `http://127.0.0.1:8000/`.

