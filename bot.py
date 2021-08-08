from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse
import os


app = Flask(__name__)


@app.route('/bot', methods=['POST'])
def bot():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()
    responded = False
    if 'help' in incoming_msg:
        helpmsg="""
        
        This app can perform following activities:
        Create an Cloud Storage Bucket
        Create an VM Instance
        Create an GKE CLuster
        Execute Command using gcloud
        """
        msg.body(helpmsg)
        responded = True
        return str(resp)
    if 'createbucket' in incoming_msg:
        abc= incoming_msg.split()
        area=(abc[1])
        name=(abc[2])
        text=("Creating a Bucket Named"+"  "+name+"  "+"in the area"+"  "+area)
        command=("gsutil mb -l" +" "+area+" " +"gs://"+name+"/")
        msg.body(text)
        os.system(command)
        return str(resp)
    if 'createinstance' in incoming_msg:
        instancetxt=incoming_msg.split()
        name=(instancetxt[1])
        zone=(instancetxt[2])
        command=("gcloud compute instances create"+" "+ name+" "+"--zone"+" "+zone)
        msg.body(command)
        os.system(command)
        return str(resp)
    if 'createcluster' in incoming_msg:
        clustertxt=incoming_msg.split()
        name=(clustertxt[1])
        nodes=(clustertxt[2])
        zone=(clustertxt[3])
        command=("gcloud container clusters create"+" "+name+" "+"--num-nodes="+nodes+"  "+"--zone"+" "+zone)
        msg.body(command)
        os.system(command)    
        return str(resp)
    if 'gcloud' in incoming_msg:
        command=incoming_msg
        msg.body(command)
        os.system(command)
        return str(resp)
    
if __name__ == '__main__':
    app.run()
