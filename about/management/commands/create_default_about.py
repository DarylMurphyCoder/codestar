from django.core.management.base import BaseCommand
from about.models import About

class Command(BaseCommand):
    help = 'Create a default About object if none exists.'

    def handle(self, *args, **options):
        if not About.objects.exists():
            About.objects.create(
                title="About Me",
                profile_image="placeholder",
                content="This is the default About page. Edit this content in the admin.",
            )
            self.stdout.write(self.style.SUCCESS('Default About object created.'))
        else:
            self.stdout.write(self.style.WARNING('About object already exists.'))
