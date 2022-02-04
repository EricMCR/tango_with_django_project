# -*- coding = utf-8 -*-
# @TIME : 2022/2/4 20:43
# @Author : Eric Ma
# @File : rango_template_tags.py
# @Software : PyCharm

from django import template
from rango.models import Category

register = template.Library()

@register.inclusion_tag('rango/categories.html')
def get_category_list(current_category=None):
    return {'categories': Category.objects.all(),
            'current_category': current_category}