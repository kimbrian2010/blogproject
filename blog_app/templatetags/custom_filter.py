from django import template


register = template.Library()


def range_filter(value):
    return value[0:500] +"..." #the number of characters to return in a paragraph

register.filter('range_filter',range_filter)