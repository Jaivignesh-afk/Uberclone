from django.contrib import admin

# Register your models here.
class RiderAdmin(admin.ModelAdmin):
    exclude = ('curr_lat', 'curr_long', 'city', 'state', 'country',)