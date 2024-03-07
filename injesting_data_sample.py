import requests, json


json_data = json.dumps({
	"level": "error",
	"message": "Message can be anything but meaning ful",
    "resourceId": "server-1234",
	"timestamp": "2022-04-15T08:00:00Z",
	"traceId": "abc-xyz-123",
    "spanId": "span-456",
    "commit": "thecommmit",
    "metadata": {
        "parentResourceId": "server-0987"
    }
})



res = requests.post('http://127.0.0.1:3000/ingest', headers = {'Content-Type':'application/json'}, data = json_data )