from rest_framework import routers
from .viewsets import UploadViewset

router = routers.DefaultRouter()
router.register('upload', UploadViewset, basename='upload')