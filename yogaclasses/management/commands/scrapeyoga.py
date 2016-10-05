from django.core.management.base import BaseCommand, CommandError
from yogaclasses.models import Studio, Teacher, YogaClass
from scrape import YogaClassScraper

import datetime

studios = [{'studio': 'Stanton Street Yoga', 'link': 'http://www.stantonstreetyoga.com/classes/schedule/'}, 
            {'studio': 'Jivamukti Yoga', 'link': 'http://www.jivamuktiyoga.nyc/schedule/'}]

class Command(BaseCommand):
    help = 'Scrapes yoga classes data.'

    def handle(self, *args, **options):
        self.delete_old_data()
        self.start_scrape()
         
    def delete_old_data(self):
        """Remove old data about available yoga classes"""
        self.stdout.write('\nDeleted old yoga classes data at %s\n' % str(datetime.datetime.now()))
        YogaClass.objects.all().delete()

    def start_scrape(self):
        """Scrape current yoga class data from list of studios """
        self.stdout.write('\nScraping started at %s\n' % str(datetime.datetime.now()))
        for studio in studios:
            name = studio['studio']
            link = studio['link']
            s = YogaClassScraper(link)
            results = s.scrape()
            print(name, '- Number of results: ', len(results))
            self.save_classes(name, results)

    def save_classes(self, studio, yoga_classes):
        """Save classes to database."""
        for c in yoga_classes:
            studio = studio
            teacher = c['teacher']
            description = c['description']
            class_date = datetime.datetime.now().date()
            class_start = c['start']
            class_end = c['end']
            # studio = 'Felice Yoga2'
            # teacher = 'Felice 2'
            # description = 'Restorative2'
            # class_date = datetime.date(2016, 8, 28)
            # class_start = '10:30:00'
            # class_end = '11:30:00'
            if not Studio.objects.filter(name=studio):
                s = Studio(name=studio)
                s.save()
            s = Studio.objects.get(name=studio)

            if not Teacher.objects.filter(name=teacher):
                t = Teacher(name=teacher)
                t.save()
            t = Teacher.objects.get(name=teacher)
            
            if not YogaClass.objects.filter(studio__name=s, teacher__name=t, description=description, date=class_date, start_time=class_start, end_time=class_end):
                y = YogaClass(studio=s, teacher=t, description=description, date=class_date, start_time=class_start, end_time=class_end)
                y.save()
            else: 
                y = YogaClass.objects.get(studio__name=s, teacher__name=t, description=description, date=class_date, start_time=class_start, end_time=class_end)
            print(y)