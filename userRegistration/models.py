
from django.db import models
from django import forms
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager,PermissionsMixin
from django.contrib.auth.hashers import make_password
from multiselectfield import MultiSelectField
from django.core.validators import MaxLengthValidator

class CustomUserManager(BaseUserManager):
    def create_user(self, registration_no, email, password=None):
        if not registration_no:
            raise ValueError('Users must have a registration number')

        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            registration_no=registration_no,
            email=self.normalize_email(email),
            # password=password,
            # is_verified = is_verified
        )

        user.set_password(make_password(password))
        user.save(using=self._db)
        return user

    def create_superuser(self, registration_no, email, password):
        user = self.create_user(
            registration_no=registration_no,
            email=email,
            password=password,
            # is_verified=is_verified
        )

        user.isadmin= True
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class CustomUser(AbstractBaseUser,PermissionsMixin):
    registration_no = models.CharField(unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField()
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=True)
    # is_verified = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'registration_no'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.registration_no

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True


# class Student(models.Model):
#     name = models.CharField(max_length=100)
#     department = models.CharField(max_length=100)
#     session = models.CharField(max_length=100)
#     registration_number = models.CharField(max_length=100)
#     hall = models.CharField(max_length=100)
#     email = models.EmailField()
#     fathers_name = models.CharField(max_length=100)
#     mothers_name = models.CharField(max_length=100)
#     present_address = models.CharField(max_length=100)
#     permanent_address = models.CharField(max_length=100)
#     social_media_link_1 = models.CharField(max_length=100)
#     social_media_link_2 = models.CharField(max_length=100, blank=True, null=True)
#     ssc_institution = models.CharField(max_length=100)
#     ssc_board = models.CharField(max_length=100)
#     ssc_passing_year = models.IntegerField()
#     hsc_institution = models.CharField(max_length=100)
#     hsc_board = models.CharField(max_length=100)
#     hsc_passing_year = models.IntegerField()
#     photography = models.BooleanField(default=False)
#     content_writing = models.BooleanField(default=False)
#     debating = models.BooleanField(default=False)
#     graphics_designing = models.BooleanField(default=False)
#     web_development = models.BooleanField(default=False)
#     hobbies_and_interests = models.CharField(max_length=100)
#     why_join_duits = models.CharField(max_length=100)
#     information_tech_interest = models.CharField(max_length=100)
#     other_club_member = models.CharField(max_length=100)
#     microsoft_word = models.BooleanField(default=False)
#     microsoft_excel = models.BooleanField(default=False)
#     adobe_illustrator_or_photoshop = models.BooleanField(default=False)
#     canva = models.BooleanField(default=False)
#     google_workspace = models.BooleanField(default=False)
#     program_compilers = models.BooleanField(default=False)


#     def __str__(self):
#         return self.name

Board_List =(
   ('','Select Your Education Board'),
   ('Dhaka','Dhaka'),
   ('Rajshahi', 'Rajshahi'),
   ('Chittagong', 'Chittagong'),
   ('Sylhet', 'Sylhet'),
   ('Dinajpur', 'Dinajpur'),
   ('Mymensing', 'Mymensing'),
   ('Barishal', 'Barishal'),
   ('Khulna', 'Khulna'),
   ('Cumilla', 'Cumilla')
)
Passing_Year = (
    ('', 'Select Your Passing Year'),
    ('2016', '2016'),
    ('2017', '2017'),
    ('2018', '2018'),
    ('2019', '2019'),
    ('2020', '2020'),
    ('2021', '2021'),
    ('2022', '2022'),
    ('2023', '2023'),
    ('2024', '2024'),
    ('2025', '2025'),
    ('2026', '2026'),
    ('2027', '2027'),
    ('2028', '2028')
)
Gender = (
    ('','Select Your Gender'),
    ('Male','Male'),
    ('Female','Female')
)
EXtra_Activities=(
    ('Photography', 'Photography'),
    ('Contnet Writing', 'Contnet Writing'),
    ('Debating', 'Debating'),
    ('Graphics Design', 'Graphics Design'),
    ('Web Development', 'Web Development'),
)
Expertise_Skill=(
    ('Microsoft Word', 'Microsoft Word'),
    ('Microsoft Excel', 'Microsoft Excel'),
    ('Adobe Illustrator or Photoshop', 'Adobe Illustrator or Photoshop'),
    ('Canva', 'Canva'),
    ('Google Workspace', 'Google Workspace'),
    ('Program Compilers', 'Program Compilers'),

)
Blood_Group=(
    ('','Select Your Blood Group'),
    ('A+','A+'),
    ('A-','A-'),
    ('B+','B+'),
    ('B-','B-'),
    ('AB+','AB+'),
    ('AB-','AB-'),
    ('O+','O+'),
    ('O+','O+')
)
class MyForm(models.Model):
    image = models.ImageField(upload_to='media/', blank=True,
                              verbose_name='Please select a image', max_length=255)
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    session = models.CharField(max_length=100)
    registration_number = models.CharField(max_length=100)
    hall = models.CharField(max_length=100)
    email = models.EmailField()
    fathers_name = models.CharField(max_length=100)
    mothers_name = models.CharField(max_length=100)
    present_address = models.CharField(max_length=100)
    permanent_address = models.CharField(max_length=100)
    contact_no = models.CharField(max_length=20)
    blood_group = models.CharField(max_length=10 ,choices=Blood_Group)
    gender = models.CharField(max_length=20,choices=Gender)
    social_media_link_1 = models.CharField(max_length=100,null=True)
    social_media_link_2 = models.CharField(max_length=100, blank=True, null=True)
    ssc_institution = models.CharField(max_length=100)
    ssc_board = models.CharField(max_length=20,choices=Board_List)
    ssc_passing_year = models.CharField(max_length=100,choices=Passing_Year)
    hsc_institution = models.CharField(max_length=100)
    hsc_board = models.CharField(max_length=20,choices=Board_List)
    hsc_passing_year = models.CharField(max_length=100,choices=Passing_Year)
    # multiselectfield
    Extra_CurriCular_Activities = MultiSelectField(choices=EXtra_Activities, default="", max_choices=5, max_length=255, validators=[MaxLengthValidator(255)])
    hobbies_interest = models.CharField(max_length=100)
    why_join_duits = models.CharField(max_length=100)
    information_tech_interest = models.CharField(max_length=100)
    other_club_member = models.CharField(max_length=100)
    skillsets = MultiSelectField(choices=Expertise_Skill, default="",max_choices=6, max_length=255, validators=[MaxLengthValidator(255)])
    def __str__(self):
        return self.name
