from django.contrib import admin

# Register your models here.
from cafe.models import Cafe, CafeImage

admin.site.register(Cafe)
admin.site.register(CafeImage)