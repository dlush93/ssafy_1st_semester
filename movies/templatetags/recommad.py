import hashlib
from django import template
from ..models import Genre
register = template.Library()

@register.filter
def recommand_ge(num):
    genres = Genre.objects.all()
    # context=[]
    # for i in genres:
    #     temp={}
    #     temp['id']=i.id
    #     temp['name']=i.name
    #     context.append(temp)
    context = {
        'genres':genres
    }
    return context
