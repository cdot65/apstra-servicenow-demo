class FilterModule(object):
    def filters(self):
        return {
            "cleanup_blueprints": self.cleanup_blueprints,
        }

    def cleanup_blueprints(self, output_blueprint_health, blueprint):
        filtered_blueprint = str()

        if isinstance(output_blueprint_health, list):
            for item in output_blueprint_health:
                if item["id"] == blueprint:
                    filtered_blueprint = item

        return filtered_blueprint
