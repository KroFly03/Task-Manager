from urllib.parse import urlencode

from django.urls import reverse


def get_url(base_url, entity_id=None, *args, **kwargs):
    if entity_id:
        url = reverse(base_url, args=[entity_id])
    else:
        url = reverse(base_url)

    if kwargs:
        query = urlencode(kwargs, doseq=True)
        url += f'?{query}'

    return url
