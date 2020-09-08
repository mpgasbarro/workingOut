from django.db import models

# Create your models here.
class Workout(models.Model):
    exercise = models.CharField(max_length=100)
    muscleGroupOne = models.CharField(max_length=200)
    muscleGroupTwo = models.CharField(max_length=200)
    muscleGroupThree = models.CharField(max_length=200)
    levelOfDifficulty = models.CharField(max_length=100)
    workout_img = models.TextField()
    workout_url = models.TextField()
    description = models.CharField(max_length=400)

    def __str__(self):
        return f'{self.exercise}, {self.muscleGroupOne}, {self.muscleGroupTwo}, {self.muscleGroupThree}, {self.levelOfDifficulty}, {self.workout_img}, {self.workout_url}, {self.description}'