from django.contrib import admin

# Register your models here.
from census import models


@admin.register(models.People)
class PeopleAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Department)
class PeopleAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Language)
class PeopleAdmin(admin.ModelAdmin):
    pass