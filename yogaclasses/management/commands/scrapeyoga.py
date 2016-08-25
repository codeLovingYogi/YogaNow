from django.core.management.base import BaseCommand, CommandError
#from polls.models import Question as Poll
from scrape import scrape_classes

class Command(BaseCommand):
    help = 'Scrapes yoga classes data'

    def handle(self, *args, **options):
    	scrape_classes()