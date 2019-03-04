from django import template
from django.conf import settings

from maps.models import GMap

register = template.Library()


@register.inclusion_tag('maps/gmap.html')
def google_map(*addresses, **kwargs):
  gm_key = getattr(settings, "GMAP_KEY", None)
  api_key=gm_key
  maps = GMap.objects.filter(address__in=addresses)
  markers = [("%f" % m.latitude, "%f" % m.longitude) for m in maps]
  map_uid = str(abs(hash(addresses)))
  width, height, zoom = "100%", 400, 14
  context = locals()
  context.update(**kwargs)
  return context
