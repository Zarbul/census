from django.db import models

class People(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    f_name = models.CharField('Имя', max_length=50)
    l_name = models.CharField('Фамилия', max_length=50)
    age = models.PositiveSmallIntegerField('Возраст', default=18)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    department = models.ForeignKey('Department', on_delete=models.DO_NOTHING, null=True, blank=True)
    language = models.ForeignKey('Language', on_delete=models.DO_NOTHING, null=True, blank=True)

    def __str__(self):
        return f'{self.f_name} {self.l_name}'


class Department(models.Model):
    name = models.CharField('Отдел', max_length=50, null=True, blank=True)
    floor = models.PositiveSmallIntegerField('Этаж')

    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField('Язык программирования', max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name