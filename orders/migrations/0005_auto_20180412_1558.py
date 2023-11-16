# Generated by Django 2.0.3 on 2018-04-12 15:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('orders', '0004_auto_20180412_1552'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='customer_id',
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey( on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
