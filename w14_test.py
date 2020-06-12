'''
pip install google-api-python-client

pip install oauth2client
'''


import sys
from oauth2client import client
from googleapiclient import sample_tools

argv = ""
# 認證並建立服務
service, flags = sample_tools.init(
  argv, 'blogger', 'v3','./client_secrets.json',
  scope='https://www.googleapis.com/auth/blogger')

try:
    users = service.users()
    # 取得使用者 profile 資料
    user = users.get(userId='self').execute()
    print('網誌名稱: %s' % user['displayName'])
    blogs = service.blogs()
    # 取得使用者所建立網誌名稱
    blogs = blogs.listByUser(userId='self').execute()
    for blog in blogs['items']:
        print(blog['name'], blog['url'])
    posts = service.posts()
    # 新增網誌 post 時, 需要 blog id
    
    body = {
    "kind": "blogger#post",
    "id": "7327461907892350368",
    "title": "透過 Python 程式新增網誌文章",
    "content":"使用 Google Blogger API 可以利用程式新增網誌文章內容"
    }
    insert = posts.insert(blogId='7327461907892350368', body=body)
    posts_doc = insert.execute()
    print(posts_doc)
    '''
    # 更新網誌文章時的 body
    body = {
    "kind": "blogger#post",
    "title": "透過 Python 程式修改網誌文章",
    "content":''使用 Google Blogger API 可以利用程式修改網誌文章內容. http://mde.tw/cd2019
    
    }
    update = posts.update(blogId="5276710004996457925", postId="1389587938059038064", body=body, publish=True)
    update_doc = update.execute()
    print(update_doc)
    '''
except(client.AccessTokenRefreshError):
    print("error")