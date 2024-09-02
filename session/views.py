
from rest_framework.response import Response
from rest_framework.views import APIView

from session.models import *
# Create your views here.
class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        obj = User_Session.objects.filter(username=username, password=password).first()
        if not obj:
            return Response({"status": 1001,"errors": "用户名或密码错误"})
        request.session['username'] = obj.username
        return Response({"status": 1002,"data": "success"})
class ListView(APIView):
    def get(self, request):
        info = request.session.get('username')
        if not info:
            return Response({"status": 2001,"errors": "请登录后访问"})
        return Response({"status": 2002,"data": info,"msg": "成功"})