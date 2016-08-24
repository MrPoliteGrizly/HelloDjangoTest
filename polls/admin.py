from django.contrib import admin

# Register your models here.
from .models import Question, Choise, test

admin.site.register(Question)
admin.site.register(Choise)
admin.site.register(test)
