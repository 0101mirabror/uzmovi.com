# Generated by Django 4.0.3 on 2022-03-12 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_alter_movie_language'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='category_id',
            field=models.IntegerField(null=True),
        ),
    ]
