from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    help = "Create production admin user"

    def handle(self, *args, **kwargs):
        User = get_user_model()

        username = "pujitha_admin"
        email = "pujth123@gmail.com"
        password = "CREATE_YOUR_PASSWORD_HERE"

        if User.objects.filter(username=username).exists():
            self.stdout.write("Admin user already exists.")
        else:
            User.objects.create_superuser(
                username=username,
                email=email,
                password=password
            )
            self.stdout.write("Admin user created successfully.")