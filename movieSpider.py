import requests
import os
import time

referer = 'http://youku.cdn1-kubozy.com/20210303/20553_fc9b0e33/index.m3u8'

with open('./url.txt', 'r') as f:
	url_dicts = eval(f.read())

headers = {'Referer':referer, 'User-Agent':'Mozilla/5.0 (Windows NT 6.1; wIN64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36'}

# data = requests.get("http://youku.cdn1-kubozy.com/20210303/20553_fc9b0e33/1000k/hls/e1843b1aa99000074.ts")
def heBingTsVideo(download_path,hebing_path):
    all_ts = os.listdir(download_path)
    with open(hebing_path, 'wb+') as f:
        for i in range(len(all_ts)):
            ts_video_path = os.path.join(download_path, all_ts[i])
            time.sleep(0.01)
            f.write(open(ts_video_path, 'rb').read())
    print("合并完成！！")

for t in range(len(url_dicts)):
	for i in range(670):
		a = i // 100
		b = (i // 10) % 10
		c = i % 10
		url = url_dicts[t][str(29 + t)] + str(a) + str(b) + str(c) + ".ts"	
		data = requests.get(url)
		with open('./zx/' + str(29 + t) + '/' + str(i) + '.ts', 'wb') as f:
			f.write(data.content)
		print('----{}:{}----'.format(29 + t, i))
	heBingTsVideo('./zx/' + str(29 + t) + '/', './zx/' + str(29 + t) + '.mp4')





