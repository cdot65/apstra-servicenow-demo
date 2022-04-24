"""Filter plugin to cleanup blueprint health response."""


class FilterModule(object):
    """Cleaning up blueprint health response."""

    def filters(self):
        """Add our filter plugin to the list of built-in plugins."""
        return {
            "cleanup_leaf_ids": self.cleanup_leaf_ids,
        }

    def cleanup_leaf_ids(self, leaf_system_ids):
        """Filter out filler from the response of our blueprint health."""
        leafs = {}

        if isinstance(leaf_system_ids, list):
            for each in leaf_system_ids:
                if each["leaf"]["label"] == "leaf1":
                    leafs["leaf1"] = {}
                    leafs["leaf1"]["hostname"] = each["leaf"]["hostname"]
                    leafs["leaf1"]["id"] = each["leaf"]["id"]
                    leafs["leaf1"]["system_id"] = each["leaf"]["system_id"]
                    leafs["leaf1"]["system_type"] = each["leaf"]["system_type"]
                if each["leaf"]["label"] == "leaf2":
                    leafs["leaf2"] = {}
                    leafs["leaf2"]["hostname"] = each["leaf"]["hostname"]
                    leafs["leaf2"]["id"] = each["leaf"]["id"]
                    leafs["leaf2"]["system_id"] = each["leaf"]["system_id"]
                    leafs["leaf2"]["system_type"] = each["leaf"]["system_type"]
                if each["leaf"]["label"] == "leaf3":
                    leafs["leaf3"] = {}
                    leafs["leaf3"]["hostname"] = each["leaf"]["hostname"]
                    leafs["leaf3"]["id"] = each["leaf"]["id"]
                    leafs["leaf3"]["system_id"] = each["leaf"]["system_id"]
                    leafs["leaf3"]["system_type"] = each["leaf"]["system_type"]

        return leafs
