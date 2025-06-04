from uuid import UUID
from django.shortcuts import render

from django.http import JsonResponse, HttpRequest
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination

from equipment.models import Equipment, EquipmentType
from equipment.serializers import CreateEquipmentSerializer, EquipmentSerializer, EquipmentTypeSerializer
from equipment.services import create_equipments


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_equipment_list(request: Request) -> Response:
    """Вывод пагинированного списка
    оборудования с возможностью
    поиска путем указания query
    параметров советующим ключам
    ответа

    Args:
        request (Request): запрос клиента

    Returns:
        Response: ответ клиенту
    """
    query_params = request.query_params
    queryset = Equipment.objects.filter(is_deleted=False)

    for key, value in query_params.items():
        if hasattr(Equipment, key):
            queryset = queryset.filter(**{key + '__icontains': value})

    paginator = PageNumberPagination()
    result_page = paginator.paginate_queryset(queryset, request)
    serializer = EquipmentSerializer(result_page, many=True)

    return paginator.get_paginated_response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_equipment_detail(request: Request, id: UUID) -> JsonResponse:
    """Запрос данных по id

    Args:
        request (Request): запрос клиента
        id (UUID): индентификатор оборудования

    Returns:
        JsonResponse: ответ клиенту
    """
    equipment = get_object_or_404(Equipment, _id=id, is_deleted=False)

    return JsonResponse(EquipmentSerializer(equipment).data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_equipment(request: Request) -> JsonResponse:
    """Создание новой(ых) записи(ей)

    Args:
        request (Request): запрос клиента

    Returns:
        JsonResponse: ответ клиенту
    """
    serializer = CreateEquipmentSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    data = serializer.validated_data
    created = create_equipments(
        equipment_type=data['equipment_type'],
        serial_numbers=data['valid_serial_numbers'],
        note=data.get('note')
    )

    return JsonResponse({
        'created': EquipmentSerializer(created, many=True).data,
        'errors': data['errors']
    }, status=status.HTTP_201_CREATED)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_equipment(request: Request, id: UUID) -> JsonResponse:
    """Редактирование записи

    Args:
        request (Request): запрос клиента
        id (UUID): индентификатор оборудования

    Returns:
        JsonResponse: ответ клиенту
    """
    equipment = get_object_or_404(Equipment, _id=id, is_deleted=False)
    serializer = EquipmentSerializer(instance=equipment, data=request.data, partial=True)
    serializer.is_valid(raise_exception=True)
    serializer.save()

    return JsonResponse(serializer.data)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_equipment(request: Request, id: UUID) -> JsonResponse:
    """Удаление записи (мягкое удаление)

    Args:
        request (Request): запрос клиента
        id (UUID): индентификатор оборудования

    Returns:
        JsonResponse: ответ клиенту
    """
    equipment = get_object_or_404(Equipment, _id=id, is_deleted=False)
    equipment.is_deleted = True
    equipment.save()

    return JsonResponse({'message': 'Deleted'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_equipment_type_list(request: Request) -> Response:
    """Вывод пагинированного списка типов
    оборудования с возможностью
    поиска путем указания query
    параметров советующим ключам
    ответа

    Args:
        request (Request): запрос клиента

    Returns:
        Response: твет клиенту
    """
    query_params = request.query_params
    queryset = EquipmentType.objects.all()

    for key, value in query_params.items():
        if hasattr(EquipmentType, key):
            queryset = queryset.filter(**{key + '__icontains': value})

    paginator = PageNumberPagination()
    result_page = paginator.paginate_queryset(queryset, request)
    serializer = EquipmentTypeSerializer(result_page, many=True)

    return paginator.get_paginated_response(serializer.data)
