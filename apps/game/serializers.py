from rest_framework import serializers
from .models import Board

class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = '__all__'
#     pk = serializers.IntegerField(read_only=True)
#     column_a = serializers.CharField()
#     column_b = serializers.CharField()
#     column_c = serializers.CharField()
# #
#     def create(self, validated_data):
#         """
#         Create and return a new `Serie` instance, given the validated data.
#         """
#         return Board(**validated_data)

    # def update(self, instance, validated_data):
    #     """
    #     Update and return an existing `Serie` instance, given the validated data.
    #     """
    #     instance.column_a = validated_data.get('column_a',instance.column_a)
    #     instance.column_b = validated_data.get('column_b',instance.column_b)
    #     instance.column_c = validated_data.get('column_c',instance.column_c)
    #     instance.save()
    #     return instance

    # def create(self, validated_data):
    #     instance = Board
    #     instance.column_a = validated_data.get('column_a')
    #     instance.column_b = validated_data.get('column_b')
    #     instance.column_c = validated_data.get('column_c')
    #     return instance
