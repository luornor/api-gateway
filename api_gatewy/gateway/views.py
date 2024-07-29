from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import requests

# Create your views here.
@api_view(['POST'])
def signup(request):
    data = request.data
    response = requests.post("http://127.0.0.1:8001/api/users/register/", data=data)
    try:
        return Response(response.json(), status=response.status_code)
    except ValueError:
        return Response(response.text, status=response.status_code)


@api_view(['POST'])
def login(request):
    data = request.data
    response = requests.post("http://127.0.0.1:8001/api/users/login/", data=data)
    try:
        return Response(response.json(), status=response.status_code)
    except ValueError:
        return Response(response.text, status=response.status_code)


@api_view(['GET', 'DELETE', "PUT"])
def getAndDeleteProfile(request, pk):
    if request.method == "GET":
        response = requests.get(f"http://127.0.0.1:8001/api/users/{pk}/")
    elif request.method == "DELETE":
        response = requests.delete(f"http://127.0.0.1:8001/api/users/{pk}/")
    else:
        data = request.data
        response = requests.put(f"http://127.0.0.1:8001/api/users/{pk}/", data=data)

    try:
        return Response(response.json(), status=response.status_code)
    except ValueError:
        return Response(response.text, status=response.status_code)



@api_view(['GET'])
def listings(request):
    response = requests.get("http://127.0.0.1:8003/api/listings/")
    try:
        return Response(response.json(), status=response.status_code)
    except ValueError:
        return Response(response.text, status=response.status_code)


@api_view(['GET', 'DELETE', "PUT"])
def listings_details(request, pk):
    if request.method == "GET":
        response = requests.get(f"http://127.0.0.1:8003/api/listings/{pk}/")
    elif request.method == "DELETE":
        response = requests.delete(f"http://127.0.0.1:8003/api/listings/{pk}/")
    else:
        data = request.data
        response = requests.put(f"http://127.0.0.1:8003/api/listings/{pk}/", data=data)

    try:
        return Response(response.json(), status=response.status_code)
    except ValueError:
        return Response(response.text, status=response.status_code)



@api_view(['GET', 'POST','DELETE', "PUT", "PATCH"])
def shops(request, pk):
    if request.method == "POST":
        data = request.data
        response = requests.post(f"http://127.0.0.1:8003/api/shops/{pk}/listings/", data=data)
    elif request.method == "GET":
        response = requests.get(f"http://127.0.0.1:8003/api/shops/{pk}/listings/")
    elif request.method == "DELETE":
        response = requests.delete(f"http://127.0.0.1:8003/api/shops/{pk}/listings/")
    else:
        data = request.data
        response = requests.patch(f"http://127.0.0.1:8003/api/shops/{pk}/listings/", data=data)

    try:
        return Response(response.json(), status=response.status_code)
    except ValueError:
        return Response(response.text, status=response.status_code)

@api_view(['POST'])
def CreateCart(request):
    data = request.data
    response = requests.post("http://127.0.0.1:8002/api/cart/create/", data=data)
    try:
        return Response(response.json(), status=response.status_code)
    except ValueError:
        return Response(response.text, status=response.status_code)
    
@api_view(['POST'])
def AddToCart(request):
    data = request.data
    response = requests.post("http://127.0.0.1:8002/api/cart/items/add/", data=data)
    try:
        return Response(response.json(), status=response.status_code)
    except ValueError:
        return Response(response.text, status=response.status_code)
    

@api_view(['GET','DELETE'])
def CartItems(request,user_id):
    if request.method=='GET':
        response = requests.get(f"http://127.0.0.1:8002/api/cart/{user_id}/")

    if request.method=='DELETE':
        response = requests.delete(f"http://127.0.0.1:8002/api/cart/{user_id}/")
    
    try:
        return Response(response.json(), status=response.status_code)
    except ValueError:
        return Response(response.text, status=response.status_code)
    
@api_view(['GET'])

@api_view(['GET'])
def orders(request):
    response = requests.get("http://127.0.0.1:8002/api/order-list/")
    try:
        return Response(response.json(), status=response.status_code)
    except ValueError:
        return Response(response.text, status=response.status_code)
    

@api_view(['POST'])
def orders_add(request):
    data = request.data
    response = requests.post("http://127.0.0.1:8002/api/orders/", data=data)
    try:
        return Response(response.json(), status=response.status_code)
    except ValueError:
        return Response(response.text, status=response.status_code)
    

@api_view(['GET', 'DELETE', "PUT", "PATCH"])
def order_details(request, pk):
    if request.method == "GET":
        response = requests.get(f"http://127.0.0.1:8002/api/orders/{pk}/")
    elif request.method == "DELETE":
        response = requests.delete(f"http://127.0.0.1:8002/api/orders/{pk}/")
    elif request.method == "PUT":
        data = request.data
        response = requests.put(f"http://127.0.0.1:8002/api/orders/{pk}/", data=data)
    else:
        data = request.data
        response = requests.put(f"http://127.0.0.1:8002/api/orders/{pk}/", data=data)

    try:
        return Response(response.json(), status=response.status_code)
    except ValueError:
        return Response(response.text, status=response.status_code)
    

@api_view(['GET'])
def deliveries(request):
    response = requests.get("http://127.0.0.1:8006/api/deliver/")
    try:
        return Response(response.json(), status=response.status_code)
    except ValueError:
        return Response(response.text, status=response.status_code)
    


@api_view(['GET', "PUT"])
def delivery_details(request, pk):
    if request.method == "GET":
        response = requests.get(f"http://127.0.0.1:8006/api/update/{pk}/")
    elif request.method == "PUT":
        data = request.data
        response = requests.put(f"http://127.0.0.1:8006/api/update/{pk}/", data=data)

    try:
        return Response(response.json(), status=response.status_code)
    except ValueError:
        return Response(response.text, status=response.status_code)