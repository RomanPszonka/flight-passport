from django.conf import settings
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):

    def handle(self, *args, **options):
        User = get_user_model()
        if User.objects.count() == 0:
            username = settings.DJANGO_SUPERUSER_USERNAME
            email = settings.DJANGO_SUPERUSER_EMAIL
            password = settings.DJANGO_SUPERUSER_INITIAL_PASSWORD
            print('Creating account for %s (%s)' % (username, email))
            admin = User.objects.create_superuser(email=email, username=username, password=password)
            admin.is_active = True
            admin.is_admin = True
            admin.save()
        else:
                print('Admin accounts can only be initialized if no Accounts exist')