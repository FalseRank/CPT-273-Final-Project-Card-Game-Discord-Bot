#Import Required Library
from discord.ext import commands

#Sets up "help" class which handles help command
class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot



    #===================================================================================
    #Help Command                                !help
    #===================================================================================
    @commands.command()
    async def help(self, ctx):

        #Sets output message
        message = """
        **Card Bot Help**

        Commands:
        - `!chips` → Check your balance
        - `!bet` → Place a bet (used in games)
        - `!reset` → Reset your chips

        Games:
        - `!blackjack` → Start a blackjack game
        - `!poker` → Start poker
        - `!highlow` → Play high/low game

        Stats:
        - `!leaderboard` → Top chip holders
        - `!highlowlb` → High/Low high scores
        """

        #Sends the output message
        await ctx.send(message)

#Required for running commands
async def setup(bot):
    await bot.add_cog(Help(bot))