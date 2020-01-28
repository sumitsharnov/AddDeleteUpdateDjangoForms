# Generated by Django 3.0.2 on 2020-01-21 00:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sumitapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Countries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_unique_Id', models.IntegerField(default=0, null=True)),
                ('country_name', models.CharField(default='SOME STRING', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('university_id', models.IntegerField(null=True)),
                ('university_name', models.CharField(default='SOME STRING', max_length=100)),
                ('city_id', models.IntegerField(default=0, null=True)),
                ('country_id', models.IntegerField(default=0, null=True)),
                ('city_name', models.CharField(default='SOME STRING', max_length=100)),
                ('course_count', models.IntegerField(default=0, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Student',
        ),
        migrations.AddField(
            model_name='countries',
            name='countryvalues',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sumitapp.University'),
        ),
    ]