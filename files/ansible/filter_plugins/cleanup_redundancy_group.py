"""Filter plugin to cleanup blueprint health response."""


class FilterModule(object):
    """Cleaning up blueprint health response."""

    def filters(self):
        """Add our filter plugin to the list of built-in plugins."""
        return {
            "cleanup_redundancy_group": self.cleanup_redundancy_group,
        }

    def cleanup_redundancy_group(self, redundancy_group):
        """Filter out filler from the response of our blueprint health."""
        rg = {}

        if isinstance(redundancy_group["items"], list):

            for each in redundancy_group["items"]:
                rg["id"] = each["esi"]["id"]
                rg["rg_type"] = each["esi"]["rg_type"]
                rg["rg_id"] = each["esi"]["rg_id"]
                rg["type"] = each["esi"]["type"]
                rg["label"] = each["esi"]["label"]

        return rg
