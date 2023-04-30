from django import template
register=template.Library()

def swap(value):
    return value.swapcase()


def remove(value,arg):
    for i in range(len(value)):
        return value.replace(arg,'')
    

@register.filter()
def count(value,arg):
    c=0
    for i in range(len(value)):
        if value[i:i+len(arg)]==arg:
            c+=1
    return c
#register.filter('count',count)
register.filter('replacing',remove)
register.filter('swapping',swap)