"""Filter plugin to cleanup vlan configuration."""


class FilterModule(object):
    """Cleaning up vlan config response."""

    def filters(self):
        """Add our filter plugin to the list of built-in plugins."""
        return {
            "cleanup_vlan_config": self.cleanup_vlan_config,
        }

    def cleanup_vlan_config(self, vconfig):
        """Filter out filler from the response of our vlan config.

        Create an empty dictionary `vlan` and fill in spots for our vlan.

        Loop over returned vlan and fill in the goods.
        """
        vlan = {}

        if isinstance(vconfig["items"], list):
            vlan["description"] = vconfig["items"][0]["vlan"]["description"]
            vlan["id"] = vconfig["items"][0]["vlan"]["id"]
            vlan["label"] = vconfig["items"][0]["vlan"]["label"]
            vlan["type"] = vconfig["items"][0]["vlan"]["type"]
            vlan["virtual_gateway_ipv4"] = vconfig["items"][0]["vlan"][
                "virtual_gateway_ipv4"
            ]
            vlan["vn_id"] = vconfig["items"][0]["vlan"]["vn_id"]

        return vlan
