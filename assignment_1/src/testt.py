import os
abs_path = os.path.dirname((os.path.abspath(__file__)))
html_path = abs_path+"\\result.html"
    
html_file = open(html_path, 'r', encoding='utf-8')

data = html_file.read()

data1="""
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>Military Aircraft</h1>
</body>
</html>
"""

print(html_file.read())