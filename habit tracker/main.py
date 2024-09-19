import requests
import datetime as dt
TOKEN = "qwertyuiop"
USER ="edb05"
pixela_endpoint = "https://pixe.la/v1/users"
graph_endpoint = f'{pixela_endpoint}/{USER}/graphs/graph1'
pixel_endpoint = f'{graph_endpoint}/20240918'
todays_date = dt.datetime.now().strftime("%Y%m%d")
headers = { # headers are used so that it cannot be seen in the api request, more ssecure way to send tokens
    "X-USER-TOKEN": TOKEN
}
def setuser():
    user_params ={
        "token": TOKEN,
        "username":USER,
        "agreeTermsOfService": "yes",
        "notMinor":"yes"
    }
    response = requests.post(url=pixela_endpoint, json=user_params)
    print(response.text)
def addgraph():
    graph_config ={
        "id": "graph1",
        'name': 'running graph',
        'unit':"km",
        'type':"float",
        'color':"ajisai"

    }

    response = requests.post(url=graph_endpoint, json= graph_config, headers=headers)
    print(response.text)


def addpixel():
    graph_config = {
        "date": todays_date,
        "quantity": "6"

    }
    response = requests.post(url=graph_endpoint,json=graph_config,headers=headers )
    print(response.text)
    print(graph_endpoint)

def updatepixel():
    
    graph_config = {
        "quantity": "2"

    }
    response = requests.put(url=pixel_endpoint,json=graph_config,headers=headers )
    print(response.text)
    

def deletepixel():
    
    response = requests.delete(url=pixel_endpoint,headers=headers )
    print(response.text)
    

deletepixel()