from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('', my_view, name='home'),
    path('success/', SuccessPageView.as_view(), name='success_page'),
    # path('maintenance/', maintenance_page, name='maintenance'),
    # path('404/', custom_404_view, name='404_error'),
]
