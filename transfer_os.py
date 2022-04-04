import subprocess

start_ad = '충남 천안시 동남구 광덕면 세종로 4162'
end_ad = '경북 경산시 진량읍 양기리 407-29'


# 도로명 주소를 받으면 geocode 반환
street_ad = 'curl -G "https://naveropenapi.apigw.ntruss.com/map-geocode/v2/geocode"\
    --data-urlencode "query='+start_ad+'" \
    -H "X-NCP-APIGW-API-KEY-ID: 61f1e26542" \
    -H "X-NCP-APIGW-API-KEY: Xe80YvmWVK9v9PeIjA7iuUT1OZc5AkDjHCePcfFW" -v'

def subprocess_open(command):
    popen = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    (stdoutdata, stderrdata) = popen.communicate()
    return stdoutdata, stderrdata

# print(subprocess_open(street_ad))

begin = '127.1, 37.5'
end = '127.2, 37.3'


# 출발,도착지 geocode 받으면 거리 계산 / begin,end에는 출발,도착지의 x,y geocode가 들어가야 함
distance_cal = 'curl "https://naveropenapi.apigw.ntruss.com/map-direction/v1/driving?start='+begin+'&goal='+end+'&option=trafast"\
	-H "X-NCP-APIGW-API-KEY-ID: 61f1e26542" \
	-H "X-NCP-APIGW-API-KEY: Xe80YvmWVK9v9PeIjA7iuUT1OZc5AkDjHCePcfFW" -v'

print(subprocess_open(distance_cal))


## r에서 불러들인 데이터 가공 : x,y 좌표만 불러오기
# with open('/Users/jd/naverapi1.json', 'r') as f:

#     json_data = json.load(f)
#     start_x = json_data["addresses"][0]["x"]
#     start_y = json_data["addresses"][0]["y"]

# #입력 순서: 경도 위도 
# with open('/Users/jd/naverapi2.json', 'r') as f:

#     json_data = json.load(f)
#     arrive_x = json_data["addresses"][0]["x"]
#     arrive_y = json_data["addresses"][0]["y"]

# address_list1 = [start_x, start_y, arrive_x, arrive_y]


# begin = str(address_list1[0])+","+str(address_list1[1])
# end = str(address_list1[2])+","+str(address_list1[3])


## 거리계산

#     b = 1/1000
#     distance_sum = json_data["route"]['trafast'][0]['summary']['distance']

# print("total distance: ",math.trunc(distance_sum*b),'Km')