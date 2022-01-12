from django.contrib import admin

from autos.models import Make, Auto
from cats.models import Cat, Breed

# Register your models here.

admin.site.register(Make)
admin.site.register(Auto)
admin.site.register(Cat)
admin.site.register(Breed)