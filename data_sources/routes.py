from data_sources.views import PosseView, GatewayView, GatewayTagsView, GatewayStatusView


posse_list = PosseView.as_view({
    'get': 'list'
})

posse_retrieve = PosseView.as_view({
    'get': 'retrieve'
})

gateway_list = GatewayView.as_view({
    'get': 'list'
})

gateway_retrieve = GatewayView.as_view({
    'get': 'retrieve'
})

gateway_tag_list = GatewayTagsView.as_view({
    'get': 'list'
})

gateway_tag_retrieve = GatewayTagsView.as_view({
    'get': 'retrieve'
})

gateway_status_list = GatewayStatusView.as_view({
    'get': 'list'
})

gateway_status_retrieve = GatewayStatusView.as_view({
    'get': 'retrieve'
})
