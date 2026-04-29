#Import Required Libraries
import discord
from discord.ext import commands

#Sets up the class of players "Balance" which handles commands for chips betting and resets
class Balance(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    #===================================================================================
    #Check Chips                                 !Chips
    #===================================================================================
    @commands.command()
    async def chips(self, ctx, member: discord.Member = None):

        #Sets member as author of message
        member = ctx.author
        
        #Gets the chips for member from economy
        balance = self.bot.economy.get(member)

        #Sends message 
        await ctx.send(f"{member.display_name} has **{balance} chips**.")



    #===================================================================================
    #Bet Command                                !Bet
    #===================================================================================
    @commands.command()
    async def bet(self, ctx, amount: int):

        #Sets user as author of message 
        user = ctx.author

        #Sets balance as chips from user
        balance = self.bot.economy.get(user)

        #If the amount "bet" is 0 or negative declines the bet
        if amount <= 0:
            return await ctx.send("Bet must be greater than 0.")

        #If the amount "bet" is greater than the users balance declines the bet
        if amount > balance:
            return await ctx.send("Not enough chips.")

        #Removes the chips when betting
        self.bot.economy.remove(user, amount)

        #Creates the bet for playing blackjack (instances when game hasnt started)
        if not hasattr(self.bot, "pending_bets"):
            self.bot.pending_bets = {}
        #Stores the bet for the next game of blackjack
        self.bot.pending_bets[user.id] = amount

        #Sends message that you placed a bet with amout
        await ctx.send(f"Bet placed: {amount} chips")


    #===================================================================================
    #Reset Chips                                     !Reset
    #===================================================================================
    @commands.command()
    async def reset(self, ctx):

        #Sets user as author of command
        user = ctx.author

        #Resets the authors balance
        self.bot.economy.balances[user.id] = 1000

        #Sends message that you account has been reset
        await ctx.send(f"{user.display_name}, your chips have been reset to 1000.")

#Required for loading the command
async def setup(bot):
    await bot.add_cog(Balance(bot))