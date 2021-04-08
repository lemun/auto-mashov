import pyimgur
from discord_webhook import DiscordWebhook, DiscordEmbed
import json
import yagmail


class Webhook:

    def app():
        #CONFIG
        config_path = (r"./config/main.json")
        with open(config_path) as data:
            config = json.load(data)
        CLIENT_ID = config["client_id"]
        webhook_url = config["webhook_url"]
        webhook_user = config["webhook_user"]
        version = config["version"]
        #CONFIG

        #CONFIG for MAIL
        config_path2 = (r"./config/mail.json")
        with open(config_path2) as data2:
            config2 = json.load(data2)
        guser = config2["guser"]
        gpass = config2["gpass"]
        tomail = config2["tomail"]
        subject = config2["subject"]
        content = config2["content"]
        
        #CONFIG for MAIL

        PATH = './img/proof.png'

        im = pyimgur.Imgur(CLIENT_ID)
        uploaded_image = im.upload_image(PATH, title="Uploaded with PyImgur for Mashov Bot")
        image_link = uploaded_image.link
        
        content = content + image_link
        try:
            #initializing the server connection
            yag = yagmail.SMTP(user=guser, password=gpass)
            #sending the email
            yag.send(to=tomail, subject=subject, contents=content)
        except:
            print("Error, email was not sent")


        
        webhook = DiscordWebhook(url=webhook_url, username=webhook_user)

        info_myclass = '?'
        info_myschool = '?'
        info_fullname = '?'

        embed = DiscordEmbed(
        description="ההצהרת קורונה היומית שלך נחתמה בהצלחה!", color='00ff00'
        )
        embed.set_author(
            name="בוט משוב",
            url="https://github.com/lemun",
            icon_url="https://web.mashov.info/students/images/logo_students.png",
        )
        embed.set_footer(text="Running Version " + version)
        embed.set_timestamp()

        embed.add_embed_field(name="שם מלא: ", value=info_fullname, inline=True)
        embed.add_embed_field(name="כיתה: ", value=info_myclass, inline=True)
        embed.add_embed_field(name="בית ספר: ", value=info_myschool, inline=True)
        embed.add_embed_field(name="הוכחה:", value=image_link, inline=True)


        webhook.add_embed(embed)
        response = webhook.execute()
