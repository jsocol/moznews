from django.shortcuts import render

from moznews.news.models import Item


def main(request):
    items = Item.scored().filter(in_reply_to__isnull=True).order_by('-score')
    render(request, 'main.html', {'items': items})
