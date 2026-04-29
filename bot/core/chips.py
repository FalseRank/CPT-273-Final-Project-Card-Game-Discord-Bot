#Creates class called economy which handles the chips
class Economy:
    def __init__(self):
        #Stores the users chips
        self.balances = {}
        #Stores the highest streaks
        self.high_low_scores = {}



    #Gets the balance of a user
    def get(self, user):
        return self.balances.get(user.id, 1000)



    #Add chips to the users balance if they win
    def add(self, user, amount):
        self.balances[user.id] = self.get(user) + amount



    #Removes chips from the users balance if they loose
    def remove(self, user, amount):
        self.balances[user.id] = self.get(user) - amount



    #Saves highest rounds someone gets in higher or lower
    def update_highlow(self, user, score):

        #Gets the current best score
        current = self.high_low_scores.get(user.id, 0)

        #Makes it so only highest scores save
        if score > current:
            self.high_low_scores[user.id] = score