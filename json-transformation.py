import json
from random import randint

jsonString = '{"uwinloc":{"owner_id":"uwinloc"},"facets":[{"facet_id":"240c4d8f-c2eb-4d74-8dac-6e6fe6257203","facet_name":"tag","producer_id":"api","creation_time":"2019-10-25T15:28:59.042328+02:00","last_modification_time":"2019-10-25T15:28:59.042328+02:00","type_semantic":{"@context":"http:\/\/uwinloc.com","@type":"uwl.sem.tag"},"type_representation":"uwl.repr.tag","content":[{"ID":1234,"IsLandMark":false,"Pos":{"Cart":{"X":{"Pos":-26.87196988392871,"Acc":0},"Y":{"Pos":-2.3232603540908245,"Acc":0},"Z":{"Pos":-5.703233182430267e-5,"Acc":0}},"LLA":{"Lat":-2.101032690404736e-5,"Lon":-0.00024138895720227915,"Alt":160}},"Status":"ThreeD","Reliability":100,"Algorithm":"Placed","Filtered":false}],"flight_recorder":null}],"summary":[{"facet_id":"240c4d8f-c2eb-4d74-8dac-6e6fe6257203","status":"new"}],"history":null}'

#converting json payload to byte array
myArray = bytearray()
myArray.extend(map(ord, jsonString))

#byte array is piped into data stream
#function to write into data stream here


#read from data stream (byte array will be read)
#convert to string
decodedStr = str(myArray.decode('utf-8'))

#convert string into python dict for data manipulation
payloadDict = json.loads(decodedStr)

#retrieve position info based on key 
locationObj = (payloadDict["facets"])[0]["content"][0]["Pos"]["LLA"]

#retrieve the ID of the payload
tag_id = (payloadDict["summary"])[0]["facet_id"]
print("tag id: " + tag_id )

#append the ID to the location object
locationObj["id"] = tag_id

#convert back to JSON
locationJSON = json.dumps(locationObj)
print(locationJSON)

#to be written back to data stream









