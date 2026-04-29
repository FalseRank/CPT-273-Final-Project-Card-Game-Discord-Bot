#Import Required Libraries
import discord
from core.deck import Deck
from core.cards import format_card
from games.blackjack_game import BlackjackGame

#Sets up class of "BlackjackView" which handles the ui for the blackjack game
class BlackjackView(discord.ui.View):
    def __init__(self, host, economy):
        #Sets timeout for 60 seconds
        super().__init__(timeout=60)

        #Sets host variable
        self.host = host
        #Gets list of players
        self.players = [host]

        #Holds game instance once started
        self.game = None
        #Gets economy system
        self.economy = economy

        #Stores the bets
        self.pending_bets = {}



    #===================================================================================
    #Join Button                             
    #===================================================================================
    @discord.ui.button(label="Join", style=discord.ButtonStyle.green)
    async def join(self, interaction: discord.Interaction, button: discord.ui.Button):

        #Prevents people joining when game is started
        if self.game is not None:
            return await interaction.response.send_message("Game already started.", ephemeral=True)

        #If someone is already in the game prevents them from joing in again
        if interaction.user in self.players:
            return await interaction.response.send_message("Already joined.", ephemeral=True)

        #Allows only 4 or less people
        if len(self.players) >= 4:
            return await interaction.response.send_message("Game full (max 4 players).", ephemeral=True)

        #Adds players to the game
        self.players.append(interaction.user)

        #Shows current player list
        await interaction.response.edit_message(
            content="Players:\n" + "\n".join(p.mention for p in self.players),
            view=self
        )



    #===================================================================================
    #Start Game Button                                
    #===================================================================================
    @discord.ui.button(label="Start", style=discord.ButtonStyle.blurple)
    async def start(self, interaction: discord.Interaction, button: discord.ui.Button):

        #Makes it so only the host can start the game
        if interaction.user != self.host:
            return await interaction.response.send_message("Only host can start.", ephemeral=True)

        #Prevents starting game multiple times
        if self.game is not None:
            return await interaction.response.send_message("Game already started.", ephemeral=True)

        #Creates the game instance
        self.game = BlackjackGame(self.players, Deck(), self.economy)

        #Takes in the bets
        self.game.bets = self.pending_bets

        #Shows game state
        await interaction.response.edit_message(
            content=self.render_state(),
            view=self
        )



    #===================================================================================
    #Hit Button                                
    #===================================================================================
    @discord.ui.button(label="Hit", style=discord.ButtonStyle.green)
    async def hit(self, interaction: discord.Interaction, button: discord.ui.Button):

        #Makes sure the game is started
        if self.game is None:
            return await interaction.response.send_message("Game hasn't started yet.", ephemeral=True)

        #Ensures that it is the players turn
        if interaction.user.id != self.game.current_player().id:
            return await interaction.response.send_message("Not your turn.", ephemeral=True)

        #Defer response to avoid interaction from timing out
        await interaction.response.defer()

        #Performs the action and moves turn to next
        msg = self.game.hit(interaction.user)
        self.game.next_turn()

        #Updates the UI
        await self.update_game(interaction, msg)



    #===================================================================================
    #Stand Button                               
    #===================================================================================
    @discord.ui.button(label="Stand", style=discord.ButtonStyle.red)
    async def stand(self, interaction: discord.Interaction, button: discord.ui.Button):

        #Ensures that the game is started
        if self.game is None:
            return await interaction.response.send_message("Game hasn't started yet.", ephemeral=True)

        #Ensures that it is the players turn
        if interaction.user.id != self.game.current_player().id:
            return await interaction.response.send_message("Not your turn.", ephemeral=True)

        #Defers the response to avoid the interaction from timing out
        await interaction.response.defer()

        #Performs the action and moves turn to next 
        msg = self.game.stand(interaction.user)
        self.game.next_turn()

        #Updates the UI
        await self.update_game(interaction, msg)



    #===================================================================================
    #Play Again Button                               
    #===================================================================================
    @discord.ui.button(label="Play Again", style=discord.ButtonStyle.success)
    async def play_again(self, interaction: discord.Interaction, button: discord.ui.Button):

        #Ensures that the game existed
        if self.game is None:
            return await interaction.response.send_message("No finished game.", ephemeral=True)

        #Ensures the game is over
        if not self.game.all_done():
            return await interaction.response.send_message("Game still running.", ephemeral=True)

        #Creates another game instance
        self.game = BlackjackGame(self.players, Deck(), self.economy)

        #Reuse previous bets
        self.game.bets = self.pending_bets

        #Enables gameplay buttons (Hit stand)
        for item in self.children:
            if item.label in ["Hit", "Stand"]:
                item.disabled = False

        #Shows the new game state
        await interaction.response.edit_message(
            content="New game started!\n\n" + self.render_state(),
            view=self
        )

    #===================================================================================
    #Exit Button                               
    #===================================================================================
    @discord.ui.button(label="Exit", style=discord.ButtonStyle.danger)
    async def exit(self, interaction: discord.Interaction, button: discord.ui.Button):

        #Disables all the buttons
        for item in self.children:
            item.disabled = True

        #Stops interactions
        self.stop()

        #Shows the game is closed
        await interaction.response.edit_message(
            content="Game closed.",
            view=self
        )

    #===================================================================================
    #Update Game                                
    #===================================================================================
    async def update_game(self, interaction: discord.Interaction, msg: str):

        #Game end if all players are done
        if self.game.all_done():
            self.game.dealer_play()
            dealer_val, results = self.game.results()

            #Builds final message
            content = (
                f"Dealer: {self.render_hand(self.game.dealer)} ({dealer_val})\n\n"
                + "\n".join(results)
            )

            #Disables gameplay buttons
            for item in self.children:
                if item.label in ["Hit", "Stand"]:
                    item.disabled = True

            #Updates message with final results
            await interaction.edit_original_response(
                content=content,
                view=self
            )
            return

        #Game continues normally if game hasnt ended
        await interaction.edit_original_response(
            content=f"{msg}\n\n{self.render_state()}",
            view=self
        )

    #===================================================================================
    #Renderinbg                              
    #===================================================================================
    def render_state(self):
        lines = []

        #Builds display for all players
        for p in self.players:
            pid = p.id

            #Formats the hand for each player and calculates value
            hand = self.render_hand(self.game.hands[pid])
            val = self.game.hand_value(self.game.hands[pid])

            #Shows if player busted
            status = "💥" if self.game.busted[pid] else ""
            #Shows what players turn it is
            turn = "⬅️" if p.id == self.game.current_player().id else ""

            lines.append(f"{p.display_name}: {hand} ({val}) {status} {turn}")

        #Shows only first card of dealer and hides the other
        dealer = format_card(self.game.dealer[0]) + " + ?"

        return f"Dealer: {dealer}\n\n" + "\n".join(lines)

    #===================================================================================
    #Hand Formatter                                
    #===================================================================================
    def render_hand(self, hand):
        #Converts list of cards into a readible string
        return ", ".join(format_card(c) for c in hand)