# Api Documentation

This is a very simple API and hopefully easy to understand as almost all patterns to fetch the data resources follow the same pattern.

The resources are the following:
- Gateways ( /api/gateways )
- Status ( /api/status )
- Tags ( /api/tags )
- Posses ( api/posses )

All [GET] requests to a resource requesting just the resource basename (api/resource-name) will return a listing of all records available.

Whenever we want to delete [DELETE], partially update [PUT], or retrieve [GET] a single resource element we can do this by calling the resource alongside its id (api/resource-name/id) > /api/tags/1

*Gateway Resource Extra Features*

As models are related it is handy to have a couple of shortcuts to get related data more intuitively, so the following methods are added:

- Tags: to get all the tags related to a Gateway resource the Gateways resource also provides the [GET] /tags option which will list all GatewayTags related to a specific Gateway resource record, it must be used in the following way (/api/gateways/id/tags)
- Dataflow: we can make use of the dataflow property which uses the relation with the GatewayStatus resource, so we can retrieve the latests status for our Gateway with the [GET] /dataflow option which returns a boolean value and must be used in the following way (/api/gateways/id/dataflow)

