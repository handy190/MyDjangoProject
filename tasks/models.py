from django.db import models

# Create your models here.


from django.db import models


class Status(models.TextChoices):
    UNSTARTED = 'u', "Not started yet"
    ONGOING = 'o', "Ongoing"
    FINISHED = 'f', "Finished"


SEX = [
    ('0', 'male'),
    ('1', 'female'),
]


class Task(models.Model):
    name = models.CharField(verbose_name="Task name", max_length=65, unique=True)
    status = models.CharField(verbose_name="Task status", max_length=1, choices=Status.choices)
    age = models.IntegerField(verbose_name=u"年龄", blank=True, null=True)
    sex = models.CharField(verbose_name=u"性别", max_length=10, blank=True, null=True, choices=SEX)

    class Meta:
        verbose_name = "任务"
        verbose_name_plural = "任务"

    def __str__(self):
        return self.name
