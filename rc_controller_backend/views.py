import json
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.db import connection
from django.http import FileResponse, HttpResponse, JsonResponse


# Create your views here.
@csrf_exempt
def getData(request):
    if request.method == 'GET':
        status = "Enable"
        with connection.cursor() as cursor_1:
            cursor_1.execute("SELECT Command FROM car1 inner join carstatus on car1.DeviceId = carstatus.DeviceId where carstatus.status = '" +
                             str(status) + "' ORDER BY Serial DESC LIMIT 1")
            row1 = cursor_1.fetchone()
            if row1 == None:
                return HttpResponse("", content_type="application/json")
            else:
                response_data = {}
                response_data['result'] = row1[0]
                json_data = json.dumps(response_data)
                return HttpResponse(json_data, content_type="application/json")


@csrf_exempt
def writeData(request):
    if request.method == 'POST':
        deviceID = request.POST.get("deviceID", False)
        command = request.POST.get("command", False)
        with connection.cursor() as cursor_1:
            cursor_1.execute("INSERT INTO car1(DeviceId,Command) VALUES ('"+str(deviceID) + "','"+str(command) + "')")
            connection.commit()
          

        return HttpResponse("", content_type="application/json")

@csrf_exempt
def writeStatus(request):
    if request.method == 'POST':
        deviceID = request.POST.get("deviceID", False)
        status = request.POST.get("status", False)
        with connection.cursor() as cursor_1:
            cursor_1.execute("INSERT INTO carstatus(DeviceId,status) VALUES ('"+str(deviceID) + "','"+str(status) + "')")
            connection.commit()
          

        return HttpResponse("", content_type="application/json")

@csrf_exempt
def updateStatus(request):
    if request.method == 'POST':
        deviceID = request.POST.get("deviceID", False)
        status = request.POST.get("status", False)
        with connection.cursor() as cursor_1:
            cursor_1.execute("update carstatus set status='"+str(status) + "' where DeviceId = '"+str(deviceID) + "'")
            connection.commit()
          

        return HttpResponse("", content_type="application/json")
