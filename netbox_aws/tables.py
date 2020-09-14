import django_tables2 as tables
from utilities.tables import BaseTable, ToggleColumn

from netbox_aws.models import VPC


class VPCTable(BaseTable):
    pk = ToggleColumn()
    name = tables.LinkColumn()

    class Meta(BaseTable.Meta):
        model = VPC
        fields = (
            'pk', 'name', 'slug', 'region', 'description', 'container_prefix'
        )
        default_columns = ('pk', 'name', 'region', 'container_prefix')
