from django.urls import path

from netbox_aws import views


urlpatterns = [
    path('vpcs/', views.VPCListView.as_view(), name='vpc_list'),
    path('vpcs/add/', views.VPCEditView.as_view(), name='vpc_add'),
    path('vpcs/<slug:slug>/', views.VPCView.as_view(), name='vpc'),
    path('vpcs/<slug:slug>/edit/', views.VPCEditView.as_view(), name='vpc_edit'),
    path('vpcs/<slug:slug>/delete/', views.VPCDeleteView.as_view(), name='vpc_delete'),
]
