#!/usr/bin/python

import os
import cgi
cwd_files = os.listdir() # list of files in the cwd, as strings
#generate html for directory listing

def itemize_files(dir):
  for item in dir:
      #res = "<li><a href='{f:}'>{f:}</li>".format(f=item)
      res = "<li><a href='{source:}'>{name:}</li>".format(source='../files/'+item, name=item)
      yield res


html_outline_start = """
<!DOCTYPE html>

<html>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<!--using the viewport is essential. The media queries wouldn't work without it.-->

<head>
        <title>pyserve</title>

<style>

body {
background-color: #f5f393;}







@media (max-width: 600px) {
body{
background-color: #f5f393;;
font-size: 20px;*/
}

p{
font-size: 20px;} /*this is the text next to the button e.g. 'Files:' */

/*change the text inside a button*/
input{
font-size: 20px;}

#div{
#font-size: 20px;}

h1{
font-size: 50px;
}
#uparea {
margin : auto;}

#dirlist {
margin: auto;}
}


@media (min-width: 600px) {
/* tablets, laptops, desktops. My tablet, for example, is 800 in width and 1200 in height in portrait mode */
body{
/*background-color: white;*/
font-size: 25px;
}

p{
font-size: 25px;} /*this is the text next to the button e.g. 'Files:' */

/*change the text inside a button*/
input{
font-size: 25px;}

#div{
#font-size: 25px;}

h1{
font-size: 40px;
}

#uparea {
margin : auto;}

#dirlist {
margin: auto;}
}


</style>

</head>

<body>

<div id="uparea">

<h1>Upload Files</h1>
   <form enctype = "multipart/form-data" action = "/cgi-bin/up_file.py" method = "post" >
   <p>File: <input type="file" name="uploaded" multiple/></p>
   <p><input type="submit"value="Upload"/></p>
   </form>
 
</div>

<br>
<br>
<div id="dirlist">
<h1>Directory listing/</h1>
<form action='/cgi-bin/gen_index.py' method='get'>
<input type='submit' value='refresh'/>
</form>
<br>
<br>

<ul>
"""
######################################################################

html_outline_end = """
</ul>
</div>
</body>
</html>
"""

#def html_res():
#  html_doc = 'Content-Type: text/html\n'
#  html_doc += html_outline_start
#  for i in itemize_files(cwd_files):
#    html_doc+=i

#  html_doc += html_outline_end
#  print(html_doc)






def html_res():
    html_doc = html_outline_start
    cwd = os.getcwd().split('/')
    print(cwd)
    abs_path = '/'.join(cwd[:]) + '/files/'     

    for i in itemize_files(os.listdir(abs_path)):
       html_doc+=i
    html_doc += html_outline_end
    print(html_doc)



html_res()



