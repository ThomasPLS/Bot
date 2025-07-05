import discord
import os
import random
import asyncio

# Le token est maintenant lu depuis les variables d'environnement
TOKEN = os.getenv("TOKEN")

# ID du canal où envoyer les images
CHANNEL_ID = 1265631325017215006

# Dossier contenant les images
IMAGE_FOLDER = "images"

intents = discord.Intents.default()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"Connecté en tant que {client.user}")
    channel = client.get_channel(CHANNEL_ID)

    while True:
        try:
            # Liste des images
            images = [f for f in os.listdir(IMAGE_FOLDER) if f.endswith(('.png', '.jpg', '.jpeg', '.gif'))]
            if not images:
                print("Aucune image trouvée dans le dossier.")
                await asyncio.sleep(3600)
                continue

            image_name = random.choice(images)
            image_path = os.path.join(IMAGE_FOLDER, image_name)

            with open(image_path, 'rb') as f:
                picture = discord.File(f)
                await channel.send(file=picture)

            print(f"Image envoyée : {image_name}")
            await asyncio.sleep(3600)  # Attendre 1 heure

        except Exception as e:
            print(f"Erreur : {e}")
            await asyncio.sleep(3600)

client.run(TOKEN)
