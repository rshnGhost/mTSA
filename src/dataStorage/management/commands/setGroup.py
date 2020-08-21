from django.contrib.auth.models import User, Group
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'add user(s) to groups'

    def add_arguments(self, parser):
        parser.add_argument('gname', type=str)
        parser.add_argument('username', nargs='+', type=str)

    def handle(self, *args, **options):
        gname = options['gname']
        group = Group.objects.get(name=gname)
        for name in options['username']:
            try:
                user = User.objects.get(username=name)
                group.user_set.add(user)
                print('User %s was added into %s group'%(name, gname))
            except User.DoesNotExist:
                print('No user with username as %s'% name)
