# -*- coding: utf-8 -*-

# Author : Robert
# Create Date : 2019/4/1 8:31
# File  :  re_practice.py
# IDE   :  PyCharm

import re
s = '''
<dd class="job_bt">
        <h3 class="description">职位描述：</h3>
        <div class="job-detail">
        <p><strong>岗位职责：</strong></p>
<ul class=" list-paddingleft-2">
 <li><p>负责森果各系统Web后端功能开发、数据处理和系统维护等。</p></li>
</ul>
<p><br></p>
<p><strong>必备技能：</strong></p>
<ul class=" list-paddingleft-2">
 <li><p>熟悉Python语言及其特性，了解相关Python Web框架；</p></li>
 <li><p>熟悉<a class="jd-ad" href="https://kaiwu.lagou.com/course/courseInfo.htm?courseId=1&amp;sid=3-MySQL-1554078627429" target="_blank" rel="nofollow" data-ad="3" data-lg-tj-id="1kcw" data-lg-tj-no="idnull" data-lg-tj-cid="31554078627429" data-lg-tj-content="MySQL">MySQL</a>的基本操作；</p></li>
 <li><p>掌握面向对象的程序设计思想；</p></li>
 <li><p>熟悉Linux开发环境；</p></li>
 <li><p>至少使用Python开发过一个Web应用。</p></li>
</ul>
<p><br></p>
<p><strong>加分项：</strong></p>
<ul class=" list-paddingleft-2">
 <li><p>学无止境，新框架新技术分分钟搞定；</p></li>
 <li><p>玩过至少一种非关系型<a class="jd-ad" href="https://kaiwu.lagou.com/course/courseInfo.htm?courseId=1&amp;sid=3-%E6%95%B0%E6%8D%AE%E5%BA%93-1554078627430" target="_blank" rel="nofollow" data-ad="3" data-lg-tj-id="1kcw" data-lg-tj-no="idnull" data-lg-tj-cid="31554078627430" data-lg-tj-content="数据库">数据库</a>；</p></li>
 <li><p>熟悉HTML5 / CSS3 / JS；</p></li>
 <li><p>熟练使用Python标准库，熟悉sqlalchemy、celery、requests、numpy、pandas等第三方库；</p></li>
 <li><p>了解非阻塞Web框架Tornado的特性，使用Tornado开发过Web应用。</p></li>
</ul>
<p><br></p>
<p><strong>在个人简历中附上github地址或作品地址，会增加您被HR看中的机会～</strong></p>
<p><strong><br></strong></p>
<p><strong><br></strong></p>
        </div>
    </dd>'''


li = re.findall(r'<(\w)>(.*)</\1>',s)
for i in li:
    print(i[1])


# s1 = s.replace("<p>",'')
# s1 = re.sub(r'<p>|</p>','',s,re.S)
# print(s1)
# print(s1)