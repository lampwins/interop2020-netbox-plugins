from extras.plugins import PluginMenuButton, PluginMenuItem
from utilities.choices import ButtonColorChoices


# Declare a list of menu items to be added to NetBox's built-in naivgation menu
menu_items = (

    # Each PluginMenuItem instance renders a custom menu item. Each item may have zero or more buttons.
    PluginMenuItem(
        link='plugins:netbox_aws:vpc_list',
        link_text='VPCs',
        permissions=['netbox_aws.view_vpc'],
        buttons=(

            # Add a green button which links to the admin view to add a new animal. This
            # button will appear only if the user has the "add_animal" permission.
            PluginMenuButton(
                link='plugins:netbox_aws:vpc_add',
                title='Add a new VPC',
                icon_class='fa fa-plus',
                color=ButtonColorChoices.GREEN,
                permissions=['netbox_aws.add_vpc']
            ),
        )
    ),

)
