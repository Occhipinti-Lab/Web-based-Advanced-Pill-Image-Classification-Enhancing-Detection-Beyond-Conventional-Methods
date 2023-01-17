from flask import Flask, render_template, request, jsonify
import os
import glob

from werkzeug.utils import secure_filename
from inference import get_result

app = Flask(__name__)
app.config['UPLOAD_EXTENSIONS'] = ['.jpg','.JPG','.PNG', '.png', '.jpeg']
app.config['UPLOAD_PATH'] = 'static/input'

ROOT_DIR = '/'

@app.route('/', methods=['GET', 'POST'])
def index():
    list_data = []
    if request.method=='POST':
        file = request.files.get("file")
        input_img = glob.glob('static/input/*')
        for f in input_img:
            os.remove(f)
        filename = secure_filename(file.filename)
        if filename != '':
            file_ext = os.path.splitext(filename)[1]
            if file_ext not in app.config['UPLOAD_EXTENSIONS']:
                os.abort(400)
            file_path = os.path.join(app.config['UPLOAD_PATH'], filename)
            file.save(file_path)
            flage , text = get_result(file_path)

            if flage == True:
                # return jsonify(str(text))
                data = {
                    "Text": str(text),
                    "flage": 'True',
                }
            else:
                data = {
                    "Text": '',
                    "flage": 'False',
                }
        #
        return jsonify(data)
    return render_template('index.html')

if __name__=='__main__':
    app.run(debug=False,host='0.0.0.0', port=5001)