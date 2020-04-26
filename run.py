import requests, string, random,json
req = requests.Session()
def genString(stringLength):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(stringLength))
def getRandUsername():
    headers = {
        'Connection': 'keep-alive',
        'Accept': 'application/json, text/plain, */*',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36',
        'Content-Type': 'application/json;charset=UTF-8',
        'Origin': 'https://instarlike.com',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://instarlike.com/auth',
        'Accept-Language': 'en-US,en;q=0.9',
    }

    data = '{"login":"%s"}'%(genString(random.randint(1,5)))
    response = requests.post('https://instarlike.com/api/instaSearch', headers=headers, data=data)
    jsonq = json.loads(response.text)["user"]["users"]
    return jsonq
def reff(id):
    x = getRandUsername()
    req.get(id)
    promo_id = id.split("=")
    headers = {
        'Connection': 'keep-alive',
        'Accept': 'application/json, text/plain, */*',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36',
        'Content-Type': 'application/json;charset=UTF-8',
        'Origin': 'https://instarlike.com',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://instarlike.com/auth',
        'Accept-Language': 'en-US,en;q=0.9',
    }
    try:
        for i in x:
            data = '{"login":"%s","promo_id":"%s","is_web":true,"is_vip":true}'%(i["username"],promo_id[1])
            print(data)
            response = req.post('https://instarlike.com/api/registerUser', headers=headers, data=data)
            if "ERROR" not in response.text:
                print("Success reff!")
            else:
                print("Failed reff!")
            req.cookies.clear()
    except:
        print("Got error contact corrykalam[at]zicor.media")
reffx = input("ur refferal link: ")
while(1):
    reff(reffx)
