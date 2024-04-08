from rest_framework import serializers
from .models import item


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model=item
        fields=['item_name','item_desc','item_image','item_price']