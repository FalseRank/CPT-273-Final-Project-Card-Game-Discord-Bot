The Card Game bot is a school project discord bot. The objective of this bot is to help people get to know one another within the discord classroom by providing some easy accessible card games such as blackjack, higher or lower, and war. The Card Game bot is written in Python code using discord.py libraries and was designed to run on Docker for easy deployment.

--------------------------------------------------------------------------------------------------------------------
System Requirements
The server hosting the bot shopuld have:
-Python 3.10+
-Docker
-Git (to install proper dependencies run: sudo apt update sudo apt install python3 python3-pip git docker.io)

--------------------------------------------------------------------------------------------------------------------
Starting Docker
1. Run:  sudo systemctl start docker
2. To download the project from the github you need to clone it. git clone https://github.com/FalseRank/Card-Game-Bot.git
3. Builder the Docker Container: Build Docker image in bash: docker build -t card-game-discord-bot
4. To start the bot run the following in bash: docker run --env-file .env card-game-discord-bot
5. Running the bot 24/7 In bash run: docker run -d -env-file .env card-game-discord-bot

--------------------------------------------------------------------------------------------------------------------
If everything is all successful you should run, docker ps, in bash and it will display values under the labels. To stop the bot run, docker stop CONTAINER_ID. 

To update the bot do: git pull docker build -t card-game-discord-bot . docker run -d -env-file .env card-game-discord-bot

--------------------------------------------------------------------------------------------------------------------
Bot Commands:
!help         -   This will print the list of commands and what they do
!chips        -   This will print the amount of chips you own
!reset        -   This will reset the amount of chips that you have in case you run out

!blackjack    -   Starts the game of blackjack (can be multiplayer)
!highlow      -   Starts the game of higher or lower where you guess whether the next card will be higher or lower  than current card
!war          -   Starts the game of war (can only be played with another person)

!leaderboard  -   This shows who the top 5 highest chip owners in the server
!highlowlb    -   This shows the top 5 longest higher or lower runs