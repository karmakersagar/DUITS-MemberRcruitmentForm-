# Generated by Django 4.2 on 2023-05-14 20:24

import django.core.validators
from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('userRegistration', '0006_myform_extra_curricular_activities_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='myform',
            name='information_tech_interest',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='myform',
            name='other_club_member',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='myform',
            name='skillsets',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Microsoft Word', 'Microsoft Word'), ('Microsoft Excel', 'Microsoft Excel'), ('Adobe Illustrator or Photoshop', 'Adobe Illustrator or Photoshop'), ('Canva', 'Canva'), ('Google Workspace', 'Google Workspace'), ('Program Compilers', 'Program Compilers')], default='', max_length=255, validators=[django.core.validators.MaxLengthValidator(255)]),
        ),
        migrations.AddField(
            model_name='myform',
            name='why_join_duits',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
