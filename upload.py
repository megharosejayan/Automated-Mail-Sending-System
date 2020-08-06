import xlrd
from send import mail
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
app = Flask(__name__)

@app.route('/upload')
def upload_fill():
   return render_template('initial.html')
	
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      semail = request.form['semail']
      passw = request.form['passw']
      user = request.form['content']
      gree = request.form['greeting']
      subject = request.form['subject']
      f.save(secure_filename(f.filename))

      
      
      loc = (f.filename)
      wb = xlrd.open_workbook(loc) 
      sheet = wb.sheet_by_index(0) 
      sheet.cell_value(0, 0)
      namei=sheet.cell_value(1,1)
      print(namei)
      print(gree)
      print(user)
      for i in range (0,3):
         rmail = sheet.cell_value(i,2)
         name = sheet.cell_value(i,1)
         body = gree+" "+name+","+"\n"+user
         mail(semail, passw, rmail, body, subject)
         print("mail send"+rmail)
      return 'file uploaded successfully %s' %f.filename
		
if __name__ == '__main__':
   app.run(debug = True)