import time
from datetime import datetime as dt
hosts_path=r"C:\Windows\System32\drivers\etc\hosts"
hosts_temp="hosts"  
redir="127.0.0.1"
website_list=["google.com","www.google.com"]
print(dt.now().hour)
while True:
    if(dt.now().hour>8 and dt.now().hour<19):
        print("working only")
        with open(hosts_path,'r+') as file:
            content=file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redir+" "+website)
                    file.write("\n")
    elif(dt.now().hour>9):
        with open(hosts_path,'r+') as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)   
            file.truncate()
        print("fun only")
        time.sleep(5)