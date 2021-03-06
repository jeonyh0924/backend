from rest_framework import mixins
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from goods.models import Goods, Type
from goods.serializers import GoodsSerializers


class GoodsViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, GenericViewSet):
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializers

    def get_queryset(self):

        if self.request.query_params.get('category'):
            category = self.request.query_params['category']
            qs = Goods.objects.filter(category__name=category)
        elif self.request.query_params.get('type'):
            type_name = self.request.query_params['type']
            type_ins = Type.objects.filter(name=type_name)[0]
            qs = Goods.objects.filter(types__type__pk=type_ins.pk)
        else:
            qs = super().get_queryset()
        return qs

