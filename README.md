# TaskManager Backend

A backend app for support Task management of multiple users and their requirements as a hiring test. This proof of concept includes:

* JWT authentication mechanism.
* CRUD endpoints for Task operations.
* Documentation (<http://127.0.0.1:8000/docs/>)
* Coverage 89%
* [OPTIONAL] serverless deployment in AWS Lambda with Zappa.


## Considerations

1. In instructions, there is no guaranteed way to identify Students in a unique form (like a national DNI, local id etc.), therefore it's assumed that the name it's a unique field.
2. It's assumed that a student can't be detected in more than one classroom on the same day and range time.
3. In the input file, there is not specified  any kind of periodicity in terms of the PRESENCE records aka it's impossible to know which Thursday, for instance, of certain week is this record:

        Presence Marco 4 09:02 10:17 R100

    So, it's impossible to know if the following border case is the student in two different Thursdays or a simple typing error.

        Presence Marco 4 09:02 10:17 R100
        Presence Marco 4 09:02 10:17 R100

    In this fact, and keeping the concept of point 2, exists two easy paths:

    3.1 Add periodicity in name of the input file. aka:
        2020-03-10.txt

    3.2 Assuming that all the days are distinct so in the previous example, these two records are two Thursdays of two differents weeks, so will be count.

    It's assumed (for simplicity) the 3.2 point.

4. The below entity-relationship model is the representation of the solution (more details in project/models):

  ![Alt text](project/apps/task_manager_backend/tests/resources/erm.png?raw=true "entity-relationship-model")

5. All the documentation is present in swagger (<http://127.0.0.1:8000/swagger/>). But also, all the worked endpoints for this test, are present in the file called: "task_manager.postman_collection.json", which is a Postman export file with all the endpoints used for the tests (in the root of the project).

## Setup

1. Copy / clone repo from github.

        git clone https://github.com/adosaa/task_manager.git

2. If you already have the repo, pull the latest version

        git checkout main
        git pull

3. Create a virtualenv. Note: supporting Pyhton 3.11.

        virtualenv -p python3.11 task_manager-env
        source task_manager-env/bin/activate

4. Switch to the project root and install requirements.

        pip install -r requirements.txt

5. Install Postgresql 15 and create a database with a free-to-choice name, just remember that name to put it as an environment variable in the next section. Just for running purposes, use the Postgres user or whatever user with  "database creator" grants to execute unit tests.

6. Create a folder called "secrets" at the "project" folder level and after that, create an "a .env" file with the following environment variables:

        SECRET_KEY=jot!b6p8=do)ad2&2hce94zu*r8y9hqht=@t&*r$qqeubp+%xv
        JWT_SECRET_KEY=og*wldp6iy(7vy5d5#$h0*+(%=wd&u)8!n9d3k526s-ly_xvn#
        DB_ENGINE=django.db.backends.postgresql
        DB_NAME=<DB_NAME>
        DB_USER=postgres
        DB_PASSWORD=<DB_NAME>
        DB_HOST=localhost
        DB_PORT=5432

6. Migrate Django datamodels

        ./manage.py migrate

7. For easy use, we recommend load the initial data (test user) with fixtures.

        ./manage.py loaddata auth_user_fixture

    The credentials of this users is:

    ```bash
    username: fvera
    password: 6-r6jC&5CRk3S$qVv
    ```

## Run

#### Subsequent runs

```bash
./manage.py runserver
```

### Run test

```bash
./manage.py test project/apps
```

## Usage

Once the setup & run step is done, it's recommended:

1. execute POST endpoint <http://127.0.0.1:8000/auth/login/> and login with the credentials served in the step number 7 of setup:

![Alt text](project/apps/task_manager/tests/resources/login.png?raw=true "upload_file")

2. 2. The user can explore for all the rest of the endpoints present in the documentation or in the postman export file, but for getting the exercise result, execute the GET endpoint <http://127.0.0.1:8000/api/v1/report/> as the below image:

![Alt text](project/apps/task_manager_backend/tests/resources/report.png?raw=true "report")
