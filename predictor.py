import discord
import pandas as pd
import tensorflow as tf
import pickle

from tensorflow.keras.preprocessing.sequence import pad_sequences

with open('tokenizer.pickle', 'rb') as handle:
  tokenizer = pickle.load(handle)
model = tf.keras.models.load_model('Discord Message Classifier 62%.h5')

names = {
  0: "Alan",
  1: "Jason",
  2: "Nick",
  3: "Jaden",
  4: "Eric"
}

client = discord.Client()

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  elif message.content.startswith("_"):
    cmd = message.content.split()[0].replace("_","")
    if cmd == "guess":
      #preprocessing
      sentence = [message.content.split()[1:]]
      sentence = tokenizer.texts_to_sequences(sentence)
      sentence = pad_sequences(sentence, maxlen=190)

      #model prediction
      name_idx = int((model.predict(sentence).argmax(axis=1)))

      #output to discord
      name = names[name_idx]
      msg = "Prediction: " + name
      await message.channel.send(msg)

client.run("")
# Token removed for safety