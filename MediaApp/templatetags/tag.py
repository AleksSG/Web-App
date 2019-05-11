from django import template
from MediaApp.models import UserProfileInfo

register = template.Library()

@register.simple_tag
def isOwner(user, comment):
    user = UserProfileInfo.objects.filter(user = user).first()
    print(user)
    print(comment)
    return True
