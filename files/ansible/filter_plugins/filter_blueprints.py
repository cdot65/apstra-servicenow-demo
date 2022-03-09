"""Filter plugin to cleanup blueprint health response."""


class FilterModule(object):
    """Cleaning up blueprint health response."""

    def filters(self):
        """Add our filter plugin to the list of built-in plugins."""
        return {
            "filter_blueprints": self.filter_blueprints,
        }

    def filter_blueprints(self, output_blueprint_health, blueprint):
        """Filter out filler from the response of our blueprint health."""
        filtered_blueprint = str()

        if isinstance(output_blueprint_health, list):
            for item in output_blueprint_health:
                if item["label"] == blueprint:
                    filtered_blueprint = item

        return filtered_blueprint
