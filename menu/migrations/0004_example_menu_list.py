from django.db import migrations, models
from django.contrib.auth import get_user_model

from menu.models import MenuItem


def generate_superuser(apps, schema_editor):
    """Create a new superuser """
    User = get_user_model()
    if User.objects.filter(username='admin', is_superuser=True, is_staff=True).exists() is False:
        admin = User.objects.create_superuser(
            username='admin',
            email='admin@admin.ru',
            password='admin'
        )
        admin.save()


def create_example_menu(apps, schema_editor):
    """ Создание примерных обьектов модели меню """
    main_menu = MenuItem.objects.create(
        title='main_menu',
        named_url='main_page',
    )
    main_menu.save()
    child_menu = MenuItem.objects.create(
        title='child_menu',
        named_url='main_page',
        parent=main_menu,
    )
    child_menu.save()
    grandchild_menu = MenuItem.objects.create(
        title='grandchild_menu',
        named_url='main_page',
        parent=child_menu,
    )
    grandchild_menu.save()


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_auto_20230401_1200'),
    ]

    operations = [
        migrations.RunPython(create_example_menu),
        migrations.RunPython(generate_superuser)
    ]
