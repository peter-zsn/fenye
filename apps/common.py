#coding=utf-8

"""
@varsion: ??
@author: 张帅男
@file: common.py
@time: 2017/7/18 17:42
"""
import re

def get_page_url(request, allCount, pageSize, pageIndex):
    newurl = re.sub(r'page=\d*', '', request.get_full_path())
    urlprefix = update(newurl)
    if allCount > pageSize:
        hits = allCount / pageSize
        if allCount % pageSize != 0:
            hits = hits + 1
    else:
        hits = 1
    start_num = 1
    end_num = 1
    page_url = u''
    page_pre = u''
    page_last = u''
    # 总页数小于等于显示分页数
    if hits <= 10:
        end_num = hits

    if hits > 10:
        if pageIndex - 8 >= 0:
            page_pre = u'<a href="%(href)spage=1">1</a><a href="%(href)spage=2">2</a>...' % {'href': urlprefix}
            start_num = pageIndex - 3
        if pageIndex + 6 <= hits:
            page_last = u'..<a href="%(href)spage=%(pageindex_pre)d">%(pageindex_pre)d</a><a href="%(href)spage=%(pageindex)d">%(pageindex)d</a>' % {
                'href': urlprefix, 'pageindex_pre': hits - 1, 'pageindex': hits}

            if page_pre:
                end_num = pageIndex + 3

            else:
                end_num = 8
        else:

            end_num = hits
    page_url += page_pre
    for n in range(start_num, end_num + 1):
        if n == pageIndex:
            page_url += u'<a href="%(href)spage=%(pageindex)d" class="current">%(pageindex)d</a>' % {'href': urlprefix,
                                                                                                     'pageindex': n}
        else:
            page_url += u'<a href="%(href)spage=%(pageindex)d">%(pageindex)d</a>' % {'href': urlprefix, 'pageindex': n}

            # 设置上一页
    if pageIndex > 1:
        page_url = u'<a href="%(href)spage=%(pageindex)d">上一页</a>' % {'href': urlprefix,
                                                                      'pageindex': pageIndex - 1} + page_url
    if pageIndex < hits:
        page_last += u'<a href="%(href)spage=%(pageindex)d">下一页</a>' % {'href': urlprefix, 'pageindex': pageIndex + 1}
    page_url = u'<div class=page_list>' + page_url + page_last + '</div>'
    if hits <= 1:
        return ''
    return page_url


def update(url):
    if url.find('?') == -1:
        url = url + '?'
    if not url.endswith('&') and not url.endswith('?'):
        url = url + '&'
    return url