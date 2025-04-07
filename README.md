# Ex02 Django ORM Web Application
## Date: 01/04/25

## AIM
To develop a Django application to store and retrieve data from Movies Database using Object Relational Mapping(ORM).

## ENTITY RELATIONSHIP DIAGRAM



## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
```
admin.py
from django.contrib import admin
from .models import Bankloan,BankloanAdmin
admin.site.register(Bankloan,BankloanAdmin)

```
```
model.py
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

```



## OUTPUT
![alt text](<Screenshot 2025-04-07 235122.png>)


## RESULT
Thus the program for creating a database using ORM hass been executed successfully
