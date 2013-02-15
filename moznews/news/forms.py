from django import forms

from moznews.news.models import Item


class NewItemForm(forms.ModelForm):
    fields = ('title', 'url')

    class Meta(object):
        model = Item


class CommentForm(forms.ModelForm):
    fields = ('text', 'in_reply_to')

    class Meta(object):
        model = Item
