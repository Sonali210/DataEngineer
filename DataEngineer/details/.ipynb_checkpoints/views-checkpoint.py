from django.shortcuts import render
from .serializers import Detail6731Serializer
from rest_framework.views import APIView
from rest_framework.response import Response
class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        data1 = Detail6731Serializer.objects.all()
        labels = data1.results.keys
        chartLabel = "my data"
        chartdata = data1.results.values
        data = {
            "labels": labels,
            "chartLabel": chartLabel,
            "chartdata": chartdata,
        }
        return render(request, 'index.html', data)