import os
import json

current_dir = os.path.dirname((os.path.abspath(__file__)))
json_path = current_dir+"\myTest.json"

#print(json_path)  

# Opening JSON file
# f = open(json_path)
  
# # returns JSON object as 
# # a dictionary
# data = json.load(f)
  
# # Iterating through the json
# # list
# print(type(data))
  
# # Closing file
# f.close()

html_path= current_dir+"\myTest.html"

HtmlFile = open(html_path, 'r', encoding='utf-8')
data = HtmlFile.read()
print(data)