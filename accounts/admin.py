from django.contrib import admin
from .models import CompanyCategory, Company, Worker
# Register your models here.

@admin.register(CompanyCategory)
class UserAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['username' ,'companyname', 'is_comapny', 'is_worker', ]
    prepopulated_fields = {'slug':('companyname',)}

@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    list_display = ['id','username', 'is_comapny', 'is_worker', 'company']
    prepopulated_fields = {'slug':('company',)}