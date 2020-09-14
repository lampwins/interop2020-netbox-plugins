from extras.plugins import PluginTemplateExtension

from netbox_aws.models import VPC


class PrefixVPC(PluginTemplateExtension):
    """
    Extend the IPAM prefix page to show a link to the VPC for which the given
    prefix is linked.
    """
    model = 'ipam.prefix'

    def right_page(self):
        return self.render('netbox_aws/prefix_right.html')


# PluginTemplateExtension subclasses must be packaged into an iterable named
# template_extensions to be imported by NetBox.
template_extensions = [PrefixVPC]
