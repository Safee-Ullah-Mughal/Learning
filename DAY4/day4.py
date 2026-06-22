import requests
import json

url='https://jsonplaceholder.typicode.com/posts'

data={"Name":"Safee Ullah",
      "Email":"safeeu@gmail.com",
      "password":"Pass123"}

response=requests.post(url,json=data)

print("Status Code",response.status_code)
serverReply=response.json()
print(json.dumps(serverReply,indent=4))


def create_post(title, body, user_id):
    name=input("Enter you Name: ")
    email=input("Enter your email")

    url1='https://jsonplaceholder.typicode.com/posts'
    data1={"Name":name,
          "EMail":email}
    
    resp=requests.post(url1,json=data1)

    statuscode=resp.status_code
    print("Status Code: ",statuscode)

    serreply=resp.json()
    print(json.dumps(serreply, indent=4))

    return (resp, serreply)


#create_post("Abdullah", "Abdullah@gmail.com",101)


def adduser(Name, Email):
    Data={"Name":Name,
          "Email":Email}
    
    with open("newuserdata.txt","a") as file:
        newdata=json.dumps(Data)

        file.write(newdata + "\n")
    

adduser("Hamna","Hamna@gmail.com")