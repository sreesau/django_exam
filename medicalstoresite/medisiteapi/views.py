from django.shortcuts import render
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.response import Response
from rest_framework import generics
from .serializers import RegisterSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import MedicineDetailsSerializer
from medisite.models import MedicineDetails

@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key},status=HTTP_200_OK)


class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer


@api_view(['GET', 'POST'])
def medicine_list(request):
    if request.method == 'GET':
        medicines = MedicineDetails.objects.all()
        serializer = MedicineDetailsSerializer(medicines, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = MedicineDetailsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT', 'DELETE'])
def medicine_detail(request, pk):
    try:
        medicine = MedicineDetails.objects.get(pk=pk)
    except MedicineDetails.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = MedicineDetailsSerializer(medicine)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = MedicineDetailsSerializer(medicine, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        medicine.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@api_view(['GET'])
def medicine_search(request):
    query = request.GET.get('q', '')
    
    if not query:
        return Response({'error': 'Please provide a search query'}, status=status.HTTP_400_BAD_REQUEST)

    medicines = MedicineDetails.objects.filter(name__icontains=query) | \
                MedicineDetails.objects.filter(quantity__icontains=query) | \
                MedicineDetails.objects.filter(price__icontains=query) | \
                MedicineDetails.objects.filter(mfg_date__icontains=query) | \
                MedicineDetails.objects.filter(exp_date__icontains=query)

    serializer = MedicineDetailsSerializer(medicines, many=True)
    return Response(serializer.data)