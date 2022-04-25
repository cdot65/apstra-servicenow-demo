"""Filter plugin to cleanup blueprint health response."""


class FilterModule(object):
    """Cleaning up blueprint health response."""

    def filters(self):
        """Add our filter plugin to the list of built-in plugins."""
        return {
            "cleanup_vlan_name": self.cleanup_vlan_name,
        }

    def cleanup_vlan_name(self, vlan_name):
        """Filter out filler from the response of our blueprint health."""

        vlan_name = vlan_name.replace(" ", "_")
        vlan_name = vlan_name.upper()

        return vlan_name
