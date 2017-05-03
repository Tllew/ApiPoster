# ApiPoster
Python programme that posts to any api, uses an example json to built the structure and a csv to add the data

unique value is for if your JSON is {value:{rest of json}
meaning that you could post {value1:{rest of json:""},
                             value2:{rest of json:""},
                             valuen:{rest of json:""}
                             }

this comes from the csv that you give it in settings.py