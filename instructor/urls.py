from django.urls import path
from instructor.views import instructor


urlpatterns = [
    path('', instructor, name='instructor'),
]