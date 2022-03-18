try {
    var r = new sn_ws.RESTMessageV2("Apstra_Blueprint_Generator", "Execute");
    r.setStringParameter(
        "blueprint_name",
        current.variables.blueprint_name.toString()
    );
    r.setStringParameter(
        "resources_ippool_leaf",
        current.variables.resources_ippool_leaf.toString()
    );
    r.setStringParameter(
        "resources_ippool_spine",
        current.variables.resources_ippool_spine.toString()
    );
    r.setStringParameter(
        "resources_ippool_fabric",
        current.variables.resources_ippool_fabric.toString()
    );
    r.setStringParameter(
        "resources_asn_leaf",
        current.variables.resources_asn_leaf.toString()
    );
    r.setStringParameter(
        "resources_asn_spine",
        current.variables.resources_asn_spine.toString()
    );
    r.setStringParameter(
        "resources_vni_pool",
        current.variables.resources_vni_pool.toString()
    );
    r.setStringParameter(
        "platform_leaf",
        current.variables.platform_leaf.toString()
    );
    r.setStringParameter(
        "platform_spine",
        current.variables.platform_spine.toString()
    );
    r.setStringParameter(
        "design_template",
        current.variables.design_template.toString()
    );

    var response = r.execute();
    var responseBody = response.getBody();
    var httpStatus = response.getStatusCode();
} catch (ex) {
    var message = ex.message;
}
