#!/usr/bin/python

import cgi
import cgitb
import os
import pickle
#from gen import html_res #this is the file that generates index.html. After uploading a file, I want to call it again to overwrite the existing html index file so that when the client asks for it again, it includes the newly uploadded files
#this isn't ideal, but it doesn't look like the http module gives me any easy way to select a function or customize the way thei ndex.html file
#is obtained
cgitb.enable()


def write_file(filename, fileobj): #filename and fileobj are the .filename and .file attributes of the fieldstorage object
  cwd = os.getcwd()  #the current working directory returned will actually be the directory of the http server, not the directory of the cgi-script (normally cgi-bin)
  path =  cwd + '/files/' + filename 
  #logfile.write(path)

  to_write = open(path, 'wb') #creating a file on disk with the same name as the uploaded file
  to_write.write(fileobj.read())   #read from the uploaded file and write to the opened file on disk of the same name
  to_write.close()
  fileobj.close()






fieldstorageinstance = cgi.FieldStorage()
form = fieldstorageinstance['uploaded'] #uploaded is the value of the 'name' field in the html form tag in gen_index.py 
logfile = open('logfile', 'w') #write to this if you're unsure what the output would be, so that you can see exactly. 
#logfile.write(str([i.fielanme for i in form]['uploaded']))



##test to see whether the field storage is a singular FieldStorage object (because a single file was uploaded),
#or a list of Fieldstorage objects (because multiple files have been uploaded at once).
#They need to be handled accordingly.
try:
  form.filename  #the fieldstorage object will only have a .file or .filename attribute if it isn't instead a list of objects
except:  #if there's an exception, then the object is actually a list of objects
  try: #handle the object like the list of objects that it is then  
    for item in form:   #since it's a multipart upload encoding, form is a list of fieldstorage objects. Each item is a fieldstorage object, that can be iterated over. See the cgi_python_interface.txt in the cwd   
      #if item.filename:  #You can test if the file has been uploaded by using either the file or filename attributes of the fieldstorage instance (read the documentation)
       write_file(item.filename, item.file) #call write_file and pass the filename and file attributes as arguments
  except:
      print('error dealing with multiple files')

else:  #if no exception was raised when checking for a .filename attribute, and form is therefore not a list
  try:
    write_file(form.filename, form.file)    
  except:
    print('error dealing with single file')

#################################
#below was the implementation for uploading a single file 
    # Get filename here.
#fileitem = form['filename']   #the value of the name field of the form tag element was 'filename', before I changed it to 'uploaded' above

# Test if the file was uploaded
#if fileitem.filename:
   # strip leading path from file name to avoid 
   # directory traversal attacks
#   fn = os.path.basename(fileitem.filename)
 #  open(fn, 'wb').write(fileitem.file.read())
#except:
#   message = "upload failed"
#else:
#message = './' + fn + '" was uploaded successfully'
message ='Upload successful'   




#html_res()
 
to_print= """\
Content-Type: text/html
Refresh: 1; URL='/index.html'\n 
<html>
<body>
   <p>%s</p>
</body>
</html>
""" % (message)
#notice that above there needs to be a blank line following the headers, and before the html content (hence the \n above)

print(to_print)
