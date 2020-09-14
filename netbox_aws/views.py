from django.shortcuts import get_object_or_404, render
from utilities.views import ObjectEditView, ObjectListView, ObjectDeleteView, ObjectView

from netbox_aws import forms, filters, tables
from netbox_aws.models import VPC


class VPCEditView(ObjectEditView):
    queryset = VPC.objects.all()
    model_form = forms.VPCForm


class VPCListView(ObjectListView):
    queryset = VPC.objects.all()
    filterset = filters.VPCFilterSet
    filterset_form = forms.VPCFilterForm
    table = tables.VPCTable
    action_buttons = ('add', 'export')
    template_name = 'netbox_aws/vpc_list.html'


class VPCDeleteView(ObjectDeleteView):
    queryset = VPC.objects.all()


class VPCView(ObjectView):
    queryset = VPC.objects.all()

    def get(self, request, slug):

        vpc = get_object_or_404(self.queryset, slug=slug)

        return render(request, 'netbox_aws/vpc.html', {
            'vpc': vpc,
        })
