# Mashov Covid-19 Automated Filler (+ Discord Webhook Integration)
A Python Application written with Python using Selenium and some other libs
## Features
Correctly (Version v3.1) the only feature is a single webhook that is either sent when the login to the Mashov system via the API was successful or was a fail. more features in the future to come and you can feel free to continue my work by forking but NOT by uploading my files again somewhere else / on your own github repository.
## Install
Use [PIP](https://pip.pypa.io/en/stable/) to install the following packages that are needed to run this app properly:
1. discord-webhook
2. requests
3. datetime
4. json
* If I forget something just download the package that is causing the error.
## Usage
in ./config/main.json find this code:
```
{
    "user": "?",
    "pass": "?",
    "school": "?",
    "client_id": "?",
    "webhook_url": "?",
    "webhook_user": "MashovAPI",
    "version": "v3.1" 
}
```
Replace the following:
* user: with your Mashov username
* pass: with your Mashov pass
* school: with your school id(semel)
* client_id: with your imgur API client id(Google how to get it)
* webhook_url: with your Discord Webhook URL
## Legal
DISCLAIMER: This is not affliated, endorsed or certified by Mashov. This is an independent and unofficial project that is strictly for educational purposes only and not intended to cause any harm. I am not responsible for anyone who decided to download my app and use it against my will and Mashov's will. Use at your OWN risk ONLY.
## Explanation of what the app does:
1. Check if you set "headless_option" to 1 or 2 or something else(if 1: show browser. if 2: hide browser. if something else: print error and show browser)
2. Go to the Mashov login page and login
3. Go to the Mashov corona daily statement and fill it
4. Take a screenshot
5. Upload said screenshot to imgur
6. Send a Discord webhook with said screenshot
7. Delete said screenshot
8. Finish
