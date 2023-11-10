from rest_framework import serializers
from .models import Plant, Species, Feedback
from django.db.models import Count, Q
from django.utils import timezone
from datetime import timedelta


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        exclude = ['created_at']


class PlantListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plant
        fields = ['nickname', 'image', 'interest']


class PlantRetrieveSubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plant
        fields = ['nickname', 'image', 'species',
                  'interest', 'humidity', 'watering']


class FeedbackRetrieveSubSerializer(serializers.ModelSerializer):
    grow_well_count = serializers.SerializerMethodField()
    too_many_bugs_count = serializers.SerializerMethodField()
    leaves_dying_count = serializers.SerializerMethodField()
    another_problem_count = serializers.SerializerMethodField()

    class Meta:
        model = Feedback
        fields = ['grow_well_count', 'too_many_bugs_count',
                  'leaves_dying_count', 'another_problem_count']

    def get_grow_well_count(self, obj):
        # obj는 Feedback 모델의 인스턴스입니다.
        # obj와 연결된 Plant의 Feedback 중 grow_well이 True인 개수를 반환합니다.
        return Feedback.objects.filter(grow_well=True).count()

    def get_too_many_bugs_count(self, obj):
        # .filter(created_at=(timezone.now() - timedelta(weeks=1)))
        return Feedback.objects.filter(too_many_bugs=True).count()

    def get_leaves_dying_count(self, obj):
        # .filter(created_at=(timezone.now() - timedelta(weeks=1)))
        return Feedback.objects.filter(leaves_dying=True).count()

    def get_another_problem_count(self, obj):
        # .filter(created_at=(timezone.now() - timedelta(weeks=1)))
        return Feedback.objects.filter(another_problem=True).count()


class SpeciesRetrieveSubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Species
        fields = ['good_humidity']


class PlantRetrieveSerializer(serializers.Serializer):
    plant = PlantRetrieveSubSerializer()
    feedback = FeedbackRetrieveSubSerializer()
    species = SpeciesRetrieveSubSerializer()


class WateringSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plant
        fields = ['watering']


class HumiditySerializer(serializers.ModelSerializer):
    class Meta:
        model = Plant
        fields = ['humidity']


class SpeciesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Species
        fields = ['name', 'content']
