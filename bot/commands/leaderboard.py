#Import Required Libraries
from discord.ext import commands

#Sets up class leaderboard which handles chip and higher or lower leaderboards
class Leaderboard(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    #===================================================================================
    #Chip Command                                !leaderboard
    #===================================================================================
    @commands.command()
    async def leaderboard(self, ctx):

        #Access shared economy system
        eco = self.bot.economy

        #Sorts out the top 5 balances from highest to lowest 
        sorted_balances = sorted(
            eco.balances.items(),
            key=lambda x: x[1],
            reverse=True
        #Can change to value for leaderboards
        )[:5]

        #Prints out title for leaderboard
        lines = ["**Chip Leaderboard**"]

        #Loops through each person in top 5
        for i, (user_id, bal) in enumerate(sorted_balances, 1):
            #Gets discord user for top 5
            user = await self.bot.fetch_user(user_id)
            #Adds line to print 
            lines.append(f"{i}. {user.name} — {bal} chips")

        #Prints out the message
        await ctx.send("\n".join(lines))



    #===================================================================================
    #Higher Or Lower Leaderboard Command                                !highlowlb
    #===================================================================================
    @commands.command()
    async def highlowlb(self, ctx):

        #Access shared economy system
        eco = self.bot.economy

        #Sorts out the top 5 balances from highest to lowest
        sorted_scores = sorted(
            eco.high_low_scores.items(),
            key=lambda x: x[1],
            reverse=True
        #Can change value for the leaderboard
        )[:5]

        #Prints out the title for leaderboard
        lines = ["**High or Low Leaderboard**"]

        #Loops through each person in top 5
        for i, (user_id, score) in enumerate(sorted_scores, 1):
            #Gets discord user for top 5
            user = await self.bot.fetch_user(user_id)
            #Adds line to print
            lines.append(f"{i}. {user.name} — {score}")

        #Prints out the message
        await ctx.send("\n".join(lines))

#Needed for running commands
async def setup(bot):
    await bot.add_cog(Leaderboard(bot))