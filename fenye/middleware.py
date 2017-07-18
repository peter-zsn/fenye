#coding=utf-8

"""
@varsion: ??
@author: 张帅男
@file: middleware.py
@time: 2017/7/18 17:08
"""

import traceback
import json

from libs.common import casts, loads
from django.http.request import QueryDict
from django.http import HttpRequest, HttpResponseRedirect, HttpResponse, Http404
from django.conf import settings


QueryDict.casts = casts
HttpRequest.loads = loads

anonymous_urls = ['/media/']

class AuthenticationMiddleware(object):
    def process_request(self, request):
        path = str(request.path)
        for obj in anonymous_urls:
            if path.startswith(obj):
                return
        try:
            return self._process_request(request)
        except:
            exc = traceback.format_exc()
            if settings.DEBUG:
                print exc

    def _process_request(self, request):
        query = request.GET.copy()
        query.update(request.POST)
        # 把body参数合并到QUERY
        try:
            body = json.loads(request.body)
            query.update(body)
        except:
            pass
        return

    def process_response(self, request, response):
        return response

    def process_exception(self, request, exception):
        if isinstance(exception, Http404):
            return
        if isinstance(exception, AssertionError):
            message = exception.message
            if not message:
                return
        path = str(request.path)
        # 如果请求的路径为 js css 文件 不处理
        if path.startswith('/media/'):
            return None