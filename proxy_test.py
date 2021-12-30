import requests

def get_proxy_list():
    proxy_list = requests.get('https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/https.txt').text.split('\n')
    return proxy_list

def get_working_proxies(proxy_list):
    working = []
    for proxy in proxy_list:
        if proxy != '':
            try:
                r = requests.get('https://amuseanime.netlify.app/', proxies={'https': proxy}, timeout=3)
                if r.status_code == 200:
                    print(f'{proxy} is working!')
                    working.append(proxy)
            except:
                # print(f"{proxy} is not working.")
                pass 
    return working

print(get_working_proxies(get_proxy_list()))