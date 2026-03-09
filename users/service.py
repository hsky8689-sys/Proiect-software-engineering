from django.db.models import Q
from socks import method
from threading import Thread

from users.models import User,UserProfileSection

async def create_user():
    await create_user_profile_sections(1)
    return True

async def create_user_profile_sections(user_id):
    return True

async def login_user(request):
    if request.method != method.POST:
        return False
    #..#
    return True

async def get_all_user_profile_sections(user_id,view_hidden=False):
    user = await User.objects.get(id=user_id)
    if user is None:
        return []
    if view_hidden:
        return await UserProfileSection.objects.get(Q(user_id=user_id))
    else:
        return await UserProfileSection.objects.get(Q(user_id=user_id)|Q(hidden=False))
