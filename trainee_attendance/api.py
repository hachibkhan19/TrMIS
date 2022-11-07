from django.shortcuts import render, HttpResponse
from batch.models import Batch
from rest_framework.views import APIView
import json
from rest_framework.response import Response

# Create your views here.
class BatchApiView(APIView):
    def get(self, request):
        with open ("/home/hachib-inneed/Desktop/trmis_backend/TrMIS/trainee_attendance/data_file/trainee.json") as trainee_data:
            trainee_datas = json.load(trainee_data)
        with open("/home/hachib-inneed/Desktop/trmis_backend/TrMIS/trainee_attendance/data_file/data.json") as data_file:
            datas = json.load(data_file)
            for data in datas:
                for index, value in enumerate(data["attendence"]):
                    data["day_{}".format(index + 1)] = True if value ==  1 else False
                data["trainees"] = [item for item in trainee_datas if item["id"] == data['trainee_id']][0]
                del data['attendence']
        return Response(datas)
