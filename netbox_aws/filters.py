import django_filters
from django.db.models import Q
from utilities.filters import BaseFilterSet
from ipam.models import Prefix

from netbox_aws.models import VPC
from netbox_aws.choices import VPCRegionChoices



class VPCFilterSet(BaseFilterSet):
    q = django_filters.CharFilter(
        method='search',
        label='Search',
    )
    region = django_filters.MultipleChoiceFilter(
        choices=VPCRegionChoices,
        null_value=None
    )
    container_prefix_id = django_filters.ModelMultipleChoiceFilter(
        queryset=Prefix.objects.all(),
        label='Prefix (ID)',
    )
    container_prefix = django_filters.ModelMultipleChoiceFilter(
        field_name='container_prefix__prefix',
        queryset=Prefix.objects.all(),
        to_field_name='prefix',
        label='Prefix',
    )

    class Meta:
        model = VPC
        fields = [
            'id', 'name', 'slug', 'description'
        ]

    def search(self, queryset, name, value):
        if not value.strip():
            return queryset
        qs_filter = (
            Q(name__icontains=value) |
            Q(name__icontains=value) |
            Q(description__icontains=value)
        )
        return queryset.filter(qs_filter)
