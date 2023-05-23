from extras.plugins import PluginConfig

class NetboxConfigElements(PluginConfig):
    name = 'netbox_device_elements'
    verbose_name = 'Netbox Device Elements'
    description = 'A plugin for NetBox that adds in additional router/switch config elements'
    version = '0.1'
    author = 'Aaron Roth'
    author_email = 'aroth01@gmail.com'
    base_url = 'config-elements'
    required_settings = []

config = NetboxConfigElements