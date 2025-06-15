import os
from django.core.management.base import BaseCommand, CommandError
from django.core.management import call_command
from core.models import CustomUser
from dotenv import load_dotenv

class Command(BaseCommand):
    help = 'Sets up the project by making migrations, migrating, and creating a superuser'

    def handle(self, *args, **kwargs):
        try:
            # Load environment variables from .env file
            load_dotenv()
            username = os.getenv('ADMIN_USERNAME', 'admin')
            email = os.getenv('ADMIN_EMAIL', 'facundoolivam@gmail.com')
            password = os.getenv('ADMIN_PASSWORD', 'pepe1234')

            username2 = 'devs'
            email2 = 'devs@gmail.com'
            password2 = 'devs1234'

            # Step 1: Make migrations
            self.stdout.write('Making migrations...')
            call_command('makemigrations')
            self.stdout.write(self.style.SUCCESS('Migrations created successfully.'))

            # Step 2: Apply migrations
            self.stdout.write('Applying migrations...')
            call_command('migrate')
            self.stdout.write(self.style.SUCCESS('Migrations applied successfully.'))

            # Step 3: Create superuser with environment variables
            if not CustomUser.objects.filter(username=username).exists():
                self.stdout.write('Creating superuser...')
                CustomUser.objects.create_superuser(
                    username=username,
                    email=email,
                    password=password,
                )
                self.stdout.write(self.style.SUCCESS('Superuser created successfully.'))
            else:
                self.stdout.write(self.style.WARNING('Superuser already exists.'))

            # Create a test user
            if not CustomUser.objects.filter(username=username2).exists():
                self.stdout.write('Creating test user...')
                CustomUser.objects.create_user(
                    username=username2,
                    email=email2,
                    password=password2,
                )
                self.stdout.write(self.style.SUCCESS('Test user created successfully.'))
            else:
                self.stdout.write(self.style.WARNING('Test user already exists.'))

        except CommandError as e:
            raise CommandError(f"Error: {e}")