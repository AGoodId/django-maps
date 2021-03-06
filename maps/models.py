from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _

from . import geocode


class GMap(models.Model):
  """Model for storing geocoded data for a given address string
  """
  address = models.CharField(_('Address'), max_length=255, unique=True)
  formatted_address = models.CharField(_('Formatted address'), max_length=255, blank=True)
  latitude = models.FloatField(_('Latitude'), blank=True)
  longitude = models.FloatField(_('Longitude'), blank=True)
  geocode_error = models.BooleanField(_('Geocode error'), default=False)
  geocode_error_message = models.CharField(_('Error message'), max_length=255, blank=True)

  class Meta:
    verbose_name = _("Google Map Address")
    verbose_name_plural = _("Google Map Addresses")

  def __unicode__(self):
    return self.address

  def save(self, *args, **kwargs):
    # fill geocode data if it is unknown
    if not self.longitude or not self.latitude:
      self.geocode()
    super(GMap, self).save(*args, **kwargs)

  def geocode(self):
    """Looks up an address string using a geocoding function
    """
    if not self.address:
      self.geocode_error = True
      return

    g_func = getattr(settings, "MAPS_GEOCODE_FUNCTION", geocode.google_v3)

    try:
      formatted_address, (latitude, longitude,) = g_func(self.address)
    except geocode.Error as e:
      try:
        self.geocode_error, self.geocode_error_message = True, e.msg
      except AttributeError:
        self.geocode_error, self.geocode_error_message = True, ''
      formatted_address, latitude, longitude = '', 0, 0
    else:
      self.geocode_error = False

    self.formatted_address = formatted_address if formatted_address else ''
    self.latitude = latitude if latitude else 0
    self.longitude = longitude if longitude else 0

    return

