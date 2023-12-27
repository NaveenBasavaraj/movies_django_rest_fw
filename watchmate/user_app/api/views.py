from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.decorators import api_view
from user_app.api.serializers import RegistrationSerializers

@api_view(['POST,'])
def registration_view(request):
    if request.method == 'POST':
        serializer = RegistrationSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return serializer.data
        