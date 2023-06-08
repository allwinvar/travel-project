from django.http import HttpResponse
from django.shortcuts import render
from .models import Place, Crew


# Create your views here.
def demo(request):
    obj=Place.objects.all()
    obj1=Crew.objects.all()

    # temporary places
    obj = [
        {
            'image': {'url': '/static/temp_places/destination_1.jpg'},
            'name': 'Bali',
            'description': 'Nulla pretium tincidunt felis, nec.',
        },
        {
            'image': {'url': '/static/temp_places/destination_2.jpg'},
            'name': 'Indonesia',
            'description': 'Nulla pretium tincidunt felis, nec.',
        },
        {
            'image': {'url': '/static/temp_places/destination_3.jpg'},
            'name': 'San Francisco',
            'description': 'Nulla pretium tincidunt felis, nec.',
        },
        {
            'image': {'url': '/static/temp_places/destination_4.jpg'},
            'name': 'Paris',
            'description': 'Nulla pretium tincidunt felis, nec.',
        },
        {
            'image': {'url': '/static/temp_places/destination_5.jpg'},
            'name': 'Phi Phi Island',
            'description': 'Nulla pretium tincidunt felis, nec.',
        },
        {
            'image': {'url': '/static/temp_places/destination_6.jpg'},
            'name': 'Mykonos',
            'description': 'Nulla pretium tincidunt felis, nec.',
        },
    ]

    #temporary team crew
    obj1 = [
        {'name': 'John Doe', 'description': 'Lorem ipsum dolor sit amet.', 'image': {'url': '/static/temp_crew/john.jpg'}},
        {'name': 'Jane Smith', 'description': 'Consectetur adipiscing elit.','image': {'url': '/static/temp_crew/jane.jpg'}},
        {'name': 'Mark Johnson', 'description': 'Ut suscipit magna at pharetra viverra.','image': {'url': '/static/temp_crew/mark.jpg'}},
        {'name': 'Sarah Davis','description': 'Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae.','image': {'url': '/static/temp_crew/sarah.jpg'}},
        # Add more team members as needed
    ]

    return render(request,"index.html",{'result':obj,'result1':obj1})









# def addition(request):
#     x=request.GET("num1")
#     y = request.GET("num2")
#     z=x+y
#     return render(request,"home.html",{"Result":z})
