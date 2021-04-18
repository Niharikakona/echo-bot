# echo-bot

# This is  a Telegram Bot that echoes the messages that we send to it

 STEP 1-**Set up your Bot’s profile
         To set up a new bot, start the conversation with BotFather (@BotFather).
         BotFather will help us in creating the new bot.
         Search for @botfather in Telegram.
         Start your conversation by pressing the Start button.
         Create the bot by running /newbot command.
         Enter the Display Name and User Name for the bot.
         BotFather will send you a message with the token.
         
STEP 2- **Coding the bot
        Open up the terminal and start by creating a new directory first.
        
        "mkdir echo-bot/"
        "cd echo-bot/"
        
        **We will be using pipenv virtual environment. Make sure that you have pipenv installed in your system.
        **We will be using python-telegram-bot package for interacting with Telegram API. Install the package using the following command.
        
        pipenv install python-telegram-bot
        
        Create a new file bot.py ,and clone my repository for code.
        
        
        
 STEP 3- Deploying Telegram Bot for FREE on Heroku
         **Setting up Heroku
           you will need to create an account on Heroku.
           Install heroku-cli for your specific operating system.
          Login in to your account by running the following command in terminal
          "heroku login"
          For deploying the bot online, we will be using webhooks.
          Replace TOKEN with the value you got from BotFather . Replace APP_NAME with the application name you will be creating in the next step. 
          
          we had made a directory named echo-bot. Run the following command to change to your bot’s directory.
          "cd echo-bot/"
          **Now, we will first need to make this directory as a git repository before pushing the code to Heroku. Use the following command to instantiate your current                 directory as a git repository.
          "git init"
   Create the Heroku application using the following command, you can use whatever “app_name” you like.
    heroku create "app_name"
          
          
   **Now you can use this Heroku application link in the APP_NAME in the code above.
   Once the app is created, you can check the Remote URL of the application. Run the following command to check the emote information.
   "git remote -v"
   Now we need to tell our application what command to run on startup, for that Heroku uses a file called Procfile.
   Create a file named “Procfile” using the following command.
   "vim Procfile"
   Add the following contents to Procfile. Make sure that your file name is bot.py
   "web: python3 bot.py"
   Now, you need to tell the dependencies to install on the Heroku server. Enter the pipenv shell first.
   "pipenv shell"
   "pip freeze > requirements.txt"
   Now we’re almost done with the Heroku part, you just need to add the files, commit it and push those changes to Heroku. For our changes, we can add all the files in the       git repo. So run the following command.
    "git add ."
    You can check the status using the following command.
    "git statuS"
    Once added to git, we need to commit it and push it. Run these commands.
    "git commit -m <add_your_message>"
    "git push heroku master"
    Now your application will start its build, you can check the logs by running the following command.
    "heroku logs -t"
