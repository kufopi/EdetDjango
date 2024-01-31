from django.contrib import admin
from import_export.admin import ImportExportModelAdmin


# Register your models here.
from .models import Session,UniversityStaff,User,Postgrad,Undergrad,VentureStaff
#from import_export.admin import ImportExportModelAdmin

class SessionfinderFilter(admin.SimpleListFilter):

    title = 'session'
    parameter_name = 'session'

    def lookups(self, request, model_admin):
        sessions = Session.objects.all()
        return [(session.pk,session.academic_session) for session in sessions]

    def queryset(self, request, queryset):
        value =self.value()
        if value is not None:
            return queryset.filter(session=self.value())
        return queryset


admin.site.register(Session)



class UniversityStaffAdmin(ImportExportModelAdmin):
    list_display= ("surname","middle_name","first_name","staff_id","gender","designation")
    list_filter = (SessionfinderFilter,"gender",)
    search_fields =("surname__startswith",)


class PostgradAdmin(ImportExportModelAdmin):
    list_display= ("surname","middle_name","first_name","staff_id","gender","level","department")
    list_filter = (SessionfinderFilter,"department",'level',)
    search_fields =("surname__startswith",)
    

class UndergradAdmin(ImportExportModelAdmin):
    list_display= ("surname","middle_name","first_name","matric_id","gender","level","department")
    list_filter = (SessionfinderFilter,"department",'level',)
    search_fields =("surname__startswith",)


class VentureStaffAdmin(ImportExportModelAdmin):
    list_display= ("surname","middle_name","first_name","staff_id","gender","designation")
    list_filter = (SessionfinderFilter,"gender",)
    search_fields =("surname__startswith",)

admin.site.register(UniversityStaff,UniversityStaffAdmin)
admin.site.register(User)
admin.site.register(Postgrad,PostgradAdmin)
admin.site.register(Undergrad,UndergradAdmin)
admin.site.register(VentureStaff,VentureStaffAdmin)
