# Generated by Django 3.2.9 on 2021-11-08 13:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=200)),
                ('username', models.CharField(max_length=100, unique=True)),
                ('intro', models.CharField(blank=True, max_length=250, null=True)),
                ('bio', models.TextField(blank=True, null=True)),
                ('social_twitter', models.CharField(blank=True, max_length=100, null=True)),
                ('social_insta', models.CharField(blank=True, max_length=100, null=True)),
                ('created', models.DateField(auto_now_add=True)),
                ('id', models.UUIDField(editable=False, primary_key=True, serialize=False, unique=True, verbose_name=uuid.uuid4)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
