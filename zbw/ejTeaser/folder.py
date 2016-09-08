from plone.supermodel import model
from zope import schema


class ITeaserFolder(model.Schema):

    title = schema.TextLine(
        title=u"Headline"
    )

    description = schema.Text(
        title=u"Description"
    )
