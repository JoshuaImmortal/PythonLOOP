import webbrowser
table = open('tablee.html','w')
table_template ="""<html lang ='en'>
<head>
<meta charset='utf-8'>
<meta http-equiv= 'X-UA compatible' content= 'IE=edge'>
<meta name='viewport' content='width=device-width'>
<title>Anime TimeTable</title>
</head>
<body>
<div id='wrapper' style='background-color: cyan;'>
<table border="1" cellspacing="5" cellpadding="20">
<caption>Anime Schedule</caption>
<thead>
<tr>
<th>Anime</th>
<th>Date</th>
<th>Time</th>
</tr>
</thead>
<tbody>
<tr>
<th>Hell's Paradise</th>
<td>Saturday</td>
<td>6:00pm</td>
</tr>
<tr>
<th>Demon Slayer</th>
<td>Sunday</td>
<td>6:00pm</td>
</tr>
</tbody>
</table>
</div>
</body>
</html>"""
table.write(table_template)
table.close()
webbrowser.open('tablee.html')