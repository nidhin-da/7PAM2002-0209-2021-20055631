from turtle import width
import streamlit as st 
from modules.file_management import FileManagement
from modules.api_request import APIRequest

st.set_page_config(layout="wide")
import time

class IMG:

    def home_page(self):                                                        # created function for home page 
        trigger = True                                                          # creating a trigger variable
        st.title("Image Caption Generator",anchor="title")                      # Creating tile page
        uploadSection, captionGenrationSection = st.columns( [0.2, 0.4])        # Setting up columns 
        #Contents inside upload Section 
        with uploadSection: 
            # created input for dynamic API endpoint  
            st.caption("Setup API Connection")
            endpoint_address = st.text_input('Enter API endpoint address')
            if endpoint_address != "":                                          # checking if the values are in the endpoint variable 
                trigger = False                                                 # Changing trigger value 
            uploadFileEndpoint = endpoint_address+"/uploadFile"
            generateCaptionEndpoint = endpoint_address+"/generateCaption"
            attentionPlotEndpoint = endpoint_address+"/attentionPlot"

            if trigger is False:                                                # if trigger is false then upload file 
                st.success("Address Updated")
            st.caption("Select Image to generate caption")
            image_path = FileManagement().file_input()                          # File Input module                      
        
            if image_path is not None:                                          # check if file image is present , then display it
                st.image(image_path, caption=None, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")

        with captionGenrationSection : 
                st.write("Select Model")
       
                option = st.selectbox("Select models trained with varying training sample" ,(1,2,3,4,5) ,disabled= trigger ,help="Upload a file to proccede")
                st.caption("Model 1 is trained with the least amount of data and Model 5 with the largest")
                if image_path is not None:
                    if st.button("Generate Caption",key="generatecaptionbtn"):
                        with st.spinner("Generating Caption"):
                            uploadPath = APIRequest.uploadIMage(image_path , uploadFileEndpoint)
                            # if uploadPath is not None :
                            st.info('File Uploaded to API', icon="ℹ️")
                            captionsFromAPI = APIRequest.captionGenerator(uploadPath ,option , generateCaptionEndpoint)
                                    
                            st.info('Captions Generated', icon="ℹ️")
                            attentionplotGenerated = APIRequest.attentionPlot(attentionPlotEndpoint)
                            if attentionPlotEndpoint  == "no_data_found":
                                st.info('Unable to Retrieve Attention Plot', icon="ℹ️")
                            else:
                                st.info('Attention Plot Generated', icon="ℹ️")
                                st.success(captionsFromAPI, icon="✅")
                                st.image(attentionplotGenerated,caption = captionsFromAPI)
                                #st.balloons()
                                                        
            
IMG().home_page()