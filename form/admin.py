from django.contrib import admin
from .models import State, Information

# Register your models here.
@admin.register(Information)
class InformationAdmin(admin.ModelAdmin):
    list_display = ["first_name", "middle_name", "last_name", "date_of_birth", "date_updated", "date_created"]
    list_filter = ["first_name", "date_created"]
    fieldset = (
        
    )
admin.site.register(State)
#admin.site.register(Information, InformationAdmin)