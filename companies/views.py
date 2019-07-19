from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Stock
from .serializers import StockSerializer
from django.shortcuts import render, get_object_or_404, redirect
from .forms import stockForm

#Lists all stocks or create a new one

class StockList(APIView):

    def get(self, request):
        #print(Stock.objects.all())
        stocks = Stock.objects.all()
        serializer = StockSerializer(stocks, many=True)
        return Response(serializer.data)

    def post(self, request):

        serializer = StockSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



def post_list(request):
    stocks = Stock.objects.all()
    return render(request, 'companies/post_list.html', {'stocks':stocks})

def stock_new(request):
    if request.method == "POST":
        form = stockForm(request.POST)
        if form.is_valid():
            stock = form.save(commit=False)
            stock.save()
    else:
        form = stockForm()
    return render(request, 'companies/stock_edit.html', {'form':form})