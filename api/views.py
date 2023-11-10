from django.shortcuts import render
from .serializers import *
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .models import Plant, Species, Feedback
from rest_framework.generics import UpdateAPIView, CreateAPIView, ListAPIView


class PlantViewSet(ModelViewSet):
    queryset = Plant.objects.all().order_by('interest')
    serializer_class = PlantListSerializer

    def get_queryset(self):
        return Plant.objects.all().select_related('species').prefetch_related('feedback_set')

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        feedback = instance.feedback_set.all()
        species = instance.species
        dataDict = {
            'plant': instance,
            'feedback': feedback,
            'species': species,
        }
        serializers = PlantRetrieveSerializer(dataDict).data
        return Response(serializers)

    def interest(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.interest += 1
        instance.save()


class SpeciesViewSet(ListAPIView):
    queryset = Species.objects.all()
    serializer_class = SpeciesSerializer


class WateringViewset(UpdateAPIView):
    queryset = Plant.objects.all()
    serializer_class = WateringSerializer


class FeedbackViewset(CreateAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer


class HumidityViewset(UpdateAPIView):
    queryset = Plant.objects.all()
    serializer_class = HumiditySerializer
