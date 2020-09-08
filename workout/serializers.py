from rest_framework import serializers
from .models import Workout

class WorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workout
        fields = ('id', 'exercise', 'muscleGroupOne', 'muscleGroupTwo', 'muscleGroupThree', 'levelOfDifficulty', 'workout_img', 'workout_url', 'description')
