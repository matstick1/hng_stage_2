from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import SimpleCaseSerializer, ComplexCaseSeializer
from .helper import get_openai


class CalculatorView(APIView):
    serializer_class = SimpleCaseSerializer

    def post(self, request):
        complex_serializer = ComplexCaseSeializer(data=request.data)
        if complex_serializer.is_valid():
            operation_type = complex_serializer.validated_data.get(
                'operation_type')
            if operation_type != "addition" and operation_type != "subtraction" and operation_type != "multiplication":
                try:
                    result = get_openai(operation_type)
                    result = [int(s) for s in result.split() if s.isdigit()]
                    result = result[len(result) - 1]
                    response = {"operation_type": operation_type,
                                "result": result, "slackUsername": "matstick"}
                    return Response(response)
                except IndexError:
                    print("oopsss you made an invalide entry")

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        operation_type = serializer.validated_data.get('operation_type')
        x = serializer.validated_data.get('x')
        y = serializer.validated_data.get('y')

        match operation_type:
            case 'addition':
                result = x + y
            case 'subtraction':
                result = x - y
            case'multiplication':
                result = x * y
        response = {"operation_type": operation_type,
                    "result": result, "slackUsername": "matstick"}
        return Response(response)
