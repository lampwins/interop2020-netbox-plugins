from rest_framework.routers import APIRootView
from utilities.api import ModelViewSet

from netbox_aws.models import VPC
from netbox_aws.filters import VPCFilterSet
from netbox_aws.api.serializers import VPCSerializer


class AWSRootView(APIRootView):
    """
    AWS API root view
    """
    def get_view_name(self):
        return 'AWS'


class VPCViewSet(ModelViewSet):
    queryset = VPC.objects.all()
    serializer_class = VPCSerializer
    filterset_class = VPCFilterSet
