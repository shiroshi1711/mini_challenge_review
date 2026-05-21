#get all todos and print only the completed one
#post a new todo with your chore name
#print response and see what the server says back

import requests

url = "https://jsonplaceholder.typicode.com"
url1 = f'{url}/todos'
response = requests.get(f"{url}/todos")
todos = response.json()

if response.status_code == 200:
    print("success!")
    completed = [todo for todo in todos if todo ["completed"]]
    print(completed[:3])
else:
    print(f"Error : {response.status_code}")


new = {
    "title" : "do the laundry",
    "completed" : True,
    "userId" : 1
}

post_new = requests.post(url1, json=new)

if post_new.status_code == 201 :
    print(f"Success!, code: {post_new.status_code}")
else:
    print(f"An error occurred!, {post_new.status_code}")