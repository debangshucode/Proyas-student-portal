from django.contrib import admin
from .models import Student, Customer,Co_Ordinator
from import_export.admin import ImportExportModelAdmin




# Register your models here.

@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['username' , 'user_type' , 'email']

@admin.register(Student)
class StudentModelAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = [ 'student_name','district','center_codes','classes','roll_no' ]
    list_filter = ['district','classes','center_codes'] 

@admin.register(Co_Ordinator)
class CoOrdinatorModelAdmin(admin.ModelAdmin):
    list_display= ['district']