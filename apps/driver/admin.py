from django.contrib import admin

# Register your models here.
class DriverAdmin(admin.ModelAdmin):
    exclude = ('ratings','curr_lat', 'curr_long', 'city', 'state', 'country',)