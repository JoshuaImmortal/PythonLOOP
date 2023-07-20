import webbrowser
form = open('form.html', 'w')
style = open("style.css", "w")
style_template = """
    *{
        margin:0;
        box-sizing:border-box
    }
    #wrapper{
        border: .2rem solid green;
    }
    form{
        border: .1rem ridge red;
        width:50%;
        margin: 0 auto;
        /*height:50vh;*/
    }
"""
html_template = """<html lang = 'en'>
<head>
<meta charset= 'utf-8'>
<meta name='viewport' content='width=device-width'>
<meta http-equiv= 'X-UA compatible' content= 'IE-edge'>
<link rel="styleSheet" href="style.css">
<title>form element</title>
</head>
<body>
<div id ='wrapper'>
<form action='' method =''>
<input type='text' placeholder='Input your first name'>
<input type='password' placeholder='password'>
<button type='submit'>Sign In</button>
</form>
</div>
</body>
</html>"""
form.write(html_template)
style.write(style_template)
form.close()
style.close()
webbrowser.open('form.html')