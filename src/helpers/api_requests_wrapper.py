# Create Helpers - requests wrapper, verification and the payload manager
# Helps you to make a POST GET PATCH PUT and DELETE
import json
import requests

# Create request function to use again and again
# Code reusability
# a custom function I created - takes URL, Auth
# we added a wrapper - we use requests() again and again
def get_request(url, auth):
    response = requests.get(url=url, auth=auth)
    return response.json()

def post_request(url, auth, headers, payload,in_json):
    post_response = requests.post(url=url, headers=headers,auth=auth, data=json.dumps(payload))
    if in_json is True:
        return post_response.json()
    return

def patch_requests(url, headers, auth, payload, in_json):
    patch_response_data = requests.patch(url=url, headers=headers, auth=auth, data=json.dumps(payload))
    if in_json is True:
        return patch_response_data.json()
    return

def put_requests(url, headers, auth, payload, in_json):
    put_response_data = requests.put(url=url, headers=headers, auth=auth, data=json.dumps(payload))
    if in_json is True:
        return put_response_data.json()
    return put_response_data

def delete_requests(url, headers, auth, in_json):
    delete_response_data = requests.delete(url=url, headers=headers, auth=auth)
    if in_json is True:
        return delete_response_data.json()
    return delete_response_data


