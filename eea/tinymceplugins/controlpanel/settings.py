""" Control Panel
"""
from zope.component import queryUtility
from zope.interface import implements
from zope.formlib import form
from plone.app.controlpanel.form import ControlPanelForm
from plone.registry.interfaces import IRegistry
from Products.CMFDefault.formlib.schema import SchemaAdapterBase
from eea.tinymceplugins.interfaces import ISettings
from eea.tinymceplugins.config import EEAMessageFactory as _

class ControlPanel(ControlPanelForm):
    """ API
    """
    form_fields = form.FormFields(ISettings)
    label = _(u"EEA TinyMCE Plugins Settings")
    description = _(u"EEA TinyMCE Plugins settings")
    form_name = _(u"EEA TinyMCE Plugins settings")

class ControlPanelAdapter(SchemaAdapterBase):
    """ Form adapter
    """
    implements(ISettings)

    def __init__(self, context):
        super(ControlPanelAdapter, self).__init__(context)
        self._settings = None

    @property
    def settings(self):
        """ Settings
        """
        if self._settings is None:
            self._settings = queryUtility(
                IRegistry).forInterface(ISettings, False)
        return self._settings

    @property
    def charCountCTypes(self):
        """ Get charCountCTypes
        """
        name = u"charCountCTypes"
        return getattr(self.settings, name, ISettings[name].default)

    @charCountCTypes.setter
    def charCountCTypes(self, value):
        """ Set charCountCTypes
        """
        self.settings.charCountCTypes = value
