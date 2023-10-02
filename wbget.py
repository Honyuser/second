'''
   这是一个抖音视频的爬取小程序
   里面的网址是可以替换的

   开发思路：
   1.访问网址获取代码（requests库用于访问网址）
   2.获取想要的内容
   3.访问数据并保存到本地

   ./表示保存到当前文件夹下

'''

# 导入库
import requests

# 导入网址
url = 'https://v3-weba.douyinvod.com/546552a12c7dacc5fef54fdd39486c0a/6513c41d/video/tos/cn/tos-cn-ve-15c001-alinc2/owJrgbrUnAUleeaA2GD4u8Q1BBDIhGjgUp9VGA/?a=6383&ch=26&cr=3&dr=0&lr=all&cd=0%7C0%7C0%7C3&cv=1&br=1811&bt=1811&cs=0&ds=6&ft=XzJ6BM06xxou7Y._1PI12lMg4-iGNbL8316aU_4LkmfP2Nv7T&mime_type=video_mp4&qs=12&rc=aDRoPDlkODQ5ZGY3PDRmM0Bpam9vZGQ6ZmdobjMzNGkzM0AyYWJjXzUtXy8xLjE1Ni81YSNlMGU1cjRnMDBgLS1kLTBzcw%3D%3D&btag=e00010000&dy_q=1695790583&l=202309271256238C139C37DD29910C9138'
# 访问链接的内容
video_content = requests.get(url).content
# 保存视频到本地
with open("./shipin.mp4","wb") as file:
    file.write(video_content)
    print('下载完成！')
