from users.serializers import CreateUserSerializer


def jwt_response_payload_handler(token, user=None, request=None):
    return {
        'token': token,
        'user': CreateUserSerializer(user, context={'request': request}).data
    }
