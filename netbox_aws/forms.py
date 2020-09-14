from django import forms
from utilities.forms import (
    BootstrapMixin, StaticSelect2, StaticSelect2Multiple, DynamicModelMultipleChoiceField,
    DynamicModelChoiceField, SlugField
)
from ipam.models import Prefix

from netbox_aws.choices import VPCRegionChoices
from netbox_aws.models import VPC


class VPCForm(BootstrapMixin, forms.ModelForm):
    container_prefix = DynamicModelChoiceField(
        queryset=Prefix.objects.all(),
        display_field='prefix'
    )
    slug = SlugField()
    description = forms.CharField(
        required=False,
    )

    class Meta:
        model = VPC
        fields = [
            'name', 'slug', 'description', 'region', 'container_prefix'
        ]
        widgets = {
            'region': StaticSelect2(),
        }


class VPCFilterForm(BootstrapMixin, forms.Form):
    model = VPC
    field_order = ['q', 'name', 'description', 'region', 'container_prefix']
    q = forms.CharField(
        required=False,
        label='Search'
    )
    name = forms.CharField(
        required=False,
    )
    description = forms.CharField(
        required=False,
    )
    region = forms.MultipleChoiceField(
        choices=VPCRegionChoices,
        required=False,
        widget=StaticSelect2Multiple()
    )
    container_prefix = DynamicModelMultipleChoiceField(
        queryset=Prefix.objects.all(),
        to_field_name='prefix',
        required=False
    )
