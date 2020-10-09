from django.shortcuts import render
import os

# Create your views here.
from rest_framework.mixins import Response
from rest_framework.views import APIView
from .models import User



current_path = os.path.dirname(__file__)

def response_success_200(res={}):
    """
    返回请求成功
    :param data_dict:
    :return: response(dict)
    """
    response = dict()
    response['msg'] = '请求成功'
    response['result'] = res
    response['code'] = 200
    return Response(response, status=200)


def response_failed_400():
    """
    返回请求失败
    :return: response(dict)
    """
    response = dict()
    response['msg'] = '请求参数错误'
    response['result'] = dict()
    response['code'] = 400
    return Response(response, status=400)



class SaveUserInfo(APIView):
    def post(self, request):
        new_user = User(name=request.data['name'],address=request.data['address'],sex= request.data['sex'],
                        age=request.data['age'],job=request.data['job'])
        new_user.save()

        res = {"user_id":new_user.user_id}

        return response_success_200(res)