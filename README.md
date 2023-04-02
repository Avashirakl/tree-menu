# tree-menu
Test Project

python -m venv venv

venv/bin/activate (venv/Scripts/activate) - Windows

pip install -r requirements.txt

Проведите миграции, при migrate создается superuser username:admin, password:admin,
и модели MenuItem для примера(в файле menu/migrations/0004_example_menu_list.py): 

python manage.py migrate
python manage.py runserver

Переходите по ссылке и вы должны увидеть древовидное меню:

http://127.0.0.1:8000/main_page/
