'''This is a discord 'chatbot' named 'Persy' that operates on keywords entered by the user 
   and selects a random hard-coded response or sends data through an API'''


import discord


#Used to get a link or a string from an API
import requests

#Used to read .json files
import json

import random

#Used to reduce the words in the user's input to their root
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

import re

#Used to detect profanity in user's input
from better_profanity import profanity

#Used to get recent news
from GoogleNews import GoogleNews

#ayncpraw operates in an asyncronous environment and is used to get posts from reddit
import asyncpraw

#Used to read .env files, where the discord token is.
import os
from dotenv import load_dotenv

#Error message that is used for handling errors related to API connectivity 
error_handler = 'An unknown error has occured. Please repeat or enter another command :)'

submission_list = []

def main():

    #Open the intents file where the keywords and hard-coded responses are
    words = json.loads(open('words.json').read())


    keywords = []

    answers = []

    
    #Read through the file and get the input and output as a list for every category

    for word in words['words']:
            keywords.append(word['keywords'])
            answers.append(word['output'])
    
    

    
    greetingI, greetingO = keywords[0], answers[0]
    generalI, generalO = keywords[1], answers[1]
    whoI, whoO = keywords[2], answers[2]
    ageI, ageO = keywords[3], answers[3]
    helpI, helpO = keywords[4], answers[4]
    joke = keywords[5]
    ping = answers[6]
    quotes = keywords[7]
    bitcoin = keywords[8]
    dogecoin = keywords[9]
    litecoin = keywords[10]
    awwI, awwO = keywords[11], answers[11]
    fun = keywords[12]
    news = keywords[13]
    error = answers[14]
    profanity1 = answers[15]
    loveI, loveO = keywords[16], answers[16]
    memesI, memesO = keywords[17], answers[17]
    funnyI, funnyO = keywords[18], answers[18]
    natureI, natureO = keywords[19], answers[19]
    picsI, picsO = keywords[20], answers[20]
    artI, artO = keywords[21], answers[21]
    foodI, foodO = keywords[22], answers[22]
 






    client = discord.Client()
    
    #Registering the on_ready event from the discord.py library

    @client.event
    async def on_ready():
        '''Logs in as the bot, 
           adds a discord activity from the discord.py library'''
        print('Logged in as {0.user}'.format(client))
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="Persy I need help!"))
   
    
    #Registering the event on_message from the discord.py library

    @client.event
    async def on_message(message):
        '''If a user sends a message containing the word 'persy', alterthe output accordingly'''
        
        #If the message is from the bot, do nothing.
        if message.author == client.user:
                return None

        #If a the message contains the bot's user ID, send a random response from the corresponding list

        if message.content in [f'<!@{client.user.id}>', f'<@{client.user.id}>']:
            await message.channel.send(random.choice(ping))



        #Checking if persy is in the user's input, ONLY then check for matches

        if 'persy' in message.content.lower():


            user_input = Stemmer(message.content)

            
            
            #Initialize the values of variables that will determine how the bot behaves
            
            
            #Output stands for the bot's response
            output = '??'  
            
            
            
            
            
            #Checks if the bot will post an image from reddit or not
            #The value changes to True when certain keywords are detected
            image_checker = False 
            
            
            
            
            
            #Changes the subreddit depending on the keywords detected.
            subreddit_checker = 'something'

            
            
            
            #Loops that read though the keywords list
            #And use the find_keywords function to determine if these keywords are in the stemmed user's input
            
            
            for element in greetingI:
                if find_keywords(element)(user_input) is not None:
                    output = random.choice(greetingO)

            for element in generalI:
                if find_keywords(element)(user_input) is not None:
                    output = random.choice(generalO)
    
            for element in whoI:
                if find_keywords(element)(user_input) is not None:
                    output = random.choice(whoO)
        
            for element in ageI:
                if find_keywords(element)(user_input) is not None:
                    output = random.choice(ageO)
                
            for element in helpI:
                if find_keywords(element)(user_input) is not None:
                    output = str(helpO)
            
            for element in joke:
                if find_keywords(element)(user_input) is not None:
                    output = get_joke()

            for element in quotes:
                if find_keywords(element)(user_input) is not None:
                    output = get_quote()
            
            for element in fun:
                if find_keywords(element)(user_input) is not None:
                    output = get_fun_fact()
            
            for element in bitcoin:
                if find_keywords(element)(user_input) is not None:
                    output = get_bitcoin()
            
            for element in dogecoin:
                if find_keywords(element)(user_input) is not None:
                    output = get_dogecoin()
            
            for element in litecoin:
                if find_keywords(element)(user_input) is not None:
                    output = get_litecoin()
            
            for element in loveI:
                if find_keywords(element)(user_input) is not None:
                    output = random.choice(loveO)  

            for element in news:
                if find_keywords(element)(user_input) is not None:
                    
                    #Checks if the user typed a '/' before a word
                    #Calls the get_news function which finds recent news related to that
                    
                    if search := re.findall(r'[/]\S*', user_input):
                        s = ''
                        search = s.join(search)
                        search = search.strip('/')
                        output = get_news(search)
                    else:
                        output = 'What should I find news about? Make sure to type "/" before anything you want me to search!'
                        break
            

            #Subreddit_checker is changed according to the keywords
            #And image_checker is changed to True as all of these keywords are related to images
            
            for element in awwI:
                if find_keywords(element)(user_input) is not None:
                    image_checker = True
                    subreddit_checker = 'aww'
                    output = random.choice(awwO)

            for element in memesI:
                if find_keywords(element)(user_input) is not None:
                    image_checker = True
                    subreddit_checker = 'memes'
                    output = random.choice(memesO)
            

            for element in picsI:
                if find_keywords(element)(user_input) is not None:
                    image_checker = True
                    subreddit_checker = 'itookapicture'
                    output = random.choice(picsO)


            for element in natureI:
                if find_keywords(element)(user_input) is not None:
                    image_checker = True
                    subreddit_checker = 'earthporn'
                    output = random.choice(natureO)

            for element in artI:
                if find_keywords(element)(user_input) is not None:
                    image_checker = True
                    subreddit_checker = 'art'
                    output = random.choice(artO)
            
            for element in funnyI:
                if find_keywords(element)(user_input) is not None:
                    image_checker = True
                    subreddit_checker = 'funny'
                    output = random.choice(funnyO)
                        

            for element in foodI:
                if find_keywords(element)(user_input) is not None:
                    image_checker = True
                    subreddit_checker = 'foodporn'
                    output = random.choice(foodO)





            # Now, if the output hasn't changed it means that
            #There are no keywords found, thus a random 'error' response is returned
        
            if output == '??':
                for element in error:
                    output = random.choice(error)
            
            

        
            


            #If the user types only the word 'persy', select a random string from the list possible_outcomes

            if message.content.lower() == 'persy'.strip(' '):
                possible_ouputs = ['Yes?', "You can always ask for help, don't be shy!", 'How can I help you?', "What's up?", "Yes! That's me!", "Look at what I am playing!!"]
                output = random.choice(possible_ouputs)



            #Checks if profanity is detected in the user's input using the better_profanity.py library

            if profanity.contains_profanity(message.content):
                image_checker = False
                for element in profanity1:
                    output = random.choice(profanity1)

            
            
            if output == helpO:
                #Using discord's embed method to create a neatly organised text!
                embedV = discord.Embed(title="*Hey, I'm Persy!!*", description=output, color=0x8040C0)
                embedV.add_field(name='Chat!', value="Yes! I can chat with humans, although I may not understand every word I'll do my best to answer! You can ask for my age, how am I, and other general questions!!", inline=False)
                embedV.add_field(name='Make your mood when you are sad!', value="Just tell me that you are not feeling well and I'll send you something to make you happy! :)", inline=False)
                embedV.add_field(name='Jokes', value="You can ask me for a joke! Some of them are funny!", inline=False)
                embedV.add_field(name='Inspirational quotes', value="I can get you meaningful quotes from the internet in case you feel the need to be inspired", inline=False)
                embedV.add_field(name='A fun fact!', value="Ask for an interesting fun fact, that I am sure you don't know about!", inline=False)
                embedV.add_field(name='The price of crypto!', value="You can ask for the current price of bitcoin, litecoin and dogecoin in US dollars!!", inline=False)
                embedV.add_field(name='Recent News!', value="Ask me to get you news from Google! Make sure to include a '/' before the thing you want news about so I can understand and provide you with the correct results!!", inline=False)
                embedV.add_field(name='Memes!', value="Yes I can also send memes! Ask for it!", inline=False)
                embedV.add_field(name='Funny pictures', value="These pictures come from reddit, in r/funny!", inline=False)
                embedV.add_field(name='Art', value="I love art, if you ask me to bring you some you will also be amazed!", inline=False)
                embedV.add_field(name='Food.', value="Are you hungry? I can't bring you food unfortunately, but I can send you pictures that will increase your appetite", inline=False)
                embedV.add_field(name='Landscapes and pictures of earth', value="I love nature, it has the most unique and beatiful places! Ask for a picture of a landscape or something pretty and I'll make sure to scavage the internet and get some for you", inline=False)
                embedV.add_field(name='Photography', value="Come on fellow human, what are you waiting for! Ask for a nice photo!", inline=False)
                await message.channel.send(embed=embedV)
            else:
                await message.channel.send(output)
                



        
                if image_checker is True:
                    image_list = []
                    reddit = asyncpraw.Reddit(client_id='dunp-xkpVUj2TypGsRa9mw',
                    client_secret='jT5pdNSTrleDfipmJxsE_Tan2yZHcg', user_agent='Persy')
                
                    #Determines the subreddit...
                    subreddit = await reddit.subreddit(subreddit_checker)
                    
                    #iterates through evey submission that has the most upvotes
                    #Adds them to a list, and chooses one url randomly to send
                    
                    async for submission in subreddit.hot(limit=50):
                        #Checking if the post is not pinned
                        if not submission.stickied:
                            url = str(submission.url)
                            image_list.append(url)
                            continue
                    image = random.choice(image_list)
                    await message.channel.send(image)
                    await reddit.close()


    #Geeting the token and running the bot!
    load_dotenv('BotToken.env')
    
    TOKEN = os.getenv('BOT_TOKEN')
    
    
    
    client.run(TOKEN)


            


