import requests
from abc import ABC
from csv import DictReader
from datetime import datetime

from django.core.management import BaseCommand
from sumitapp.models import University
from sumitapp.models import Countries
from pytz import UTC


class Command(BaseCommand):


    def handle(self, *args, **options):
        if University.objects.exists():
            print('This University already exists')
            return
        countries = requests.get("https://dhcr.clarin-dariah.eu/api/v1/countries/index").json()
        universityData = requests.get("https://dhcr.clarin-dariah.eu/api/v1/institutions/index?sort_count").json()
        print(countries)
        print("Creating Data")



        for universityrowdata in universityData:
            university = University()
            university.university_id = universityrowdata['id']
            university.university_name = universityrowdata['name']
            university.city_id = universityrowdata['city_id']
            try:
                University.objects.get(country_id = universityrowdata['country_id'])
                print("record already exists")
                print(universityrowdata['country_id'])
            except:
                university.country_id = universityrowdata['country_id']
            university.city_name = universityrowdata['city']['name']
            university.course_count=universityrowdata['course_count']
            university.save()
        for countryvalue in countries:
            country = Countries()
            #print(university.objects.get(university_id=6))
            #students = Students(student_Id=6, universiti=university)
            #students.student_name=studentdetail['name']
            #stuname = students.student_name
            country.country_unique_Id=countryvalue['id']
            country.country_name=countryvalue['name']
            #students.university=university.objects.get(university_id=6)
            country.save()
            oneToMany = OneToMany()
            oneToMany.oneToManyRelation(country)
            # try:
            #     country.countryvalues=University.objects.get(country_id = country.country_unique_Id)
            # except:
            #     print("Does nothing")
            # country.save()



class OneToMany():
    def oneToManyRelation(self, object):
        try:
            object.countryvalues=University.objects.get(country_id = object.country_unique_Id)
        except:
            print("Does nothing")
        object.save()


        # count = 6
        # for studentde in Students.objects.all():
        #     try:
        #         t =University.objects.get(university_id=count)
        #         print(t.university_name)
        #         students.universiti = t
        #         count = count + 134
        #         students.save()
        #     except:
        #         print("Does ")
    # for universityid in University.objects.all():
        #     uniId=universityid.university_id
        #     print(uniId)
        #     try:
        #         t = Students.objects.get(student_Id=uniId)
        #         university.students.add(t)
        #         students.save()
        #     except:
        #         print("Does nothing")
