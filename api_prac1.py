
import requests 
while True:
    user_name=input("User Name(Press 'n' to exit):")
    url_=f'https://api.github.com/users/{user_name}/repos'
    response=requests.get(url_)
    data=response.json()
    if response.status_code!=200:
        print("Error identidying user-->Try Again")

    elif user_name=='n':
        break
    else:
        count=0
        print("*"*80)
        print("\t\t\t\t{}".format(user_name))
        print("*"*80)
        for repo in data:
            print(f"Repo :{repo['name']}\nLink :{repo['html_url']}")
            count+=1
        print("*"*50)
        print("TOTAL REPOS:{}".format(count))
        print("*"*80)

