import json

def load_cookies(driver, session_name):
    cookies = get_saved_cookies(session_name)
    if not cookies:
        return False
    for cookie in cookies:
        driver.add_cookie(cookie)
    return True

def save_cookies(driver, session_name):
    with open(f'./cookies_{session_name}.json', 'w') as cookies_file:
        cookies_file.write(json.dumps(driver.get_cookies()))

def get_saved_cookies(session_name):
    try:
        with open(f'./cookies_{session_name}.json', 'r') as cookies_file:
            return json.loads(cookies_file.read())
    except:
        return False