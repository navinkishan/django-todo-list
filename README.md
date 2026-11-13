**Django To-Do List Application :**



A simple and user-friendly To-Do List application built using Python and Django. It helps users organize daily tasks, manage priorities, track deadlines, and monitor completed and pending tasks.



**Features :**



* Add new tasks with titles and descriptions
* Edit existing tasks
* Delete tasks
* Mark tasks as completed
* Set task priorities (High, Medium, Low)
* Set due dates for tasks
* Search tasks by title
* Filter tasks by completed and pending status
* Sort tasks by priority and due date
* Dashboard with total, completed, and pending task counts



**Technologies Used :**



* Python 3.14.5
* Django 6.1.3
* SQLite3
* HTML
* CSS



**Project Structure :**



```text

todo/

│

├── tasks/

│   ├── migrations/

│   ├── templates/

│   │   └── tasks/

│   │       ├── home.html

│   │       └── edit.html

│   ├── admin.py

│   ├── apps.py

│   ├── models.py

│   ├── tests.py

│   ├── urls.py

│   └── views.py

│

├── todo/

│   ├── settings.py

│   ├── urls.py

│   ├── asgi.py

│   └── wsgi.py

│

├── manage.py

├── requirements.txt

└── README.md

```



**Installation and Setup :**



&#x20;1. Clone the repository



```bash

git clone YOUR\_GITHUB\_REPOSITORY\_URL

```



&#x20;2. Open the project folder



```bash

cd todo

```



&#x20;3. Create a virtual environment



```bash

python -m venv venv

```



&#x20;4. Activate the virtual environment



Windows:



```bash

venv\\Scripts\\activate

```



&#x20;5. Install dependencies



```bash

pip install -r requirements.txt

```



&#x20;6. Set your Django secret key



Generate a new secret key:



```bash

python -c "from django.core.management.utils import get\_random\_secret\_key; print(get\_random\_secret\_key())"

```



**Set the generated key in Windows Command Prompt:**



```cmd

set DJANGO\_SECRET\_KEY=YOUR\_GENERATED\_SECRET\_KEY

```



&#x20;7. Apply database migrations



```bash

python manage.py migrate

```



&#x20;8. Run the development server



```bash

python manage.py runserver

```



&#x20;9. Open in your browser



```text

http://127.0.0.1:8000/

```



&#x20;**Screenshots :**



Screenshots of the application will be added here.



&#x20;**Database :**



This project uses SQLite as its database.



Django migrations automatically create the required database tables.



&#x20;**Future Improvements :**



* &#x20;User registration and login
* &#x20;Individual task management for each user
* &#x20;Task reminders and notifications
* &#x20;Improved responsive design



\## Author



\*\*Navin Kishan\*\*



\## License



This project is available for educational and personal use.



