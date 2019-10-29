from django.urls import path, include
from .views import TestApiList, TestApiDetail
from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register('test', TestViewSet)

urlpatterns = [
    path('test/', TestApiList.as_view()),
    path('test/<int:pk>/', TestApiDetail.as_view()),
    # path('router/', include(router.urls)),
]
