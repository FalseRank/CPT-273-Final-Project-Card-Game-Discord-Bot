#Import Required Libraries
from discord.ext import commands
from ui.blackjack_view import BlackjackView

#Sets up class of "blackjack" which handles commands for blacjack
class Blackjack(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        #Stores bets before game so you can bet
        if not hasattr(bot, "pending_bets"):
            bot.pending_bets = {}



    #===================================================================================
    #Blackjack Command                                !blackjack
    #===================================================================================
    @commands.command()
    async def blackjack(self, ctx):

        #Creates the game UI by calling ui.blackjack_view
        view = BlackjackView(ctx.author, self.bot.economy)

        #Passes stored bets into the view so the game can use them
        view.pending_bets = self.bot.pending_bets

        #Sends message with buttons to start game
        await ctx.send(
            f"{ctx.author.mention} started Blackjack!\nClick Join (max 4 players).",
            view=view)

#Required for running command
async def setup(bot):
    await bot.add_cog(Blackjack(bot))