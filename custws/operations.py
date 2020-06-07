import requests
import json
from .externalUrls import *
from .models import UserTaskDetails
from .internalOperations import *



def createTaskRequestPayload(custTaskId):
    q=UserTaskDetails.objects.filter(custTaskId=custTaskId)
    requestPayload={
        "custTaskId": custTaskId,
        "userId":q[0].user_id ,
        "taskName": q[0].taskName,
        "taskDescription": q[0].taskDescription,
        "taskCategory": q[0].taskCategory,
        "taskSubCategory": q[0].taskSubCategory,
        "taskAttachment1": "",
        "taskAttachment2": "",
        "taskStatus": q[0].taskStatus
    }
    return requestPayload

def sendTaskToTml(req):
    url=URL_createTicketTml
    req=req
    response = requests.post(url=url, data=json.dumps(req), headers={'Content-type': 'application/json'})
    return response.status_code


def createPaymentRequestPayload(custTaskId):
    q = UserTaskDetails.objects.filter(custTaskId=custTaskId)
    requestPayload = {
        "taskId": custTaskId,
        "amount": calculateAmount(q[0].taskRevenue,q[0].currency),
        "paymentMethod": "CREDIT CARD",
        "isPaid": True

    }
    return requestPayload

def makePaymentToBRM(req):
    url = URL_makePaymentToBrm
    req = req
    response = requests.post(url=url, data=json.dumps(req), headers={'Content-type': 'application/json'})
    return response.status_code

