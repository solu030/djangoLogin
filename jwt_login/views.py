
from rest_framework.views import APIView
from rest_framework.response import Response

from jwt_login.utils.jwt_generate import generate_jwt_token
from jwt_login.extends.auth_jwt import JwtQueryParamsAuthentication
from jwt_login.models import *
# Create your views here.
class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        obj = User_JWT.objects.filter(username=username,password=password).first()
        if not obj:
            return Response({"status": 1001,"errors": "用户名或密码错误"})
        payload = {
            "id": obj.id,
            "user": obj.username,
        }
        jwt = generate_jwt_token(payload)
        return Response({"jwt":jwt,"msg":"jwt生成成功"})

class ListView(APIView):
    authentication_classes = [JwtQueryParamsAuthentication,]
    def get(self, request):
        return Response({"status":2000,"payload": request.user})