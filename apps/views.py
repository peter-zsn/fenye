#coding=utf-8

"""
@varsion: ??
@author: 张帅男
@file: views.py
@time: 2017/7/18 17:00
"""
from libs.ajax_template import render_template
from apps.common import get_page_url

def page(request):
    page_no = int(request.GET.get('page', 0))
    data = {}
    n = 5
    data_list = []
    for i in range(100):
        data_list.append({
            "id": i,
            "value": "haha"
        })
    count = len(data_list)
    data_list = data_list[page_no * n: (page_no+ 1) * n]
    page_url = get_page_url(request, count, n, page_no)
    data['data'] = data_list
    data['page_url'] = page_url
    return render_template(request, 'fenye.html', data)