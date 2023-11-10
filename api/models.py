from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


def user_directory_path(instance, filename):
    birthday = instance.birthday.strftime('%Y/%m')
    return '{0}/{1}'.format(birthday, filename)


class Plant(models.Model):
    nickname = models.CharField(max_length=15)
    image = models.ImageField(upload_to=user_directory_path, blank=True)
    species = models.ForeignKey(
        "Species",  on_delete=models.CASCADE, related_name='plants')
    interest = models.PositiveSmallIntegerField(default=0)
    humidity = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)])
    watering = models.IntegerField(validators=[MinValueValidator(0)])
    birthday = models.DateField()

    def __str__(self):
        return self.nickname


class Species(models.Model):
    name = models.CharField(max_length=30)
    good_humidity = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)])
    content = models.TextField()

    def __str__(self):
        return self.name


class Feedback(models.Model):
    plant = models.ForeignKey("Plant",  on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    grow_well = models.BooleanField(default=False, blank=True)
    too_many_bugs = models.BooleanField(default=False, blank=True)
    leaves_dying = models.BooleanField(default=False, blank=True)
    another_problem = models.BooleanField(default=False, blank=True)
