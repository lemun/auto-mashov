import pyimgur
from discord_webhook import DiscordWebhook, DiscordEmbed
import json

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

        PATH = './img/proof.png'

        im = pyimgur.Imgur(CLIENT_ID)
        uploaded_image = im.upload_image(PATH, title="Uploaded with PyImgur for Mashov Bot")
        image_link = uploaded_image.link

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
