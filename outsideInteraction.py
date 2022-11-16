personalkey = "bea4b2f859d90f424de7826877067770"
token = "7b908de58dc85cd27fa1f72e87e5c40fb1729f52631e89589d770cdabf119293"
idlist = "6374d124be349301beb0040c"

# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
import json


def createCard(name,description):
    url = "https://api.trello.com/1/cards"

    headers = {
    "Accept": "application/json"
    }

    query = {
    'idList': idlist,
    'key': personalkey,
    'token': token,
    "name":name,
    "desc" : description

    }

    response = requests.request(
    "POST",
    url,
    headers=headers,
    params=query
    )

#     print(response)

#     card_id = json.loads(response.text)['id']
#     query = {
#     'idList' : idlist,
#     'key': personalkey,
#     'token': token,
#     'id' : card_id,
#     'color':'red'
# }

#     response = requests.request(
#     "POST",
#     url,
#     headers=headers,
#     params=query
#     )
#     print(response.text)

createCard("vasigay","very gay")