def get_quote(random='random'):
    '''Returns a random quote from an API'''
    try:
        response = requests.get('https://zenquotes.io/api/' + random)
        m = response.json()
        data = json.loads(response.text)
        quote = data[0]['q'] + ' --> ' + data[0]['a']
        return quote
    except requests.RequestException:
        global error_handler 
        return error_handler




def get_joke(flags='Any?blacklistFlags=nsfw,religious,political,racist,sexist,explicit'):
    '''Returns a random joke from an API'''
    try:
        response = requests.get('https://v2.jokeapi.dev/joke/' + flags)
        m = response.json()
        data = json.loads(response.text)
        joke = data['setup'] + ' ' + data['delivery']
        return joke
    except KeyError:
        joke = data['joke']
        return joke
    except requests.RequestException:
        global error_handler
        return error_handler



def get_bitcoin(symbol1='BTCUSDT'):
    '''Returns the price of dogecoin in US dollars'''
    try:
        response = requests.get(f'https://api.binance.com/api/v3/ticker/price?symbol=' + symbol1)
        m = response.json()
        data = json.loads(response.text)
        price = float(data['price'])
        format = f"BitCoin price is {price:,.2f}$"
        return format
    except requests.RequestException:
        global error_handler
        return error_handler




def get_litecoin(symbol2='LTCUSDT'):
    '''Returns the price of litecoin in US dollars'''
    try:
        response = requests.get(f'https://api.binance.com/api/v3/ticker/price?symbol=' + symbol2)
        m = response.json()
        data = json.loads(response.text)
        price = float(data['price'])
        format = f"Litecoin price is {price:,.2f}$"
        return format
    except requests.RequestException:
        global error_handler
        return error_handler



