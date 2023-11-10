from django.urls import path
from .views import *

# router = DefaultRouter()
# router.register(r'plant', PlantViewSet)
# router.register(r'species', SpeciesViewSet)
# router.register(r'feedback', FeedbackViewSet)
urlpatterns = [
    # path('', include(router.urls)),actions={'get': 'list'}
    path('plant/', PlantViewSet.as_view(actions={'get': 'list'})),
    path('plant/<int:pk>/',
         PlantViewSet.as_view(actions={'get': 'retrieve', })),
    path('plant/<int:pk>/interest/',
         PlantViewSet.as_view(actions={'get': 'interest', })),
    path('plant/<int:pk>/watering/',
         WateringViewset.as_view()),
    path('plant/<int:pk>/humidity/', HumidityViewset.as_view()),
    path('feedback/', FeedbackViewset.as_view()),
    path('species/', SpeciesViewSet.as_view()),

]
