from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status,generics
from .serializers import SignUpSerializer


class SignUpView(generics.GenericAPIView):
    serializer_class=SignUpSerializer

    def post(self,request:Request):

        data = request.data

        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            res={
                "message":"User created successfully",
                "data":serializer.data
            } 

            return Response(data=res,status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)



