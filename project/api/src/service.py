#importing Libraries 
import warnings
from flask_restful import Resource, Api
from flask import Flask , jsonify , request ,send_file
from flask_cors import CORS
import os 

from caption_generator import predictcatption

#checks if the folder called data exisit if not it will create a folder called data 
if not os.path.exists("data"):
    os.mkdir("data")

#setting default settings
warnings.filterwarnings("ignore")
app = Flask(__name__)
CORS(app)
api = Api(app)
pipe = None
retriver = None
reader = None 


#Endpoint 1 : Upload File 
class POST_UploadFile(Resource):
    """
    Upload Image to API Database 
    parameters:
        "file": Upload Image file
    """
    def post(self):
        try: # Exception Handling 
            if os.path.exists("attention_plot.png"):
                os.remove("attention_plot.png") 
            file = request.files.get("file")
            fileName = file.filename # getting the file name from the uploaded file 
            dataPath = os.path.join(fileName)
            file.save(dataPath)
            return jsonify({"status":"File Uploaded Successfully" ,"filePath":dataPath})
        except Exception as e:
            return jsonify({"error": str(e)})

api.add_resource(POST_UploadFile, '/uploadFile')

#Endpoint 2 : 

class POST_GenerateCaption(Resource):
    """
    Endpoint to generate captions for image 
    parameters:
        "filePath": Path of file to generate caption.
        "version" : Version of the model to be used. 
    """
    def post(self):
        try:
            file_path = request.form.get("filePath")
            model_version = request.form.get("version")
            prediction  = predictcatption(file_path,int(model_version))
            return jsonify({"prediction" :prediction})
        except Exception as e:
            return jsonify({"error": str(e)})
api.add_resource(POST_GenerateCaption, '/generateCaption')

class Post_AttentionPlot(Resource):
    """
    Endpoint to send attention plot for the image 

    """
    def post(self):
        try:
             return send_file("attention_plot.png",download_name = "attention_plot.png") 
        except Exception as e:
            return jsonify({"error": str(e)})
            

api.add_resource(Post_AttentionPlot, '/attentionPlot')


# #Flask Server Details 
if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port=8501, debug=True , threaded = True)