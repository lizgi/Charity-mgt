from datetime import datetime
import base64
import requests
import json
m={
    "paybill":"174379",
    "passKey":"bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919",
    "consumer_key":"mVCZ6HueP2soLBtsAG8GWyfF7R1D1ATm",
    "consumer_secret":"xoEeo8whgW2fiYBN",
    "BusinessShortCode": 174379,
    "TransactionType": "CustomerPayBillOnline",
    "PartyB": 174379,
     "CallBackURL": "https://mydomain.com/path",
    "AccountReference": "CompanyXLTD",
    "TransactionDesc": "Payment of X"
}
def express_payload(amount,phone,passkey,time):
    return {
         "BusinessShortCode": 174379,
         "Password":passkey,
         "Timestamp":time,
         "TransactionType": "CustomerPayBillOnline",
          "Amount": amount,
          "PartyA": phone,
          "PartyB": 600978,
          "PhoneNumber": phone,
           "CallBackURL": "https://mydomain.com/path",
         "AccountReference": "CompanyXLTD",
        "TransactionDesc": "Payment of X"
    }
## Function Below generates the mpesa password and time format.
def mpesa_time_pass():
    t=mpesa_time_stamp()
    s=str(m["paybill"]+m["passKey"]+t).encode("ascii")
    en=base64.b64encode(s)
    print(en)
    return {"time":str(t),"password":en.decode("ascii")}
def mpesa_pass_key(timestamp):
    en=str(str(m["BusinessShortCode"])+m["passKey"]+timestamp).encode("ascii")
    return base64.b64encode(en).decode("ascii")
def mpesa_time_stamp():
   d=datetime.now()
   x=d.strftime("%Y%m%d%H%M%S")
   return x
def mpesa_express(amount=1,phone=254725089717):
    time=mpesa_time_stamp()
    token=mpesa_token()
    payload=express_payload(amount,phone,mpesa_pass_key(time),time)
    print(payload)
    url='https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest'
    res=requests.post(url,headers={"Authorization":f"Bearer {token}"},data=payload)
    print(res.text)
#Function to generate mpesa token
def mpesa_token():
    s=str(m["consumer_key"]+":"+m["consumer_secret"]).encode("ascii")
    mpesaKey=base64.b64encode(s)
    #print(mpesaKey)
    #print(mpesaKey.decode("ascii"))
    newkey=mpesaKey.decode("ascii")
    url="https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"
    res=requests.get(url,headers={"Authorization":f"Basic {newkey}"})
    k=json.loads(res.text)
    return k["access_token"]
# mpesa_time_pass()
#print(mpesa_time_pass())
#print(mpesa_token())
# mpesa_express()
# print(mpesa_pass_key("34324234"))