from django.db.models.fields import CharField
from django.utils.translation import ugettext_lazy as _

from .models import GMap
from .widgets import GMapInput


class GMapField(CharField):
  """Custom field for Google Maps integration that ensures a GMap object
  is created for each new address string.
  """

  description = _("An address")

  def __init__(self, *args, **kwargs):
    if 'max_length' in kwargs:
      self.max_length = kwargs['max_length']
    else:
      self.max_length = 255
      kwargs.update({'max_length': self.max_length})      
    super(GMapField, self).__init__(*args, **kwargs)

  def get_internal_type(self):
    return "GMapField"

  def pre_save(self, model_instance, add):
    """Create GMap object and call super before saving field data
    """
    value = self.value_from_object(model_instance)
    if value:
      gmap = GMap.objects.get_or_create(address=value)
    return super(GMapField, self).pre_save(model_instance, add)

  def formfield(self, **kwargs):
    defaults = {'max_length': self.max_length,
                'widget': GMapInput}
    defaults.update(kwargs)
    return super(GMapField, self).formfield(**defaults)


# Tell South how to handle GMapFields
try:
  from south.modelsinspector import add_introspection_rules
except ImportError:
  pass
else:
  add_introspection_rules([], ["^maps\.fields\.GMapField"])
