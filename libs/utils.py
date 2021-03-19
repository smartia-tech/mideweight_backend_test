def is_request_verbose(request):
    """Is the request verbose

    :request -> django's request
    """
    if request:
        return request.GET.get('response') == 'verbose'
