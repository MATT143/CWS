from .models import UserTaskDetails

def generateCustTaskId():
    q=UserTaskDetails.objects.all().order_by('-custTaskId')
    currentTaskid=q[0].custTaskId
    custTaskId=currentTaskid+1
    return custTaskId

def calculateAmount(revenue,currency):
    curr={'rupees':1,'dollar':75.61,'euro':85.54,'pound':95.86,'yen':0.69}
    amount=float(revenue)*(curr[currency])
    return amount


