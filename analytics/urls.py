from django.urls import path
from .views import GetAnalyticsData, AddAnalyticsData

urlpatterns = [
    path('get/', GetAnalyticsData.as_view(), name='get-analytics-data'),
    path('add/', AddAnalyticsData.as_view(), name='add-analytics-data'),
]
