# ApiPoster
Python programme that posts to any api, uses an example json to built the structure and a csv to add the data

unique value is for if your JSON is {value:{rest of json}}
meaning that you could post {value1:{rest of json:""},
                             value2:{rest of json:""},
                             valuen:{rest of json:""}
                             }

this comes from the csv that you give it in settings.py

url = the URL you want to post to

filename = filename the programme looks for

uniqueKey = if the value uniqueValue should be the Key to your JSON

urlHeads = headers for your post

uniqueValue = the key that should be use to the JSON (not required) if unique key is True

time = example for if you wanted to add the epoch time of the event to the data

jsonString = example json string for your post
