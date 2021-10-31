from django.contrib import admin
from .models import *

admin.site.register(User)
admin.site.register(Institutes)
admin.site.register(Transactions)
admin.site.register(Visit_Purpose)
admin.site.register(Institute_Classification)
admin.site.register(Transactction_Status)

# Register your models here.
