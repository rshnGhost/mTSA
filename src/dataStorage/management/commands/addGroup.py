from django.contrib.auth.models import Group
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Create a group with the given name'

    def add_arguments(self, parser):
        parser.add_argument('gname', type=str)

    def handle(self, *args, **options):
        name = options['gname']
        group, created = Group.objects.get_or_create(name=name)
        if created:
            print('Successfully created %s' % name)
        else:
            print('Group %s not created' % name)
