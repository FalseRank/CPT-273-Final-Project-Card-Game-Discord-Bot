#Import Required Libraries
import discord
from core.deck import Deck
from core.cards import format_card
from games.war_game import WarGame

#Creates the class "WarView" which handles the ui for War game
class WarView(discord.ui.View):
    def __init__(self, host, cog):
        #Sets timeout for 60 seconds
        super().__init__(timeout=60)

        #Sets author variable
        self.host = host
        #Creates variable for second plahyer
        self.player2 = None
        #Sets cog for war
        self.cog = cog
        #Creates game instance
        self.game = None

        #Creates player tracking
        self.p1_played = False
        self.p2_played = False

    #===================================================================================
    #Join Button                           
    #===================================================================================
    @discord.ui.button(label="Join", style=discord.ButtonStyle.green)
    async def join(self, interaction: discord.Interaction, button: discord.ui.Button):

        #Prevents more than 2 people from playing
        if self.player2:
            return await interaction.response.send_message("Game full.", ephemeral=True)

        #Host cannot join as a second player
        if interaction.user == self.host:
            return await interaction.response.send_message("You are host.", ephemeral=True)

        #Assigns second plyaer
        self.player2 = interaction.user

        #Updates the message to show the players
        await interaction.response.edit_message(
            content=f"{self.host.mention} vs {self.player2.mention}\nPress Start!",
            view=self
        )

    #===================================================================================
    #Start Button                           
    #===================================================================================
    @discord.ui.button(label="Start", style=discord.ButtonStyle.blurple)
    async def start(self, interaction: discord.Interaction, button: discord.ui.Button):

        #Only the host can start the game
        if interaction.user != self.host:
            return await interaction.response.send_message("Only host can start.", ephemeral=True)

        #Requires a second player to start
        if not self.player2:
            return await interaction.response.send_message("Need 2 players.", ephemeral=True)

        #Initialize game logic
        self.game = WarGame(Deck(), self.host, self.player2)

        #Prints that the game has started and prompts players to draw card
        await interaction.response.edit_message(
            content=f"War Started!\n{self.host.mention} vs {self.player2.mention}\nPress Draw!",
            view=self
        )

    #===================================================================================
    #Draw Button                           
    #===================================================================================
    @discord.ui.button(label="Draw", style=discord.ButtonStyle.red)
    async def draw(self, interaction, button):

        #Ensures that game has started
        if not self.game:
            return await interaction.response.send_message("Game not started.", ephemeral=True)

        #Tracks player input 
        if interaction.user == self.host:
            if self.p1_played:
                return await interaction.response.send_message("Already played.", ephemeral=True)
            self.p1_played = True

        elif interaction.user == self.player2:
            if self.p2_played:
                return await interaction.response.send_message("Already played.", ephemeral=True)
            self.p2_played = True

        else:
            #Prevents outsiders from interacting
            return await interaction.response.send_message("Not your game.", ephemeral=True)

        #If both players havent played yet this update message instead of sending new one
        if not (self.p1_played and self.p2_played):

            #Makes status
            status = []
            status.append("✅" if self.p1_played else "⏳")
            status.append("✅" if self.p2_played else "⏳")

            await interaction.response.edit_message(
                content=(
                    f"{self.host.mention} vs {self.player2.mention}\n\n"
                    f"Waiting for players...\n"
                    f"{self.host.display_name}: {status[0]}\n"
                    f"{self.player2.display_name}: {status[1]}"
                ),
                view=self
            )
            return

        #Plays the round if both players are ready
        c1, c2, text = self.game.play_round()

        #Resets both players to not played - prepares for next round
        self.p1_played = False
        self.p2_played = False

        #Builds round result message
        content = (
            f"{self.host.mention} drew: {format_card(c1)}\n"
            f"{self.player2.mention} drew: {format_card(c2)}\n\n"
            f"{text}\n\n"
            f"Cards left:\n"
            f"{self.host.display_name}: {len(self.game.p1)}\n"
            f"{self.player2.display_name}: {len(self.game.p2)}"
        )

        #If game is over show winner
        if self.game.game_over:
            self.stop()
            return await interaction.response.edit_message(
                content=f"{content}\n {self.game.winner.mention} wins!",
                view=None
            )

        #Continues game if the game is still going
        await interaction.response.edit_message(content=content, view=self)

    #===================================================================================
    #End Game Button                           
    #===================================================================================
    @discord.ui.button(label="End Game", style=discord.ButtonStyle.grey)
    async def end_game(self, interaction, button):

        #Only the players can end the game
        if interaction.user not in [self.host, self.player2]:
            return await interaction.response.send_message("Not your game.", ephemeral=True)

        #Forces the game to end
        self.game.game_over = True
        self.game.winner = "Game manually ended"

        #Disables all the buttons
        for item in self.children:
            item.disabled = True

        #Stop the view
        self.stop()

        #Updates the message
        await interaction.response.edit_message(
            content="Game ended by player.",
            view=None
        )


