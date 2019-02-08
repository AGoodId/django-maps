from django.conf import settings
from django.utils.encoding import smart_str

from geopy import geocoders
from geopy.exc import GeocoderQueryError


class Error(Exception):
  pass


def google_v3(address):
  """Given an address, return ``(computed_address, (latitude, longitude))``
  tuple using Google Geocoding API v3.
  """
  gm_key = getattr(settings, "GMAP_KEY", None)
  g = geocoders.GoogleV3(api_key=gm_key)
  address = smart_str(address)
  try:
    g_result = g.geocode(address, exactly_one=False)[0]
  except (UnboundLocalError, ValueError, GeocoderQueryError) as e:
    raise Error(e)
  
  return g_result
