"""Filter plugin to find the root cause of an issue."""


class FilterModule(object):
    """Find any anomolies that have a root cause."""

    def filters(self):
        """Add our filter plugin to the list of built-in plugins."""
        return {
            "retrieve_root_cause_info": self.retrieve_root_cause_info,
        }

    def retrieve_root_cause_info(self, root_cause_information):
        """Find the root causes of any existing issues."""
        root_causes = []

        if isinstance(root_cause_information, list):
            for each in root_cause_information:
                root_causes.append(each["description"])

        return root_causes
