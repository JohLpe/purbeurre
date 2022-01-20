# Generated by Django 3.2.9 on 2021-12-03 10:44

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0004_favorite'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='favorite',
            unique_together={('product', 'user')},
        ),
    ]