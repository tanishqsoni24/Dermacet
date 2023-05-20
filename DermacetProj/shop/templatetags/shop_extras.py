from django import template

register = template.Library()

@register.simple_tag
def getAlert(request):
    alert = request.session.get('alert')
    if alert:
        request.session.pop('alert')
    return alert
