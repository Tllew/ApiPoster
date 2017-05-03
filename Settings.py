from datetime import datetime

url = "http://requestb.in/u3d3rju3"

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

# {
#     "__trigger": {
#         "Booking": {
#             "Booking Reference": ""
#         },
#         "startedAt": time
#     }
# }
