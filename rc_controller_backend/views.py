import json
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.db import connection
from django.http import FileResponse, HttpResponse, JsonResponse


# Create your views here.
@csrf_exempt
def getData(request):
    with connection.cursor() as cursor_1:
        cursor_1.execute("SELECT tempData FROM mydata ORDER BY ID DESC LIMIT 1")
        row1 = cursor_1.fetchone()
        result = []
        keys = ("mydata")
        result.append(dict(zip(keys, row1)))
        json_data = json.dumps(result)
        print(json_data)
        return HttpResponse(json_data, content_type="application/json")