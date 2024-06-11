from discord_webhook import DiscordWebhook
import sys
import os

path = sys.argv[1]

webhook = DiscordWebhook(url="WebHookURLを入れてください")
basename = os.path.basename(path)
username = os.getlogin()

# send two images
with open(path, "rb") as f:
    webhook.add_file(file=f.read(), filename=basename)

response = webhook.execute()

webhooka = DiscordWebhook(url="WebHookURLを入れてください", content=f"{username}さんのアップロード")
responsea = webhooka.execute()
