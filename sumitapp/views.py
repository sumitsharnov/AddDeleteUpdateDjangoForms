from django.shortcuts import render

from .management.commands.load_data import OneToMany
from .models import University
from .models import Countries


def home(request):
    university = University.objects.all()

    return render(request, 'home.html', {'universitydata': university})

def studentdetail(request):
    university = University.objects.all()
    return render(request, 'studentdetails.html', {'students': university})


def adddetails(request):
    return render(request, 'adddetails.html')


def updatedetails(request):
    return render(request, 'updatedetails.html')


def deletedetails(request):
    return render(request, 'deletedetails.html')


def successmessage(request):
    universityid = request.POST["universityid"]
    university_name = request.POST["university_name"]
    city_id = request.POST["city_id"]
    country_id = request.POST["country_id"]
    city_name = request.POST["city_name"]
    course_count = request.POST["course_count"]
    country_name = request.POST["country_name"]

    # university_info, created = University.objects.get_or_create(university_id=universityid, country_id=country_id, university_name=university_name, city_id=city_id, city_name=city_name, defaults={'course_count': course_count})
    # print(created)
    # if not created:
    #     university_info.save()
    # else:
    #     print("Failed"),country_id=country_id, university_name=university_name, city_id=city_id, city_name=city_name
    # try:
    #     University.objects.get(university_id=universityid, university_name=university_name)
    #
    #     try:
    #         University.objects.get(city_name=city_name, city_id=city_id)
    #         print("Already exists")
    #         return render(request, 'failedmessage.html')
    #     except:
    #         try:
    #             University.objects.get(city_id=city_id)
    #             print("Already exists")
    #             return render(request, 'failedmessage.html')
    #         except:
    #             try:
    #                 University.objects.get(city_name=city_name)
    #                 print("Already exists")
    #                 return render(request, 'failedmessage.html')
    #             except:
    #                 university_info = University(university_id=universityid, country_id=country_id,
    #                                              university_name=university_name, city_id=city_id,
    #                                              city_name=city_name, course_count=course_count)
    #                 university_info.save()
    #                 country_info = Countries(country_unique_Id=country_id, country_name=country_name)
    #                 country_info.save()
    #                 oneToMany = OneToMany()
    #                 oneToMany.oneToManyRelation(country_info)
    #                 return render(request, 'successmessage.html')
    #                 print("Created successfully")
    # except:
    try:
        University.objects.get(university_id=universityid)
        print("Already exists")
        return render(request, 'failedmessage.html')
    except:
        try:
            University.objects.get(university_name=university_name)
            print("Already exists")
            return render(request, 'failedmessage.html')
        except:
            try:
                University.objects.get(country_id=country_id)
                print("Already exists")
                return render(request, 'failedmessage.html')
            except:
                try:
                    University.objects.get(city_name=city_name, city_id=city_id)
                    print("Already exists")
                    return render(request, 'failedmessage.html')
                except:
                    try:
                        University.objects.get(city_id=city_id)
                        print("Already exists")
                        return render(request, 'failedmessage.html')
                    except:
                        try:
                            University.objects.get(city_name=city_name)
                            print("Already exists")
                            return render(request, 'failedmessage.html')
                        except:
                            university_info = University(university_id=universityid, country_id=country_id,
                                                         university_name=university_name, city_id=city_id,
                                                         city_name=city_name, course_count=course_count)
                            university_info.save()
                            country_info = Countries(country_unique_Id=country_id, country_name=country_name)
                            country_info.save()
                            oneToMany = OneToMany()
                            oneToMany.oneToManyRelation(country_info)
                            return render(request, 'successmessage.html')
                            print("Created successfully")


def failedmessage(request):
    return render(request, 'failedmessage.html')

def updatedetailsuccess(request):
    print("Sumit")
