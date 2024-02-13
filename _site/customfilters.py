from django.template.defaulttags import register

@register.filter(name="get_item")
def get_item(dictionary, key):
    return dictionary.get(key)

@register.filter(name="contains")
def contains(list, element):
    return element in list

@register.filter(name="toHashnodeTag")
def contains(string):
    return string.lower().replace(" ", "-")
