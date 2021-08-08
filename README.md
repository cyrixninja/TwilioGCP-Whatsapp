# TwilioGCP-Whatsapp
App to Control Google Cloud Platform Using Whatsapp
# Create an Twilio and Google Cloud Account to Try it
# Step 1 Create an VM Instance in Google Cloud Compute Engine
![Step1Img](https://github.com/cyrixninja/TwilioGCP-Whatsapp/blob/main/Image/7.png?raw=true)
# Step 2 SSH into VM and Install 
```
sudo apt-get install git python3 python3-pip
pip3 install twilio requests flask
```
# Step 3 Git Clone this Repo
```
git clone https://github.com/cyrixninja/TwilioGCP-Whatsapp
```
![Step3Img](https://github.com/cyrixninja/TwilioGCP-Whatsapp/blob/main/Image/2.png?raw=true)
 
# Step 4 Cd into the Directory
```
cd TwilioGCP-Whatsapp
```
![Step4Img](https://github.com/cyrixninja/TwilioGCP-Whatsapp/blob/main/Image/3.png?raw=true)

# Step 5 Run the Python Script
```
python3 bot.py
```
![Step5Img](https://github.com/cyrixninja/TwilioGCP-Whatsapp/blob/main/Image/4.png?raw=true)

# Step 6 Open another SSH Session and Run the NGROK Server
```
cd TwilioGCP-Whatsapp
chmod +x ngrok
./ngrok http 5000
```
![Step6Img](https://github.com/cyrixninja/TwilioGCP-Whatsapp/blob/main/Image/5.png?raw=true)

# Step 7 Copy the Ngrok URL and Paste it in your twilio console whatsapp sandbox
https://www.twilio.com/console/sms/whatsapp/sandbox
![image](https://user-images.githubusercontent.com/61012869/128624742-4ef078af-5ff3-4342-a467-a8cf8f95d273.png)

Add /bot at the end after pasting the url in twilio console and Save it.

# Congratulations,Now you're ready to go



