# Generated by Django 5.1.2 on 2024-10-15 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receipe_name', models.CharField(max_length=100)),
                ('receipe_desc', models.TextField()),
                ('receipe_img', models.ImageField(upload_to='receipe')),
            ],
        ),
    ]
