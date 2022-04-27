"""Filter plugin to cleanup leaf IDs."""


class FilterModule(object):
    """Cleaning up leaf IDs response."""

    def filters(self):
        """Add our filter plugin to the list of built-in plugins."""
        return {
            "cleanup_endpoint_policy": self.cleanup_endpoint_policy,
        }

    def cleanup_endpoint_policy(self, ct):
        """Filter out filler from the response of our leaf IDs.

        Create an empty dictionary `policy` and fill in spots for our policy.

        Loop over returned policy and fill in the goods.
        """
        policy = {}

        if isinstance(ct["items"], list):
            policy["description"] = ct["items"][0]["policy"]["description"]
            policy["id"] = ct["items"][0]["policy"]["id"]
            policy["label"] = ct["items"][0]["policy"]["label"]
            policy["type"] = ct["items"][0]["policy"]["type"]

        return policy
