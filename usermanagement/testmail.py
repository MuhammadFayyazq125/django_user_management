import requests

def callapi(send_from,send_to,subject,cc,bcc,htmlBody,password):
    url = 'https://mis.mobilelinkusa.com/MLServiceAPI/api/SendEmail/SendEmailBody/'
    data = {"from": send_from, "to":send_to,"subject": subject,'cc':cc,'bcc':bcc,'htmlBody':htmlBody,'password':password}
    response = requests.post(url, json=data)
    # url+=send_from+'/'
    # url+=send_to+'/'
    # url+=subject+'/'
    # url+=cc+'/'
    # url+=bcc+'/'
    # url+=htmlBody+'/'
    # url+=password+'/'
    # response=requests.post(url)
    # return response

callapi('hasan_khan@mobilelinkusa.com','danish_hussain@mobilelinkusa.com',
        'testing subject','haseeb_ahmed@mobilelinkusa.com','',
        'testing body via py file','mobilelink@2')