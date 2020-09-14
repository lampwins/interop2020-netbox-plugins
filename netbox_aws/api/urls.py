from utilities.api import OrderedDefaultRouter
from netbox_aws.api import views


router = OrderedDefaultRouter()
router.APIRootView = views.AWSRootView

# VPCs
router.register('vpcs', views.VPCViewSet)

app_name = 'netbox_aws-api'
urlpatterns = router.urls
