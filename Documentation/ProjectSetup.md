# Project Setup

## factorio-benchmark-frontend

* **Tech stack**: **React** project, using **React Bootstrap**
* **Editor**: **VS Code**
    * To open the project: right-click *factorio-benchmark-frontend* folder -> Open with Code.
    * No VS Code extensions needed.
* **How to run**:
    * Install the dependencies with `npm install`
    * Run `npm start` to start a local server
    * To debug React components you can use the **React DevTools** browser extension

## factorio_benchmark_backend

* **Tech stack**: [Django](https://www.djangoproject.com/) and [PostgreSQL](https://www.postgresql.org/)
* **Recommended IDE**: [VSCodium](https://vscodium.com/)
* **Dependencies**: [python](https://www.python.org/) (recommended version **>=3.12**)
* **How to run**:
    * create a virtual environment with [venv](https://docs.python.org/3/tutorial/venv.html) and activate it
    * `pip install django`
    * `pip install django-environ`
    * `pip install psycopg2`
    * **Setting up the environment variables**
        * create a .env file inside [/factorio_benchmark_backend/factorio_benchmark_backend](/factorio_benchmark_backend/factorio_benchmark_backend)
        * set the environment variables `SECRET_KEY` (use `print(get_random_secret_key())` to get a new random key), `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `DB_HOST` (usually **localhost**) and `DB_PORT` (usually **5432**)
    * make sure `DB_HOST:DB_PORT` is reachable (for the configuration of the server it is recommended you use [pgAdmin](https://www.pgadmin.org/))
    * make sure `DB_NAME` is a database that exists on the server
    * on the server `DB_HOST` create a user `DB_USER` (its password must be `DB_PASSWORD`) with all grants to the **public** schema of the database `DB_NAME`
    * `cd factorio_benchmark_backend` (this assumes you are in the root dir of the project beforehand)
    * `python manage.py makemigrations`
    * `python manage.py migrate`
    * `python manage.py runserver`