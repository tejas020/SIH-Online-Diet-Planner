# Generated by Django 4.2.5 on 2023-09-15 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='getstarted',
            old_name='City',
            new_name='city',
        ),
        migrations.RenameField(
            model_name='getstarted',
            old_name='Contact',
            new_name='contact',
        ),
        migrations.RenameField(
            model_name='getstarted',
            old_name='First_Name',
            new_name='firstname',
        ),
        migrations.RenameField(
            model_name='getstarted',
            old_name='Last_Name',
            new_name='lastname',
        ),
        migrations.AddField(
            model_name='getstarted',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Rather not say', 'Rather not say')], default='1', max_length=20),
        ),
    ]
