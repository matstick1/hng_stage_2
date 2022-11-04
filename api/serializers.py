from rest_framework import serializers

OPERATION_TYPE_CHOICES = (
    ('addition', 'addition'),
    ('subtraction', 'subtraction'),
    ('multiplication','multiplication')
)

class SimpleCaseSerializer(serializers.Serializer):
    operation_type = serializers.ChoiceField(choices=OPERATION_TYPE_CHOICES)
    x = serializers.IntegerField()
    y = serializers.IntegerField()


class ComplexCaseSeializer(serializers.Serializer):
    operation_type = serializers.CharField(max_length=300)