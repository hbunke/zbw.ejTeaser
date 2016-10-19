# from plone.app.textfield import RichText
from plone.supermodel import model
from zope import schema
from plone.namedfile.field import NamedBlobImage
from plone.autoform import directives as form
from plone.app.z3cform.wysiwyg import WysiwygFieldWidget
from plone.formwidget.contenttree import ContentTreeFieldWidget, ObjPathSourceBinder

class ITeaser(model.Schema):

    title = schema.TextLine(
        title=u"Headline",
        required=True
    )
    # RichText does *not* call wysiwig editor automatically, so for now use schema.Text
    # and WysiwygFieldWidget
    form.widget('teasertext', WysiwygFieldWidget)
    teasertext = schema.Text(
        title=u"Teaser Text",
        required=True
    )

    picture = NamedBlobImage(
        title=u"Teaser Image",
        required=True
    )

    caption = schema.TextLine(
        title=u"Image Caption",
        description=u"Add image description or copyright info here (not required)",
        required=False,
    )


    # form.widget('url', ContentTreeFieldWidget)
    # url = schema.Choice(
    #     title=u"URL",
    #     required=False,
    #     source=ObjPathSourceBinder(portal_type=['JournalPaper', 'DiscussionPaper'])
    # )

    url = schema.TextLine(
        title=u"URL",
        description=u"Please add the *full* address of the referenced article/page",
        required=True
    )
