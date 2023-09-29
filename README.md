# TaskManager Backend

A backend app that manages all student's presence detection as a hiring test. This proof of concept includes:

* JWT authentication mechanism.
* Saving/Retrieving student's presence records and is able to generate reports of all student's presence in descending order.
* Documentation (<http://127.0.0.1:8000/docs/>)
* Coverage 89%

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

        git clone git@github.com:adosaa/task_manager_backend.git

2. If you already have the repo, pull the latest version

        git checkout master
        git pull

3. Create a virtualenv. Note: supporting Pyhton 3.8.

        virtualenv -p python3.8 task_manager-env
        source task_manager-env/bin/activate

4. Switch to the project root and install requirements.

        pip install -r requirements.txt

5. create in project/secrets folder a .env file with the follow env. variables:

        SECRET_KEY=<secret_key_to_election>
        DB_NAME=django.db.backends.sqlite3

6. Migrate Django datamodels

        ./manage.py migrate

7. For easy use, we recommend load the initial data with fixtures

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

1. execute POST endpoint <http://127.0.0.1:8000/api/v1/input_file/> with an election file (or pick some of one example in project/apps/task_manager_backend/tests/resources):

![Alt text](project/apps/task_manager_backend/tests/resources/upload_input_file.png?raw=true "upload_file")

2. 2. The user can explore for all the rest of the endpoints present in the documentation or in the postman export file, but for getting the exercise result, execute the GET endpoint <http://127.0.0.1:8000/api/v1/report/> as the below image:

![Alt text](project/apps/task_manager_backend/tests/resources/report.png?raw=true "report")
