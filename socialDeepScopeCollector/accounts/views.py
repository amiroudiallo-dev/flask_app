from rest_framework import generics, status, permissions # pyright: ignore[reportMissingImports]
from rest_framework.request import Request # pyright: ignore[reportMissingImports]
from rest_framework.response import Response # pyright: ignore[reportMissingImports]

from .serailizers import *
from .models import Language
from .serailizers import LanguageSerializer, SignUpSerializer


class LanguageAPIView(generics.ListCreateAPIView):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    paginator = None
list_create_language = LanguageAPIView.as_view()


class RetUpdateDelLanguage(generics.RetrieveUpdateDestroyAPIView):

    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    permission_classes = [permissions.IsAdminUser]
ret_upate_del_LanguageView = RetUpdateDelLanguage.as_view()


class SignUpView(generics.GenericAPIView):
    serializer_class = SignUpSerializer
    permission_classes = []

    def post(self, request: Request):
        data = request.data

        serializer = self.serializer_class(data=data)

        if serializer.is_valid():
            serializer.save()

            response = {"message": "User Created Successfully", "data": serializer.data}

            return Response(data=response, status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
