   # Persy: Discord Bot
        
   #### Video Demo:  <URL HERE>
        
   *Persy was made using the discord.py library.*


#### When I first though of making a discord bot for CS50p final project, I wanted it to interact with the users and also entertain them or give them information that they may need! I noticed that most bots on discord used hard-coded commands such as '!help' that have a prefix before them. However, this may be easier to control as it is something specific that will probably not be typed by any user that doesn't want to use the bot. Knowing that, I wanted to make the input more flexible so the user would not have to remember the command or the prefix, which may look cryptic to some individuals, that's why I set up a basic .json file;

    
 ## The words.json file
        
        
#### In words.json there is a 'keywords' list in each instance, that includes words or phrases that are likely to be typed by the user, all of these words are ***reduced to their root***. Also, there is the 'Output' that includes various hardcoded responses that the bot will randomly chose from in each case. Finally the 'subject' describes the category that the keywords and responses correspond to. Despite the fact that it is not used in the file project.py, it is still useful to add in order to get some basic context.

        
## BotToken.env file
        
#### This must include the token of a bot, which is something like its password. The token is needed in order to run the code that's why it should not be made public or be shared. This is where a discord bot token can be obtained: https://discord.com/developers.

 ## Main Idea

#### The main idea goes as follows; 
        
#### 1) The program will read the data from the .json file, add them into individual lists depending on their category

#### 2) The user will type a sentence in the chat, the program will check if the user's input contains the word 'persy' (ignoring the case) and will do the following;

####    i) The program will split this sentence into individual words and will use the nltk.stem package from the nltk library to get the root of each word.

####    ii) Then the program will check if there is the same stemmed word/phrase in the user's input with each list that has the keywords from the .json file and will chose randomly from the corresponding output and     assign the answer in a variable.
   
###    iii) The process is repeated when the program detects 'persy' in the user's input
            
## The discord.py library

#### Discord.py is an asynchronous library and mainly uses 'events', for instance when a user sends a message the program responds to that event and excecutes the code of the event function. In this code we have two async functions; on_ready and on_message
    
#### According to the discord.py documentation (*https://discordpy.readthedocs.io/en/stable/*), the **on_ready** function is called when the bot has finished logging in discord. Also this function displays an activity status, a sentence that allows the user to ask for help from the bot. In addition, the **on_message** function is called when a user sends a message in a server where the bot is or in private chat with a user. 

## The usage of NLTK (Natural Language Tool Kit) library

  
    
