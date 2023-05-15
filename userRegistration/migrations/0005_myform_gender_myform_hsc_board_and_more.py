# Generated by Django 4.2 on 2023-05-14 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userRegistration', '0004_myform_blood_group_myform_contact_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='myform',
            name='gender',
            field=models.CharField(choices=[('', 'Select Your Gender'), ('Male', 'Male'), ('Female', 'Female')], default='', max_length=8),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='myform',
            name='hsc_board',
            field=models.CharField(choices=[('', 'Select Your Education Board'), ('Dhaka', 'Dhaka'), ('Rajshahi', 'Rajshahi'), ('Chittagong', 'Chittagong'), ('Sylhet', 'Sylhet'), ('Dinajpur', 'Dinajpur'), ('Mymensing', 'Mymensing'), ('Barishal', 'Barishal'), ('Khulna', 'Khulna'), ('Cumilla', 'Cumilla')], default='', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='myform',
            name='hsc_institution',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='myform',
            name='hsc_passing_year',
            field=models.CharField(choices=[('', 'Select Your Passing Year'), ('2016', '2016'), ('2017', '2017'), ('2018', '2018'), ('2019', '2019'), ('2020', '2020'), ('2021', '2021'), ('2022', '2022'), ('2023', '2023'), ('2024', '2024'), ('2025', '2025'), ('2026', '2026'), ('2027', '2027'), ('2028', '2028')], default='', max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='myform',
            name='social_media_link_1',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='myform',
            name='social_media_link_2',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='myform',
            name='ssc_board',
            field=models.CharField(choices=[('', 'Select Your Education Board'), ('Dhaka', 'Dhaka'), ('Rajshahi', 'Rajshahi'), ('Chittagong', 'Chittagong'), ('Sylhet', 'Sylhet'), ('Dinajpur', 'Dinajpur'), ('Mymensing', 'Mymensing'), ('Barishal', 'Barishal'), ('Khulna', 'Khulna'), ('Cumilla', 'Cumilla')], default='', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='myform',
            name='ssc_institution',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='myform',
            name='ssc_passing_year',
            field=models.CharField(choices=[('', 'Select Your Passing Year'), ('2016', '2016'), ('2017', '2017'), ('2018', '2018'), ('2019', '2019'), ('2020', '2020'), ('2021', '2021'), ('2022', '2022'), ('2023', '2023'), ('2024', '2024'), ('2025', '2025'), ('2026', '2026'), ('2027', '2027'), ('2028', '2028')], default='', max_length=10),
            preserve_default=False,
        ),
    ]
