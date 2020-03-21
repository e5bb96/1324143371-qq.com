import csv,requests,json
def text():
    with open(r'C:\Users\e5bb96\Desktop\张佳玮.csv','w',newline='') as f:
        writer = csv.writer(f)
        list1 = ['标题','锁链','摘要']
        writer.writerow(list1)
        url = 'https://www.zhihu.com/api/v4/members/zhang-jia-wei/articles'
        headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'}
        for k in range(3):
            l = (10 if (k==0) else 20)
            params = {'include': 'data[*].comment_count,suggest_edit,is_normal,thumbnail_extra_info,thumbnail,can_comment,comment_permission,admin_closed_comment,content,voteup_count,created,updated,upvoted_followees,voting,review_info,is_labeled,label_info;data[*].author.badge[?(type=best_answerer)].topics',
            'offset': str((k+1)*10),
            'limit': str(l),
            'sort_by': 'created'}
            res = requests.get(url,headers=headers,params=params)
            #print(res.status_code)   #检查是否得到浏览器回应
            res.encoding='utf-8'        #encoding='格式'
            ja = res.json()     
            preview = ja['data']        #preview预览
            for i in preview:
                list2=[i['title'],i['url'],i['excerpt']]
                writer.writerow(list2)
text()