def get_dogecoin(symbol3='DOGEUSDT'):
    '''Returns the price of bitcoin in US dollars'''
    try:
        response = requests.get(f'https://api.binance.com/api/v3/ticker/price?symbol=' + symbol3)
        m = response.json()
        data = json.loads(response.text)
        price = float(data['price'])
        format = f"DogeCoin price is {price:,.2f}$"
        return format
    except requests.RequestException:
        global error_handler
        return error_handler



def get_fun_fact(language='en'):
    '''Returns a random 'fun fact' from an API'''
    try:
        response = requests.get('https://uselessfacts.jsph.pl/random.json?language=' + language)
        m = response.json()
        data = json.loads(response.text)
        fact = data['text']
        return fact
    except requests.RequestException:
        global error_handler
        return error_handler



def get_news(arg):
    '''Returns the most recent 
       news of a specific field, using the GoogleNews.py library.
       Takes an argument that determines that field.'''
    try:
        arg = arg.upper()
        googlenews = GoogleNews()
        googlenews = GoogleNews(lang='en')
        googlenews.search(arg)
        googlenews.get_page(2)
        res = googlenews.results()
        return res[0]['title'] + '\n' + res[0]['link'] + '\n' + res[0]['date']
    except requests.RequestException:
        global error_handler
        return error_handler
    except AttributeError:
        return 'Make sure to type a "/" before the term you want to be searched!!'
    except IndexError:
        return 'Make sure to type a "/" before the term you want to be searched!!'




def find_keywords(a):
    '''Returns None if there are no matches'''
    return re.compile(r'\b({0})\b'.format(a), flags=re.IGNORECASE).search





def Stemmer(input):
    '''Returns a string
       which words are reduced to their root '''
    ps = PorterStemmer()
    w = []
    string = ' '
    #Separeating the sentence into individual words
    #So they can be stemmed
    tokenized = word_tokenize(input)
    for word in tokenized:
        stemmed = ps.stem(word)
        w.append(stemmed)
        user = string.join(w)
    return user



if __name__ == '__main__':
    main()