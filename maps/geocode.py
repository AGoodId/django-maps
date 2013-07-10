from django.conf import settings
from django.utils.encoding import smart_str

from geopy import geocoders
from geopy.geocoders.base import GeocoderResultError


class Error(Exception):
  pass


def google_v3(address):
  """Given an address, return ``(computed_address, (latitude, longitude))``
  tuple using Google Geocoding API v3.
  """
  g = geocoders.GoogleV3()
  address = smart_str(address)
  try:
    g_result = g.geocode(address, exactly_one=False)[0]
  except (UnboundLocalError, ValueError, GeocoderResultError) as e:
    raise Error(e)
  
  return g_result
