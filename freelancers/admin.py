from django.contrib import admin
from .models import Freelancer, WorkingField, Profile, Platform, Job, Intake, City, Country

# Register your models here.


class ProfileInline(admin.TabularInline):
    model = Profile
    extra = 0


class FreelancerAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'city', 'intake']
    inlines = [ProfileInline]


class WorkingFieldAdmin(admin.ModelAdmin):
    pass


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['freelancer', 'status', 'platform', 'url', 'working_field']
    list_filter = ['status', 'platform', 'working_field']


class PlatformAdmin(admin.ModelAdmin):
    pass


class JobAdmin(admin.ModelAdmin):
    list_display = ['profile', 'title', 'job_type', 'client_country', 'is_interviewed', 'is_hired',
                    'is_completed_successfully', 'is_disputed', 'total_job_income']
    fieldsets = (
        ('Proposal', {
            'fields': ('profile', 'url', 'title', 'working_field', 'cover_letter', 'job_type', 'rate',
                       'client_country', 'applied_at',)
        }),
        ('Interview', {
            'fields': ('is_interviewed', 'interviewed_at', 'interview_channel', 'interview_notes')
        }),
        ('Hiring', {
            'fields': ('is_hired', 'hired_at', 'hiring_notes')
        }),
        ('Completed', {
            'fields': ('is_completed_successfully', 'is_disputed', 'dispute_notes', 'total_working_hours',
                       'total_job_income', 'notes', 'closed_at')
        })
    )

    list_filter = ('job_type', 'is_interviewed', 'is_hired', 'is_completed_successfully', 'is_disputed')



class IntakeAdmin(admin.ModelAdmin):
    list_display = ['name', 'start_date', 'end_date']


class CityAdmin(admin.ModelAdmin):
    pass


class CountryAdmin(admin.ModelAdmin):
    pass


admin.site.register(Freelancer, FreelancerAdmin)
admin.site.register(WorkingField, WorkingFieldAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Platform, PlatformAdmin)
admin.site.register(Job, JobAdmin)
admin.site.register(Intake, IntakeAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Country, CountryAdmin)


admin.site.site_title = 'ITI Freelancers'
admin.site.site_header = 'ITI Freelancers'

