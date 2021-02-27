from rest_framework.renderers import JSONRenderer


class CustomRenderer(JSONRenderer):

    def render(self, data, accepted_media_type=None, renderer_context=None):
        status_code = renderer_context['response'].status_code
        response = {
            'success': True,
            'message': 'Data processed successfully',
            'data': data
        }

        if not str(status_code).startswith('2'):
            response = data

        return super(CustomRenderer, self).render(response, accepted_media_type, renderer_context)