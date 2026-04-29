#Required Libraries
from discord.ext import commands
from core.deck import Deck
from games.highlow_game import HighLowGame
from ui.highlow_view import HighLowView
from core.cards import format_card

#Sets up class of "HigherLow" which handles commands for higher or lower game
class HighLow(commands.Cog):
    def __init__(self, bot, economy):
        self.bot = bot

        #Sets economy for leaderboard stats
        self.economy = economy

        #Prevents multiple games occuring at once
        self.games = {}



    #===================================================================================
    #Higher Or Lower Command                                !highlow
    #===================================================================================
    @commands.command()
    async def highlow(self, ctx):

        #Prevents user from having multiple games at once
        if ctx.author.id in self.games:
            await ctx.send("You already have a game running.")
            return

        #Creates a shuffled deck
        deck = Deck()

        #Starts the game logic
        game = HighLowGame(deck)

        #Creates interactive UI by calling the HighLowView
        view = HighLowView(game, ctx.author, self, self.economy)

        #Stores the active game for the user
        self.games[ctx.author.id] = game

        #Sends a message for starting game
        await ctx.send(
            f"Starting card: {format_card(game.current_card)}\n"
            f"Higher or Lower?",
            view=view
        )

#Required for running commands
async def setup(bot):
    await bot.add_cog(HighLow(bot, bot.economy))