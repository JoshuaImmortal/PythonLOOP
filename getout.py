import webbrowser
table = open('getout.html','w')
table_template ="""<html lang ='en'>
<head>
<meta charset='utf-8'>
<meta http-equiv= 'X-UA compatible' content= 'IE=edge'>
<meta name='viewport' content='width=device-width'>
<title>Api Table</title>
</head>
<body>
<div id='wrapper' style='background-color: cyan;'>
<table border="1" cellspacing="5" cellpadding="20">
<caption>Classwork</caption>
<thead>
<tr>
<th>Nation</th>
<th>Nation ID</th>
<th>Year</th>
<th>Population</th>
</tr>
</thead>
<tbody>
<tr>
<td>United States</td>
<td>01000US</td>
<td>2013</td>
<td>311536594</td>
</tr>
<tr>
<td>United States</td>
<td>01000US</td>
<td>2014</td>
<td>314107084</td>
</tr>
<tr>
<td>United States</td>
<td>01000US</td>
<td>2015</td>
<td>316515021</td>
</tr>
<tr>
<td>United States</td>
<td>01000US</td>
<td>2016</td>
<td>318558162</td>
</tr>
<tr>
<td>United States</td>
<td>01000US</td>
<td>2017</td>
<td>321004407</td>
</tr>
<tr>
<td>United States</td>
<td>01000US</td>
<td>2018</td>
<td>322903030</td>
</tr>
<tr>
<td>United States</td>
<td>01000US</td>
<td>2019</td>
<td>324697795</td>
</tr>
<tr>
<td>United States</td>
<td>01000US</td>
<td>2020</td>
<td>326569308</td>
</tr>
</tbody>
</table>
</div>
</body>
</html>"""
table.write(table_template)
table.close()
webbrowser.open('getout.html')