import requests,json,openpyxl
all_=[]
class all_12:
    def __init__(self):
        url = 'https://u.y.qq.com/cgi-bin/musicu.fcg'
        headers={
            'Origin': 'https://y.qq.com',
            'Referer': 'https://y.qq.com/n/yqq/singer/001BLpXF2DyJe2.html',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'
        }

        for i in range(1):
            number = str((i)*10)
            params_ = {
            '-': 'getSingerSong9169760373122566',
            'g_tk': '5381',
            'loginUin': '0',
            'hostUin': '0',
            'format': 'json',
            'inCharset': 'utf8',
            'outCharset': 'utf-8',
            'notice': '0',
            'platform': 'yqq.json',
            'needNewCode': '0',
            'data': '{"comm":{"ct":24,"cv":0},"singerSongList":{"method":"GetSingerSongList","param":{"order":'+number+',"singerMid":"001BLpXF2DyJe2","begin":1,"num":10},"module":"musichall.song_list_server"}}'
            }
            a = requests.get(url,params=params_,headers=headers)    
        #json将对像转换成列表或字典
            b = a.json()            
            c = b['singerSongList']['data']['songList']
            for o in c:
                aa = o['songInfo']['name']
                bb = o['songInfo']['album']['name']
                cc = o['songInfo']['url']

                lists=(aa,bb,cc)
                self.all_1= all_.append(list(lists))
        print(self.all_1)

    def self_(self):
        wb = openpyxl.Workbook()
        sheet = wb.active
        names = ['歌曲名','所属专辑','播放时长','播放锁链']
        sheet.append(names)
        for i in self.all_1 :
            sheet.append(i)
        wb.save(r'C:\Users\e5bb96\Desktop\name.xlsx')

