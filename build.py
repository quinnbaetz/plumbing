import base64
src=open('src.html').read()
img='data:image/jpeg;base64,'+base64.b64encode(open('upper.jpg','rb').read()).decode()
out=src.replace('__IMG__',img)
open('smart-recirc.html','w').write(out)
open('index.html','w').write(out)
