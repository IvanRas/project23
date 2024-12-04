from django.core.management import BaseCommand

from users.models import CustomUserCreationForm


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = CustomUserCreationForm.objects.create(email='admin@example.com')
        user.set_password('123123')
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save()
