from django import template
from django.utils.http import urlencode
from goods.models import Categories

#Регистрируем функции которые будут работать в шаблоне как шаблонный тег
register = template.Library()


@register.simple_tag()
def tag_categories():
    return Categories.objects.all()


#Чтобы пагинация работала с примененными фильтрами
@register.simple_tag(takes_context=True)
def change_params(context, **kwargs):
    query = context['request'].GET.dict()
    query.update(kwargs)
    return urlencode(query)
