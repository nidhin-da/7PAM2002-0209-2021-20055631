import streamlit as st 
import os 
import glob

TEMP_DIR = r"data"
#create TEMP_DIR if not exists
if not os.path.exists(TEMP_DIR):
    os.makedirs(TEMP_DIR)

class FileManagement:

    def file_input(self):
    # try:
        file_upload = st.file_uploader("")
        if file_upload is not None:
            fileSavePath = FileManagement().saveFile(file_upload)
            #Filemanagement().delete_files(TEMP_DIR)
            if fileSavePath == None:
                FileManagement().file_input()
            return fileSavePath
        else:
            return None




    def saveFile(self, uploadedfile):
        # try:
            if not os.path.exists(TEMP_DIR):
                    os.mkdir(TEMP_DIR)
            
            file_path = os.path.join(TEMP_DIR,uploadedfile.name)
            with open(file_path,"wb") as f:
                f.write(uploadedfile.getbuffer())
            return file_path
        # except Exception as e:
        #     print(e)


    def delete_files(self):
        try:
            #remove all files in the directory
            for file in glob.glob(TEMP_DIR + '/*'):
                os.remove(file)
        except Exception as e:
            print(e)

        