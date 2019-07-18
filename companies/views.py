from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Stock
from .serializers import StockSerializer
from django.shortcuts import render

#Lists all stocks or create a new one

class StockList(APIView):

    def get(self, request):
        #print(Stock.objects.all())
        stocks = Stock.objects.all()
        serializer = StockSerializer(stocks, many=True)
        return Response(serializer.data)

    def post(self, request):
        print('asd')
        print(Stock.objects.all())
        stocks = Stock.objects.all()
        serializer = StockSerializer(stocks, many=True)
        return Response(serializer.data)



def post_list(request):
    stocks = Stock.objects.all()
    return render(request, 'post_list.html', {'stocks':stocks})
