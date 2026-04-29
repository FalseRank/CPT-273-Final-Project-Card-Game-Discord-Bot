#Imports required libraries
from discord.ext import commands
from ui.war_view import WarView

#Sets up class "War" which handles war command
class War(commands.Cog):
    def __init__(self, bot):
        self.bot = bot



    #===================================================================================
    #War Command                                !war
    #===================================================================================
    @commands.command() 
    async def war(self, ctx):

        #Creates the game UI 
        view = WarView(ctx.author, self)

        #Send starting message 
        await ctx.send(
            f"{ctx.author.mention} started a War game!\nClick Join to play.",
            view=view
        )

#Needed for running commands
async def setup(bot):
    await bot.add_cog(War(bot))