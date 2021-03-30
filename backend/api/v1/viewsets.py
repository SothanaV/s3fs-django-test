from rest_framework import viewsets
from .serializers import UploadSerializer
from upload.models import Upload

class UploadViewset(viewsets.ModelViewSet):
    serializer_class = UploadSerializer
    model = Upload

    def get_queryset(self):
        return self.model.objects.none()