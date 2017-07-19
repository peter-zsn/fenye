#coding=utf-8

"""
@varsion: ??
@author: 张帅男
@file: views.py
@time: 2017/7/18 17:00
"""
from libs.ajax_template import render_template, ajax_ok
from apps.common import get_page_url

def page(request):
    data = {}
    n = 5
    data_list = []
    for i in range(100):
        data_list.append({
            "id": i,
            "value": "haha",
            "word": 123456 + i,
        })
    if request.method == 'POST':
        id = int(request.POST.get("id", 0))
        a = data_list[id]['word']
        data['pwd'] = a
        return ajax_ok(data)
    page_no = int(request.GET.get('page', 0))
    count = len(data_list)
    data_list = data_list[page_no * n: (page_no+ 1) * n]
    page_url = get_page_url(request, count, n, page_no)
    data['data'] = data_list
    data['page_url'] = page_url
    return render_template(request, 'fenye.html', data)