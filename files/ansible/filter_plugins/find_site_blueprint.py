"""Filter plugin to find a site's blueprint."""


class FilterModule(object):
    """Cleaning up the list of blueprints."""

    def filters(self):
        """Add our filter plugin to the list of built-in plugins."""
        return {
            "find_site_blueprint": self.find_site_blueprint,
        }

    def find_site_blueprint(self, nautobot_blueprints, blueprint_name):
        """Looking for an existing blueprint that matches the parameters."""
        blueprint_information = str()

        if isinstance(nautobot_blueprints, list):
            for item in nautobot_blueprints:
                if item["name"] == blueprint_name:
                    blueprint_information = item

        return blueprint_information
