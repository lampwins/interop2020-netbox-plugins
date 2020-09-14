try:
    from extras.plugins import PluginConfig
except ImportError:
    # Importing outside of a NetBox install
    class PluginConfig:
        pass


class AWSConfig(PluginConfig):
    """
    This class defines attributes for the NetBox AWS plugin.
    """
    # Plugin package name
    name = 'netbox_aws'

    # Human-friendly name and description
    verbose_name = 'AWS Resources'
    description = 'A plugin for tracking AWS resources'

    # Plugin version
    version = '1.0.0'

    # Plugin author
    author = 'John Anderson'
    author_email = 'lampwins@gmail.com'

    # Configuration parameters that MUST be defined by the user (if any)
    required_settings = []

    # Default configuration parameter values, if not set by the user
    default_settings = {}

    # Base URL path. If not set, the plugin name will be used.
    base_url = 'aws'

    # Caching config
    caching_config = {}


config = AWSConfig
