from django.contrib.auth.models import User
from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .serializers import *


class ListagemClientes(APIView):
    def get(self, request, format=None):
        clientes = Cliente.objects.all()
        serializer = ClientesSerializer(clientes, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ClientesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DetalhesCliente(APIView):
    def get_object(self, pk):
        try:
            return Cliente.objects.get(pk=pk)
        except Cliente.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        cliente = self.get_object(pk)
        serializer = ClientesSerializer(cliente)
        return Response(serializer.data)

    def patch(self, request, pk, format=None):
        cliente = self.get_object(pk)
        serializer = ClientesSerializer(cliente, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        cliente = self.get_object(pk)
        cliente.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
    

class ListagemFornecedor(APIView):
    def get(self, request, format=None):
        fornecedor = Fornecedor.objects.all()
        serializer = FornecedorSerializer(fornecedor, many=True)
        return Response(serializer.data)


    def post(self, request, format=None):
        serializer = FornecedorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DetalhesFornecedor(APIView):
    def get_object(self, pk):
        try:
            return Fornecedor.objects.get(pk=pk)
        except Fornecedor.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        fornecedor = self.get_object(pk)
        serializer = FornecedorSerializer(fornecedor)
        return Response(serializer.data)

    
    def patch(self, request, pk, format=None):
        fornecedor = self.get_object(pk)
        serializer = FornecedorSerializer(fornecedor, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    def delete(self, request, pk, format=None):
        fornecedor = self.get_object(pk)
        fornecedor.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
        

class ListagemTitulos(APIView):
    def get(self, request, format=None):
        titulos = Titulo.objects.all()
        serializer = TitulosSerializer(titulos, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TitulosSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DetalhesTitulos(APIView):
    def get_object(self, pk):
        try:
            return Titulo.objects.get(pk=pk)
        except Titulo.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        titulo = self.get_object(pk)
        serializer = TitulosSerializer(titulo)
        return Response(serializer.data)

    def patch(self, request, pk, format=None):
        titulo = self.get_object(pk)
        serializer = TitulosSerializer(
            titulo,
            data=request.data,
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    def delete(self, request, pk, format=None):
        titulo = self.get_object(pk)
        titulo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ListagemContas_A_Pagar(APIView):
    def get(self, request, format=None):
        contasapagar = Contas_A_Pagar.objects.all()
        serializer = ContasAPagarSerializer(contasapagar, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ContasAPagarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DetalhesContas_A_Pagar(APIView):
    def get_object(self, pk):
        try:
            return Contas_A_Pagar.objects.get(pk=pk)
        except Contas_A_Pagar.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        contasapagar = self.get_object(pk)
        serializer = ContasAPagarSerializer(contasapagar)
        return Response(serializer.data)

    
    def patch(self, request, pk, format=None):
        contasapagar = self.get_object(pk)
        serializer = ContasAPagarSerializer(
            contasapagar,
            data=request.data,
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk, format=None):
        contasapagar = self.get_object(pk)
        contasapagar.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

