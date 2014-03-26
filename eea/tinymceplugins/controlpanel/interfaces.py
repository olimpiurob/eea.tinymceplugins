""" Control Panel Interfaces

   >>> portal = layer['portal']
   >>> sandbox = portal['sandbox']

"""
from zope.interface import Interface
from zope import schema
from eea.tinymceplugins.config import EEAMessageFactory as _

class ISettings(Interface):
    """ Settings

        >>> from eea.tinymceplugins.interfaces import ISettings
        >>> ISettings(portal).portalTypes = [u'Document', u'News Item']
        >>> ISettings(portal).portalTypes
        [u'Document', u'News Item']

    """
    charCountCTypes = schema.List(
        title=_(u"Enable character count plugin"),
        description=_(u"Character count plugin is enabled for the "
                      u"following content-types"),
        required=False,
        default=[u"Document"],
        value_type=schema.Choice(
            vocabulary=u"plone.app.vocabularies.ReallyUserFriendlyTypes")
    )
