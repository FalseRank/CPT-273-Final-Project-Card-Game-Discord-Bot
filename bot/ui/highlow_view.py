#Import Required Libraries
import discord
from core.cards import format_card

#Creates the class "HighLowView" which handles ui for highlow game
class HighLowView(discord.ui.View):
    def __init__(self, game, author, cog, economy):
        #Sets timeout for 60 seconds
        super().__init__(timeout=60)

        #Sets game instance
        self.game = game
        #Creates author variable
        self.author = author
        #Sets cog for highlow
        self.cog = cog
        #Sets economy
        self.economy = economy

    async def interaction_check(self, interaction: discord.Interaction):
        return interaction.user == self.author



    #===================================================================================
    #Buttons                           
    #===================================================================================
    #Button to guess higher
    @discord.ui.button(label="Higher", style=discord.ButtonStyle.green)
    async def higher(self, interaction, button):
        await self.play(interaction, "higher")

    #Button to guess Lower
    @discord.ui.button(label="Lower", style=discord.ButtonStyle.red)
    async def lower(self, interaction, button):
        await self.play(interaction, "lower")

    #Button to Quit
    @discord.ui.button(label="Quit", style=discord.ButtonStyle.grey)
    async def quit(self, interaction, button):

        #Mark the game as over and remove it from active games
        self.game.game_over = True
        self.cog.games.pop(self.author.id, None)

        #Disables the buttons
        for item in self.children:
            item.disabled = True

        #Stops interactions from happening
        self.stop()

        #Sends message that game has ended
        await interaction.response.edit_message(
            content="Game quit.",
            view=None
        )

    #===================================================================================
    #Game Logic                             
    #===================================================================================
    async def play(self, interaction, choice):

        #Processes the players guess
        result, card, _ = self.game.guess(choice)

        #Formats the cards drawn
        card_text = format_card(card) if card else "No card"
        #Shows streak
        streak_text = f"Streak: {self.game.score}"

        #===================================================================================
        #Game Over                             
        #===================================================================================
        if self.game.game_over:

            #Remove game from active sessions
            self.cog.games.pop(self.author.id, None)

            #Saves score to leaderboard
            self.economy.update_highlow(
                interaction.user,
                self.game.score
            )

            #Disables all the buttons 
            for item in self.children:
                item.disabled = True

            #Stops interactions
            self.stop()

            #Shows final results
            await interaction.response.edit_message(
                content=(
                    f"{result}\n"
                    f"You drew: {card_text}\n"
                    f"{streak_text}\n"
                    f"Game Over!"
                ),
                view=None
            )
            return

        #===================================================================================
        #Continue Game                             
        #===================================================================================
        await interaction.response.edit_message(
            content=(
                f"{result}\n"
                f"You drew: {card_text}\n"
                f"{streak_text}"
            ),
            view=self
        )