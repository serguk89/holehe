from holehe.core import *
from holehe.localuseragent import *

def crevado(email):
    s=requests.session()
    headers = {
        'User-Agent': random.choice(ua["browsers"]["chrome"]),
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'https://crevado.com',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'TE': 'Trailers',
    }

    req=s.get("https://crevado.com")
    token=req.text.split('<meta name="csrf-token" content="')[1].split('"')[0]

    data = [
      ('utf8', '\u2713'),
      ('authenticity_token', token),
      ('plan', 'basic'),
      ('account[full_name]', ''),
      ('account[email]', email),
      ('account[password]', ''),
      ('account[domain]', ''),
      ('account[confirm_madness]', ''),
      ('account[terms_accepted]', '0'),
      ('account[terms_accepted]', '1'),
    ]

    response = s.post('https://crevado.com/', headers=headers, data=data)
    try:
        msg_error=response.text.split('showFormErrors({"')[1].split('"')[0]
        if msg_error=="account_email":
            errorEMail=response.text.split('showFormErrors({"account_email":{"error_message":"')[1].split('"')[0]
            if errorEMail=="has already been taken":
                return({"rateLimit": False, "exists": True, "emailrecovery": None, "phoneNumber": None, "others": None})
            else:
                return({"rateLimit": False, "exists": False, "emailrecovery": None, "phoneNumber": None, "others": None})
        else:
            return({"rateLimit": False, "exists": False, "emailrecovery": None, "phoneNumber": None, "others": None})
    except :
        return({"rateLimit": True, "exists": False, "emailrecovery": None, "phoneNumber": None, "others": None})
