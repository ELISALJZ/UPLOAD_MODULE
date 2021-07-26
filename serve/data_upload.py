from flask import Flask, render_template, request,url_for,redirect, abort
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER']=os.path.join(os.path.dirname(__file__),'upload')
ALLOWED_EXTENISONS=set(['txt','fasta'])

def file_check(filename):
        return '.' in filename and filename.rsplit('.',1)[1] in ALLOWED_EXTENISONS

@app.route('/api/upload',methods=['POST'])
def upload_file():
    file=request.files['file']
    if file and file_check(file.filename):
        filename= secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'],filename)
        file.save(filepath)
        filesize = os.path.getsize((filepath))
        if filesize > 1000*1024:
            return {
                "errno": -1,
                "errMsg": 'Size has reached upper limit'
            }, 400

        with open(filepath) as file_obj:
            content = file_obj.read()
        return {
            "errno": 0,
            "errMsg": content
        }
    else:
        return {
            "errno": -1,
            "errMsg": '不支持的文件类型'
        }, 400


# @app.route('/upload',methods=['GET'])
# def upload_template():
#     return render_template('uploadtest.html')


if __name__=='__main__':
    app.run(debug=True,port=10000)

