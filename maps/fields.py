from django.db.models.fields import CharField
from django.utils.translation import ugettext_lazy as _

from .widgets import GMapInput


class GMapField(CharField):
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
