#from django.contrib import admin

# Register your models here.
'''from django.contrib import admin
from .models import TripRegistration


admin.site.register(TripRegistration)
'''
from django.contrib import admin
from .models import TripRegistration


@admin.register(TripRegistration)
class TripRegistrationAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'phone',
        'email',
        'number_of_people',
        'food_preference',
    )


    