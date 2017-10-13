from django.contrib import admin

from pets.models import Cat, Dog


@admin.register(Cat)
class CatAdmin(admin.ModelAdmin):
    pass


@admin.register(Dog)
class DogAdmin(admin.ModelAdmin):
    pass
