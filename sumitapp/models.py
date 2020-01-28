from django.db import models


class University(models.Model):
    university_id = models.IntegerField(null=True)
    university_name = models.CharField(max_length=100, default='SOME STRING')
    city_id = models.IntegerField(null=True, default=0)
    country_id = models.IntegerField(null=True, default=0)
    city_name = models.CharField(max_length=100, default='SOME STRING')
    course_count = models.IntegerField(null=True, default=0)

    def __str__(self):
        return self.city_id


class Countries(models.Model):
    country_unique_Id = models.IntegerField(null=True, default=0)
    country_name = models.CharField(max_length=100, default='SOME STRING')
    countryvalues = models.ForeignKey(University, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.country_unique_Id
