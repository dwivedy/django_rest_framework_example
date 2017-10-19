from ecommr_home.models import EcommrHomeModle
from rest_framework import serializers

class EcommrHomeSerializer(serializers.ModelSerializer):

    class Meta:
        model = EcommrHomeModle
        fields = ('id','product_name','product_quantity')

