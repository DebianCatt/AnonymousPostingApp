import uuid


COOKIE_NAME = 'anonymous_owner_id'


def get_or_create_owner_id(request):
    owner_id = request.COOKIES.get(COOKIE_NAME)

    if owner_id is None:
        owner_id = str(uuid.uuid4())

    return owner_id