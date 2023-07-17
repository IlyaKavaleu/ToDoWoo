To Do Woo
How started my project on your local server?

The project for study Django.

Stack:
Python
PostgreSQL
Redis
Local Developing
All actions should be executed from the source directory of the project and only after installing all requirements.

Firstly, create and activate a new virtual environment:

python3.9 -m venv ../venv
source ../venv/bin/activate
Install packages:

pip install --upgrade pip
pip install -r requirements.txt
Run project dependencies, migrations, fill the database with the fixture data etc.:

./manage.py migrate
./manage.py loaddata <path_to_fixture_files>
./manage.py runserver 

Run Redis Server:
redis-server

Run Celery:
celery -A store worker --loglevel=INFO


ToDoList for tasks.
The “to do woo” program is designed to create a list of tasks. The program helps to manage to-do lists, implement planned tasks and not forget anything.
The user has the ability to create a list of tasks, in the process of their execution, can change, delete, complete.
The program is implemented in the Python programming language using:

- Django;
- Redis;
- HTML;
- CSS;

Description of the program interface:
When the “New todo” button is clicked, the createtodo event handler invokes a modal window to create a task.
The window contains fields for title, description, priority selection, saving and returning to the main menu.
There is a limit on the number of characters on the field for entering the name, if the number of characters entered matches the maximum number,
are checked using the max_length attribute. In the modal window, the user has a warning label for the maximum number of input characters.
The project was implemented using caching, in my case "Redis", also for convenience, the tool "Django-Toolbar" was used, object-oriented programming,
framework Django, HTML, CSS, Python, SqLite(default), TestCase. 

1. - Modal window for creating a task.
The “Save” button, if all fields are filled, calls the createtodo () function in which the markup of the task is generated with all the entered values and
by choosing to change the state of the task.
![createtodo_1](https://github.com/IlyaKavaleu/Small-To-Do-List/assets/97099564/6ac58695-a2ce-45f5-b29b-20604d0d6f9e)

2. - Ability to change the importance of the task.
![createtodo_2](https://github.com/IlyaKavaleu/Small-To-Do-List/assets/97099564/334d7380-16ec-413c-9acd-aa806459f032)


3. - A generated block with a task.
Working with the task block. The block of each task contains information: Name; Description; A priority; Task state change menu.


Menu for working with the task.
Option "Done" - completes work on the task, makes its menu inactive.
Option "Edit" - causes the generation of a modal window for editing. The user can change: title, description, priority, keep or refuse
changes.
Option “Delete“ - deletes the task.
![crearedtodo_3](https://github.com/IlyaKavaleu/Small-To-Do-List/assets/97099564/fc74fb67-2427-4df8-942a-b1df22af510a)


4. - Task editing window.
Also in the task name input field, we can change it, as well as descriptions. You can also change the task status from “Important” to “Minor”.
Also, when choosing to change the importance of a task, the color of the task changes - from white to red!
![edittodo_4](https://github.com/IlyaKavaleu/Small-To-Do-List/assets/97099564/f2e80780-75b2-4eb8-9346-aac1d8ff1465)


5. - List of current tasks, which is formed using the "currenttodos" method.
![currenttodos_5](https://github.com/IlyaKavaleu/Small-To-Do-List/assets/97099564/141bd455-f730-454f-b787-5b6b91e56326)


6. - List of completed tasks, which is formed using the “completetodos“ method.
![completetodos_6](https://github.com/IlyaKavaleu/Small-To-Do-List/assets/97099564/09c2fc83-33d2-48c8-8c68-37048867b62b)


7. - Registration.
By clicking on the “Sign Up“ button, we will go to the user registration window with the following fields:
   -username
   -password 1
   -password 2
The password will need to be repeated.
After filling in the fields and upon successful registration, we are redirected to the main page with current tasks.


8. - Authorization
By clicking on the “Login“ button, we will go to the user logging window with the following fields:
   -username
   -password
After filling in the fields and upon successful authorization, we are also redirected to the main page with current tasks.
![authorization_8](https://github.com/IlyaKavaleu/Small-To-Do-List/assets/97099564/14e5baee-d547-46b9-86de-14f4e2afe877)


9. - Exit the session using the “Logout“ button.
![logout_9](https://github.com/IlyaKavaleu/Small-To-Do-List/assets/97099564/75b57950-277e-4e81-81cf-127a8d9afe9a)


10. - Library tests were imposed on the project “UnitTest“.
For example, a test for successful user registration is taken:
Have a check:
  - page status
  - redirect url
  - absence of a user
  - user presence
  - check by message(fail) for an error
![tests_10 png](https://github.com/IlyaKavaleu/Small-To-Do-List/assets/97099564/986c9f62-ceff-4766-b0ba-1c4b30a53edb)
