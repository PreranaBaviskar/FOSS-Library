
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import contributorSerializer
from .models import contributor

def index(request):
    return render(request, 'index.html')

def act(request):

    if request.method== 'POST':
        print("Submission done")
        month = request.POST["month"]
        series_name = request.POST["series"]
        Date1 = request.POST["Date1"]
        Date2 = request.POST["Date2"]
        Date3 = request.POST["Date3"]
        Date4 = request.POST["Date4"]
        Date5 = request.POST["Date5"]
        Date6 = request.POST["Date6"]
        Date7 = request.POST["Date7"]
        Date8 = request.POST["Date8"]
        Date9 = request.POST["Date9"]
        Date10 = request.POST["Date10"]



        months = {"January": "01" , "February":"02", "March":"03", "April":"04", "May":"05", "June":"06", "July":"07", "August":"08", "September":"09", "October":"10", "November":"11", "December":"12"}

        for key,value in months.items():
            if month==key:
                month_value = value

        count = 0
        date_list = [Date1, Date2, Date3, Date4, Date5, Date6, Date7, Date8, Date9, Date10]

        for obj in date_list:
            print(obj)
            if obj[5:7]==month_value:
                count = count + 1

        count = count * 1000

        info = contributor( foss=series_name, date1=Date1, date2=Date2, date3=Date3, date4=Date4, date5=Date5, date6=Date6, date7=Date7, date8=Date8, date9=Date9, date10=Date10, payment = count)
        info.save()

        return render(request, 'index.html')



class contributorList(APIView):

    def get(self, request):
        contrib = contributor.objects.all()
        serializer = contributorSerializer(contrib, many=True)
        return JsonResponse(serializer.data, safe=False)

# Create your views here.

