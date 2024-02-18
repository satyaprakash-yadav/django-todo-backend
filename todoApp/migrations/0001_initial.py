# Generated by Django 5.0.1 on 2024-01-26 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.CharField(max_length=300)),
                ('completed', models.BooleanField(default=False)),
                ('updated_At', models.DateTimeField(auto_now=True)),
                ('created_At', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
