from rest_framework import serializers
from utilities.api import ChoiceField, ValidatedModelSerializer
from ipam.api.nested_serializers import NestedPrefixSerializer

from netbox_aws.choices import VPCRegionChoices
from netbox_aws.models import VPC


class VPCSerializer(ValidatedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='plugins-api:netbox_aws-api:vpc-detail')
    region = ChoiceField(choices=VPCRegionChoices)
    container_prefix = NestedPrefixSerializer()

    class Meta:
        model = VPC
        fields = [
            'id', 'url', 'name', 'slug', 'description', 'region', 'container_prefix',
            'created', 'last_updated',
        ]
