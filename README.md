  # Persy: Discord Bot
        



#### Video Demo:  <URL HERE>
        




*Persy was made using the discord.py library.*





#### When I first though of making a discord bot for CS50p final project, I wanted it to interact with the users and also entertain them or give them information that they may need! I noticed that most bots on discord used hard-coded commands such as '!help' that have a prefix before them. However, this may be easier to control as it is something specific that will probably not be typed by any user that doesn't want to use the bot. Knowing that, I wanted to make the input more flexible so the user would not have to remember the command or the prefix, which may look cryptic to some individuals, that's why I set up a basic .json file;

    
 
 
 
 
### The words.json file
        
        
#### In words.json there is a 'keywords' list in each instance, that includes words or phrases that are likely to be typed by the user, all of these words are ***reduced to their root***. Also, there is the 'Output' that includes various hardcoded responses that the bot will randomly chose from in each case. Finally the 'subject' describes the category that the keywords and responses correspond to. Despite the fact that it is not used in the file project.py, it is still useful to add in order to get some basic context.

        




## BotToken.env file
        
#### This must include the token of a bot, which is something like its password. The token is needed in order to run the code that's why it should not be made public or be shared. This is where a discord bot token can be obtained: https://discord.com/developers.

 
 



## Main Idea

#### The main idea goes as follows; 
        
#### 1) The program will read the data from the .json file, add them into individual lists depending on their category

#### 2) The user will type a sentence in the chat, the program will check if the user's input contains the word 'persy' (ignoring the case) and will do the following;

####    i) The program will split this sentence into individual words and will use the nltk.stem package from the nltk library to get the root of each word.

####    ii) Then the program will check if there is the same stemmed word/phrase in the user's input with each list that has the keywords from the .json file and will chose randomly from the corresponding output and     assign the answer in a variable.
   
####    iii) The process is repeated when the program detects 'persy' in the user's input
            





## The discord.py library

#### Discord.py is an asynchronous library and mainly uses 'events', for instance when a user sends a message the program responds to that event and excecutes the code of the event function. In this code we have two async functions; on_ready and on_message
    
#### According to the [discord.py documentation](*https://discordpy.readthedocs.io/en/stable/*), the **on_ready** function is called when the bot has finished logging in discord. Also this function displays an activity status, a sentence that allows the user to ask for help from the bot. In addition, the **on_message** function is called when a user sends a message in a server where the bot is or in private chat with a user. 



## The usage of NLTK (Natural Language Tool Kit) library and searching for keywords



### Word Tokenize



#### First of all, this library is used to separate the user's input into 'tokens' using the word_tokenize. This way, the user's sentence will become a list of individual words, ignoring spaces and separating punctuation from the word. For instance, the string 'Hello, there' will become a list of ['Hello', ',', 'there'] e.t.c. This process is essential for the next step, stemming the words.



### Stemmer 


#### First of all, I have to mention why I decided to use this method; As mentioned, the .json file contains stemmed keywords, thus if the user decides to type the keyword with the same root and meaning but with different ending for example, the algorithm will be able to recognise this word from the keywords list. For instance, if the user types 'cry' or 'cried' the *Stemmer()* function will return 'cri' which is a keyword found in the .json file, thus it is not needed to write every form of the word. Another thing that I had originally though but ended up avoiding is to use the statement 'if keyword in user_input' without implementing the *Stemmer()* function. For example, if the keyword was 'cry' this statement would be *True* for every word wich containing **cry** in it such as **cry**stal and [much more](https://www.thefreedictionary.com/words-containing-cry). So, I decided to implement a function that checks if there is an individual word from the stemmed user's input which is the same with a keyword using [regular expressions](https://regexguide.readthedocs.io/en/latest/regex/regex.html). 





## Chosing the response

#### The program checks if the *find_keywords* does not return *None*, and choses a random hard-coded response from the corresponding list, so the bot seems more humanlike and interactive. However, some *ouputs* from the .json file are empty. This is because of the fact that the bot has some other features instead of chatting.




## Additional features and fetching posts from [Reddit](https://www.reddit.com/)


### Help!


#### As I mentioned before, when the bot logs in it displays an activity status under the profile, for example in this case 'Playing **Persy I need help!**', in order to guide the user to ask for it. When the program detects a keyword related to *help* sets the output variable as a string writen in the .json file and later checks if the output is equal to that string. If it is the bot displays a well-organised, and pleasant to read message using discord's Embed method.



### Getting recent news with the [GoogleNews](https://pypi.org/project/GoogleNews/) library


#### Persy can also get recent news using the [GoogleNews](https://pypi.org/project/GoogleNews/) library! The program checks for the right keywords and a '/' before a word the the user wants to get news about (So the bot can recognise what to search for), removes it, and then calls the *get_news* function which uses the word to get recent news from the library! If the user does not include a '/' **before** a word then they are prompted to do so!


### Getting [quotes](https://zenquotes.io/), [jokes](https://v2.jokeapi.dev/), [fun facts](https://uselessfacts.jsph.pl/) and the price of [cryptocurrency](https://www.binance.com/en-IN/binance-api) from APIs!

#### 


    
