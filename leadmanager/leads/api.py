from leads.models import Lead
from rest_framework import viewsets, permissions
from .serializers import LeadSerializers


#Lead viewset
class LeadViewSet(viewsets.ModelViewSet):
    queryset = Lead.objects.all()
    permission_class =[
        permissions.AllowAny
    ]
    serializer_class=LeadSerializers
