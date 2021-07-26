from flask import Flask, render_template, request,url_for,redirect, abort
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER']=os.path.join(os.path.dirname(__file__),'upload')
ALLOWED_EXTENISONS=set(['txt','fasta','jpg','gif']) #define allowed file type

def file_check(filename):
        return '.' in filename and filename.rsplit('.',1)[1] in ALLOWED_EXTENISONS #check if file uploaded is in correct format

@app.route('/api/upload',methods=['POST']) #domain:https://local/api/upload
def upload_file():
    file=request.files['file']
    if file and file_check(file.filename):
        filename= secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'],filename) #file saved in local address: serve/upload
        file.save(filepath)
        filesize = os.path.getsize((filepath))
        if filesize > 2*1024*1024: # less than 2 MB allowed
            return {
                "errno": -1,
                "errMsg": 'Size has reached upper limit' # error message: larger than 2 MB
            }, 400

        with open(filepath) as file_obj:
            content = file_obj.read()
        return {
            "errno": 0,
            "errMsg": content #successful upload
        }
    else:
        return {
            "errno": -1,
            "errMsg": 'wrong file type' # error message: disallowed file type
        }, 400


# @app.route('/upload',methods=['GET'])
# def upload_template():
#     return render_template('uploadtest.html')


if __name__=='__main__':
    app.run(debug=True,port=10000) #define port:10000

