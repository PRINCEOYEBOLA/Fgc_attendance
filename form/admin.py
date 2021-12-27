from django.contrib import admin
from .models import State, Information

# Register your models here.
@admin.register(Information)
class InformationAdmin(admin.ModelAdmin):
    list_display = ["first_name", "middle_name", "last_name", "date_of_birth", "date_updated", "date_created"]
    list_filter = ["first_name", "date_created"]
    fieldsets = (
        ("Names", 
        {"fields":("first_name", "middle_name", "last_name")}),
        
        ("Others",
         {
           "fields":("state_of_origin", "date_of_birth", "summary")
         })
        
                     
    )


admin.site.register(State)
#admin.site.register(Information, InformationAdmin)