from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    msg = response.data
    if response.status_code == 401:
        msg = 'O token fornecido não é válido para nenhum tipo de token.'

    if response is not None:
        response = Response({
            'status': response.status_code,
            'message': msg
        }, status = response.status_code)

    return response


class BaseViewSet(viewsets.ModelViewSet):

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)

        return Response({
            'status': status.HTTP_200_OK,
            'message': 'OK',
            'data': serializer.data
        })
