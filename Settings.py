from datetime import datetime

url = "http://requestb.in/1glkpgs1"

filename = 'basicCsv.csv'

uniqueKey = False

urlHeads = {} #headers for the post

uniqueValue = "Email"

time = int(datetime.now().timestamp())

jsonString = {
    "Customer":{
        "Email":"",
        "First Name":"",
        "Last Name":""
    }
}
