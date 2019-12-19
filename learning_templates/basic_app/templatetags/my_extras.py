from django import template

register = template.Library()


@register.filter(name="bye")
def bye(value, arg):
    """
    This cuts out all values of "arg" from the string
    """
    return value.replace(arg, "bye")


# register.filter("bye", bye)
