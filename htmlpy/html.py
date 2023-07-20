import webbrowser;
sample = open('index.html', 'w')
code = """<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Form</title>
</head>
<body>
 <div id= 'wrapper'>
    <form action='' method=''>
        <input type='text' placeholder='enter your name'>
        <input type='password' placeholder='enter your password'>
        <button>Login</button>
    </form>
 </div>
</body>
</html>"""
sample.write(code)
sample.close()
webbrowser.open('index.html') 