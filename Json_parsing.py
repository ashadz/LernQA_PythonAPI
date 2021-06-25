import json

string = '{' \
         '"messages":[{"message":"This is the first message","timestamp":"2021-06-04 16:40:53"},{' \
         '"message":"And this is a second message","timestamp":"2021-06-04 16:41:01"}]' \
         '}'

json_text = json.loads(string)
print(json_text['messages'][1]['message'])