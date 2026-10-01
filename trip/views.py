#from django.shortcuts import render

# Create your views here.
'''from django.shortcuts import render


def trip_form(request):
    return render(request, 'trip/trip_form.html')'''

from django.shortcuts import render
from .models import TripRegistration


def trip_form(request):

    if request.method == 'POST':

        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        number_of_people = request.POST.get('number_of_people')
        food_preference = request.POST.get('food_preference')
        message = request.POST.get('message')

        TripRegistration.objects.create(
            name=name,
            phone=phone,
            email=email,
            number_of_people=number_of_people,
            food_preference=food_preference,
            message=message
        )

        return render(request, 'trip/success.html')

    return render(request, 'trip/trip_form.html')