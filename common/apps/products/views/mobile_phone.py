from rest_framework import viewsets
from ..models import MobilePhone
from ..serializers import MobilePhoneModelSerializer
from ...shared.pagination import PageLimitPagination
from ...shared.util import get_exclude_query
from django_filters.rest_framework import DjangoFilterBackend
from ..filters import MobilePhoneFilter


class MobilePhoneModelViewSet(viewsets.ModelViewSet):
    queryset = MobilePhone.objects.all()
    serializer_class = MobilePhoneModelSerializer
    pagination_class = PageLimitPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = MobilePhoneFilter
    # filterset_fields  = '__all__'

    def get_queryset(self):
        ordering = self.request.GET.get('_sort', "id")
        queryset_order = self.queryset.order_by(ordering)
        queryset_exclude = MobilePhone.objects.exclude(
            **get_exclude_query(self.request.GET))
        return queryset_order & queryset_exclude
