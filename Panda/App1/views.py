from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import pandas as pd
from django.http import JsonResponse
import json
from django.core.serializers import serialize
from rest_framework.pagination import PageNumberPagination


class Get_Practice_data(APIView):
    

    def post(self, request):
        
        paginator_class = PageNumberPagination()

        data = pd.read_csv(r"C:\Users\ADMIN\Desktop\DJANGO_API\Python_Panda\Practice_data.csv")

        data.fillna('', inplace=True)

        data_list = data.to_dict(orient='records')

        print(data_list)

        print("just checking purpose")
        paginated_data = paginator_class.paginate_queryset(data_list, request)

        print(paginated_data)
            
        # return jsonResponse(data=data1)

        return Response(data=paginated_data)