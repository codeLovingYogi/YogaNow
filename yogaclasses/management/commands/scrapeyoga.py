from django.core.management.base import BaseCommand, CommandError
#from polls.models import Question as Poll
from scrape import YogaClassScraper

import datetime

class Command(BaseCommand):
    help = 'Scrapes yoga classes data'

    def handle(self, *args, **options):
    	self.stdout.write('\nScraping started at %s\n' % str(datetime.datetime.now()))
    	s = YogaClassScraper()
    	s.scrape()