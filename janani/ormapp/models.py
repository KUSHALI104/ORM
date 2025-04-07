from django.db import models
from django.contrib import admin
class Bankloan(models.Model):
    Name=models.CharField(max_length=50);
    Gender=models.CharField(max_length=10);
    Token_no=models.IntegerField(primary_key=True);
    Amount=models.IntegerField();
    Phone=models.IntegerField();


class BankloanAdmin(admin.ModelAdmin):
    list_display=('Name','Gender','Token_no','Amount','Phone')