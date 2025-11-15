from django.http import JsonResponse
from collegedb.models import student
from eventdb.models import events
from eventdb.models import hosts,eventshosts,registrations
from django.shortcuts import render
import requests
api_key="AIzaSyCSujc1mYc-WT47nxhsO265Ydemm31u3jU"



def chatbox(request):
    query=request.GET.get('query')
    payload={
    "contents": [
     {
    "parts": [
          {
            "text": "I want you to act as a experienced technical interviewer interviewing me "
          },
          {"text":query}
    ]
   }
  ]
}
    params={
        "key":api_key
    }
    
    result=requests.post("https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent",
                        params=params,json=payload)
    data=result.json()
    output_text=data["candidates"][0]["content"]["parts"][0]["text"]
    return JsonResponse({"output":output_text})

def chatbot_page(request):
    return render(request,"chatbot.html")
   


def fetch_events(request):
    result=events.objects.all().values()
    #result=events.objects.filter(name="Exhibition").values()

    # result=events.objects.filter(price__gte=6000).values()
   # result=events.objects.filter(host_id=1).values()
    #print(result.values())
   # return JsonResponse(list(result),safe=False)
    return render(request,"events.html",context={"events":list(result)})



def fetch_eventshosts(request):
    result=eventshosts.objects.all().values()
    return JsonResponse(list(result),safe=False)

def fetch_registrations(request):
    result=registrations.objects.all().values()
    return JsonResponse(list(result),safe=False)


def update_event(request):
    name_value=request.GET.get('name')
    price_value=request.GET.get('price')
    desc_value=request.GET.get('desc')
    limit_value=request.GET.get('limit')

    event=events.objects.get(name=name_value)
    event.price= price_value
    event.desc=desc_value
    event.limit=limit_value

    event.save()
    return JsonResponse({'message':'event updated'})

def delete_event(request):
    name_value=request.GET.get('name')
    event= events.objects.get(name=name_value)
    event.delete()
    return JsonResponse({'message':'event deleted'})

def add_event(request):
    name_value=request.GET.get('name')
    price_value=request.GET.get('price')
    desc_value=request.GET.get('desc')
    limit_value=request.GET.get('limit')
    
    events.objects.create(
        name=name_value,
        price=price_value,
        desc=desc_value,
        limit=limit_value
    )
    return JsonResponse({'message':'event added'})

def update_host(request):
    event_id_value=request.GET.get('event_id')
    host_id_value=request.GET.get('host_id')
    event=events.objects.get(event_id=event_id_value)
    host=hosts.objects.get(host_id=host_id_value)
    eventshosts.objects.create(
        event_id=event,
        host_id=host
    )
    return JsonResponse({'message':'event host updated'})

def fetch_hosts(request):
    result=hosts.objects.all().values()
    return JsonResponse(list(result),safe=False)

student_list = []
professor_list=[]
facility_list=[]

def add_student(request):
    name_value = request.GET.get('name')
    usn_value = request.GET.get('usn')
    phone_value = request.GET.get('phone')
    department_value = request.GET.get('department')

    student = {
        'name': name_value,
        'usn': usn_value,
        'phone': phone_value,
        'department': department_value
    }
    student.objects.create(view_students)
    student_list.append(student)
    return JsonResponse({'message': 'Student added successfully!', 'student': student})


def view_students(request):
    view_students=student.objects.all().values('name','usn','gender','cgpa')
    return JsonResponse({'Students data': list(view_students)})





professor_list = []

def add_professor(request):
    name_value = request.GET.get('name')
    id_value = request.GET.get('id')
    subject_value = request.GET.get('subject')
    experience_value = request.GET.get('experience')

    professor = {
        'name': name_value,
        'id': id_value,
        'subject': subject_value,
        'experience': experience_value
    }

    professor_list.append(professor)
    return JsonResponse({'message': 'Professor added successfully!', 'professor': professor})


def view_professors(request):
    return JsonResponse({'data': professor_list})



facility_list = []

def add_facility(request):
    name_value = request.GET.get('name')
    location_value = request.GET.get('location')
    description_value = request.GET.get('description')
    capacity_value = request.GET.get('capacity')

    facility = {
        'name': name_value,
        'location': location_value,
        'description': description_value,
        'capacity': capacity_value
    }

    facility_list.append(facility)
    return JsonResponse({'message': 'Facility added successfully!', 'facility': facility})


def view_facilities(request):
    return JsonResponse({'data': facility_list})