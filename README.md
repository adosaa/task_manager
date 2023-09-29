# TaskManager Backend

A backend app for support Task management of multiple users and their requirements as a hiring test. This proof of concept includes:

* JWT authentication mechanism.
* CRUD endpoints for Task operations.
* Documentation (<http://127.0.0.1:8000/docs/>)
* Coverage 89%
* [OPTIONAL] serverless deployment in AWS Lambda with Zappa.

## Considerations

1. The design of the system was thought of as "school wall information", that everyone can put and create tasks, change their status, and so on. Very Similar to Jira's scrum wall.
2. In that order of ideas, we can assume the following sentences:

    2.1 Unless for management, the read operations will rarely be made in terms of all the collection of Tasks. Mostly will be filtered in terms of the user who made the task and paginated by the way. Therefore, read operations will not give a huge overhead to consider a DB with high throughput in these necessities like MySQL or MongoDB. However, this does not mean that optimizations such as dynamically selecting only a subset of fields per resource not be a good idea to reduce overhead in each request (<https://github.com/dbrgn/drf-dynamic-fields>).

    2.2 Quite the opposite, write operations made by multiples of users (and concurrent ) can be big trouble in terms of the scalability of the system. A DB capable of receiving concurrent requests in write operations like PostgreSQL, gives us robustness and scalability as long as we keep the filters and care in the reading operations.

3. Overall, PostgreSQL will be the DB chosen for this project due to this good trade-off between robustness and scalability.

4. By the above considerations, extra fields (as created_at), dynamically selecting fields (drf-dynamic-fields), and filters like search by "Task's user creator" (query param 'search') are necessary for good performance and read operations. The below entity-relationship model is the representation of the solution (more details in project/models):

  ![Alt text](project/apps/task_manager/tests/resources/model.png?raw=true "entity-relationship-model")

5. All the documentation is present in (<http://127.0.0.1:8000/docs/>). But also, all the worked endpoints for this test, are present in the file called: "TaskManager.postman_collection.json", which is a Postman export file with all the endpoints used for the tests (in the root of the project).

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

1.Execute POST endpoint <http://127.0.0.1:8000/auth/login/> and login with the credentials served in the step number 7 of setup:

![Alt text](project/apps/task_manager/tests/resources/login.png?raw=true "login")

    1.1 Copy the token value presented in the Endpoint response.

    ![Alt text](project/apps/task_manager/tests/resources/token.png?raw=true "token")

2.Paste the token value in the {{token}} placeholder in Header section of the first EP called "Create Task".

![Alt text](project/apps/task_manager/tests/resources/replaced_placeholder.png?raw=true "replaced_placeholder")

    2.1 After that, just click in send button to create a new Task.

    ![Alt text](project/apps/task_manager/tests/resources/create_task.png?raw=true "create_task")
