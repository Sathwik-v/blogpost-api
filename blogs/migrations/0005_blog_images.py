# Generated by Django 3.2.9 on 2021-11-08 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0004_alter_blog_feature_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='images',
            field=models.ImageField(blank=True, null=True, upload_to='uploaded'),
        ),
    ]
