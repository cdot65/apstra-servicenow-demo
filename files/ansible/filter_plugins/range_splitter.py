"""Filter plugin to cleanup the ranges entered by ServiceNow."""


class FilterModule(object):
    """Cleaning up the data passed as a range."""

    def filters(self):
        """Add our filter plugin to the list of built-in plugins."""
        return {
            "range_splitter": self.range_splitter,
        }

    def range_splitter(self, asn_range):
        """Create a dictionary and return the first and last within a range."""
        range_split = {}
        range_split["first"] = ""
        range_split["last"] = ""

        if isinstance(asn_range, str):
            asn_range = asn_range.split("-")
            range_split["first"] = asn_range[0]
            range_split["last"] = asn_range[1]

        return range_split
