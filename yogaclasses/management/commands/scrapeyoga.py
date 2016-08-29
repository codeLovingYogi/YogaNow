from django.core.management.base import BaseCommand, CommandError
from yogaclasses.models import Studio, Teacher, YogaClass
from scrape import YogaClassScraper

import datetime


class Command(BaseCommand):
    help = 'Scrapes yoga classes data'

    def handle(self, *args, **options):
        self.stdout.write('\nScraping started at %s\n' % str(datetime.datetime.now()))
        # s = YogaClassScraper()
        # results = s.scrape()

        # print('num results: ', len(results))

        # for j in range(len(results)):
        #     for key, value in results[j].items():
        #         print(key, ': ', value) 

        studio = 'Felice Yoga2'
        teacher = 'Felice 2'
        description = 'Restorative2'
        class_date = datetime.date(2016, 8, 28)
        class_start = '10:31:00'
        class_end = '11:31:00'

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