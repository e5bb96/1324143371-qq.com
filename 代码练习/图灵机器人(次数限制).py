import requests,json
session = requests.session()

url = r'http://openapi.tuling123.com/openapi/api/v2'

contents = input("请输入你要询问的问题：")

data = {
	"reqType":0,
    "perception": {
        "inputText": {
            "text": "contents"
        },
        "inputImage": {
            "url": "imageUrl"
        },
        "selfInfo": {
            "location": {
                "city": "北京",
                "province": "",
                "street": ""
            }
        }
    },
    "userInfo": {
        "apiKey": "41c76be3d651459994c5b15ee3366c99",
        "userId": "e5bb96"
    }
}

data_json = json.dumps(data).encode('utf-8')    #转json格式
content = session.post(url,data_json)
data = json.loads((content._content).decode('utf-8')) #反列序化
print(data)
