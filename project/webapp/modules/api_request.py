import requests

class APIRequest:

    def uploadIMage(imagePath , endpointURL):
        file = imagePath
        payload={}
        files=[
        ('file',(file,open(file,'rb'),'image/jpeg'))
        ]
        headers = {}

        response = requests.request("POST", endpointURL, headers=headers, data=payload, files=files)
        contents_response = response.json()

        path = contents_response["filePath"]
        return path
    
    def captionGenerator(imagePath,modelVersion,endpointURL):
        payload={'filePath': imagePath,
        'version': modelVersion}
        files=[

        ]
        headers = {}
        response = requests.request("POST", endpointURL, headers=headers, data=payload, files=files)
        result = response.json()['prediction']
        x=" ".join([str(i) for i in result])
        #replace "<end>" with ""
        caption = x.replace("<end>" , "")
        print(x)
        return caption
            
    def attentionPlot(endpointURL):

        try:
            payload={}
            files={}
            headers = {}
            response = requests.request("POST", endpointURL, headers=headers, data=payload, files=files)
            save_file = open(r"data\attention_plot.png", "wb")
            save_file.write(response.content)
            save_file.close()
            return r"data\attention_plot.png"
        except Exception as e:
            print(e)
            return "no_data_found"

