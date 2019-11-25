def get_id(request, backend, strategy, details, response, user=None, *args, **kwargs):
    url = None
    if backend.name == 'google-oauth2':
        try:
            url = response["id"]
        except KeyError:
            url = response['id'].get('url')
