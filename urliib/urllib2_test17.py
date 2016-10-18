# -*- coding: cp936 -*-  
import urllib  
page = 1  
head = 'http://blog.sina.com.cn/s/articlelist_1191258123_0_'  
end = '.html'  
i = 0  
while page <= 7:  
    url = head + str(page) + end  
    print url     
    con0 = urllib.urlopen(url).read()  
    con = con0  
    while con.find(r'<a title=') != -1:  
        a0 = con.find(r'<a title=')  
        if con.find(r'href=',a0) != -1:  
            a1 = con.find(r'href=',a0)
            if con.find(r'html">',a1) != -1:  
                b1 = con.find(r'html">',a1)  
                url1 = con[a1+6 : b1+4]   
                i = i + 1  
                print i ,':', url1  
                content = urllib.urlopen(url1).read()  
                if url1.find('blog_') != -1:  
                    c1 = url1.find('blog_')  
                    open(url1[c1 :],'w').write(content)  
                con = con[b1+4:]   
    page = page + 1  