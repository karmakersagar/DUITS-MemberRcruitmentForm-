from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import CustomUser,MyForm
# Register your models here.
class CustomUserAdmin(BaseUserAdmin):
      list_display = ('registration_no','email','is_admin','is_active')
      search_fields = ('registration_no','email')
      # readonly_fields = ('date_joined','last_login')
      filter_horizontal=()
      list_filter=('is_active',)
      fieldsets=()
      add_fieldsets =(
       (None,{
        'classes':('wide'),
        'fields': ('registration_no','email','password'),
       }

       )
      )
      ordering=('registration_no',)
admin.site.register(CustomUser,CustomUserAdmin)

class MyFormAdmin(admin.ModelAdmin):
      list_display = ['image',
                  'name',
                  'department',
                  'session',
                  'registration_number',
                  'hall',
                  'email',
                  'fathers_name',
                  'mothers_name',
                  'present_address',
                  'permanent_address',
                  'contact_no',
                  'blood_group',
                  'gender',
                  'social_media_link_1',
                  'social_media_link_2',
                  'ssc_institution',
                  'ssc_board',
                  'ssc_passing_year',
                  'hsc_institution',
                  'hsc_board',
                  'hsc_passing_year',
                  'Extra_CurriCular_Activities',
                  'hobbies_interest',
                  'why_join_duits',
                  'information_tech_interest',
                  'other_club_member',
                  'skillsets']
      search_fields = ['registration_number']
      list_per_page= 50
admin.site.register(MyForm,MyFormAdmin)