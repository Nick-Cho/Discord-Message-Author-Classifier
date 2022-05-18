# Discord Message Author Classifier
Created a Discord bot that predicts that author of a message sent with a 64% accuracy. The bot was created using a Tensorflow **Recurrent 
Neural Network** to train the model on 5 years worth of message history. Discord is a platform for communication through chatting and audio in the form of chat rooms. 
The Discord API was used to create the bot and its message scraping and author predicting functionality. 
![Example Prediction](https://github.com/Nick-Cho/Discord-Message-Author-Classifier/blob/master/example-prediction.png)
![Example Message](https://github.com/Nick-Cho/Discord-Message-Author-Classifier/blob/master/example-message.png)
*This message was included in the .csv file used to train the RNN*
### Message Scraping Functionality
In the **message_scraper.py** I created a script that the bot used to filter through messages sent in a server text channel and output the message data as well as the author 
of the message into a .csv file. Not all messages were recorded from the text channel due to the usability of some messages.</br>
Messages that were filtered out from the scraping process included:</br>
- Messages that "pinged" users. In discord it is possible to send users a notification through a server text channel by typing "@" followed by their name. As this is usually 
done to get a user's attention it is not usually followed by any messages so every user would have data sending this type of message
- Messages beginning with ":" often denote the user of an emoticon and most of the time that emotes are used at the start of a sentence it is the only thing sent in the same message in our server
- Messages that included links were also removed for simillar reasoning as the pings
- Other discord bot commands were also removed as they would be called by every user (includes the removal of the messages that start with "-" and ";;") </br>
*.csv file is not included for privacy reasons*
</br>

### RNN Training
Only messages of word length 9 or greater were passed into the bot to train as messages with less word length are often more repeatable among users (e.g. phrases such as "lol", "lmao")
. This disclusion of shorter length words improved the model's accuracy despite the decrease in data. Additionally there was an imbalance in the data that was accounted for, the amount
of messages that I had sent were significantly above the rest of the users so when I discluded messages of word length 8 and under I also cut out some of my message data so the
model would be more practical and generalize better to new messages.

![Balancing Data](https://github.com/Nick-Cho/Discord-Message-Author-Classifier/blob/master/cutting-data.png)

Additionally, the user tree had very little messages after filtering out shorter messages so I used **oversampling** on the training data set to account for this which brought up
the bot's accuracy ~4% by allowing the bot to get more familliar with this user's speech patterns.

![OverSampling](https://github.com/Nick-Cho/Discord-Message-Author-Classifier/blob/master/oversampling.png)

### Results
The bot has an accuracy of 64% which isn't ideal for commercial situations however, due to the nature of the data from the messages this was not a bad outcome. This server that I sampled data from is used recreationally so normal speech patterns used day to day conversation was often not followed and all users would often use the same "slang" making the model receive some overlapping data. Additionally, using the text feature of Discord is not the primary form of communication as the calling feature is often opted for, the users in our server often send very short messages, spam (as seen in the example below), as well as song lyrics. Although there were a lot of messages gathered from message scraping, the majority of the data had to be ommitted due to the quality of the data decreasing the quality of the model.

![Spam Example](https://github.com/Nick-Cho/Discord-Message-Author-Classifier/blob/master/spam-example.png)
