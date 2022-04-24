"""Filter plugin to cleanup blueprint health response."""


class FilterModule(object):
    """Cleaning up blueprint health response."""

    def filters(self):
        """Add our filter plugin to the list of built-in plugins."""
        return {
            "cleanup_security_zone": self.cleanup_security_zone,
        }

    def cleanup_security_zone(self, routing_instance):
        """Filter out filler from the response of our blueprint health."""
        security_zone = {}

        if isinstance(routing_instance["items"], list):

            for each in routing_instance["items"]:
                security_zone["id"] = each["security_zone"]["id"]
                security_zone["label"] = each["security_zone"]["label"]
                security_zone["sz_type"] = each["security_zone"]["sz_type"]
                security_zone["type"] = each["security_zone"]["type"]
                security_zone["vlan_id"] = each["security_zone"]["vlan_id"]
                security_zone["vni_id"] = each["security_zone"]["vni_id"]
                security_zone["vrf_name"] = each["security_zone"]["vrf_name"]

        return security_zone
