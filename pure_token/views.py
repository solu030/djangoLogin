import uuid

from rest_framework.views import APIView
from rest_framework.response import Response

from pure_token.models import User_token


# Create your views here.

class LoginView(APIView):

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user_obj = User_token.objects.filter(username=username,password=password).first()
        if not user_obj:
            return Response({'status':1001,"errors":"用户名或密码错误"})
        token = str(uuid.uuid4())
        user_obj.token = token
        user_obj.save()
        return Response({"status":1000,"data":user_obj.token})

class ListView(APIView):
    def get(self, request):

        token = request.query_params.get('token')
        if not token:
            return Response({"status": 1003,"errors": "token不存在"})
        user_obj = User_token.objects.filter(token=token).first()
        if not user_obj:
            return Response({"status": 1004,"errors": "token错误"})
        return Response({"status": 2000,"data":user_obj.token})
