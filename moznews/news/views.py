from django.shortcuts import render

from moznews.news.models import Item


def main(request):
    items = Item.scored().order_by('-score')
