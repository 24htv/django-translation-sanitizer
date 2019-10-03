from django.core.management.commands import makemessages


class Command(makemessages.Command):
    msgmerge_options = ['--previous', '-N', '-s', '-q', '--previous']
