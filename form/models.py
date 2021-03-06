from django.db import models

# Create your models here.

class State(models.Model):
    State = models.CharField(max_length = 20, null = False)
    
    def __str__(self):
        return f"{self.State}"
        
class Information(models.Model):
    first_name = models.CharField(max_length = 30, null = False, help_text = "your own personal name")
    middle_name = models.CharField(max_length = 30, null = False, help_text = "your own second name")
    last_name = models.CharField(max_length = 30, null = False, help_text = "your family name")
    state_of_origin = models.ForeignKey(State, null = False, on_delete = models.PROTECT)
    summary = models.TextField(null = True, help_text = "Tell us a little about yourself")
    date_of_birth = models.DateField(null = False)
    date_created = models.DateTimeField(auto_now = True)
    date_updated = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        return f"{self.first_name} ({self.middle_name} {self.last_name} {self.date_of_birth}) ({self.date_created} {self.date_updated})"
    
    