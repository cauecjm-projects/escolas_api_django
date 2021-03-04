from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework import status


DEFAULT_PAGE = 1
DEFAULT_PAGE_SIZE = 20

class CustomPagination(PageNumberPagination):
    page = DEFAULT_PAGE
    page_size = DEFAULT_PAGE_SIZE
    page_size_query_param = 'page_size'

    def get_paginated_response(self, data):
        return Response({
            'status': status.HTTP_200_OK,
            'message': 'OK',
            'total': self.page.paginator.count,
            'total_pages': self.page.paginator.num_pages,
            'current_page': self.page.number,
            'total_current_page': len(data),
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'data': data
        })