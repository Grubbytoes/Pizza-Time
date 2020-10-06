#PUSSY
class Topping:
    def __init__(self, name, isVeg = True):
        self.name = name
        self.isVeg = isVeg

    def __repr__(self):
        return self.name
    
class Pizza:
    #The size dictionary:
    sizes = {
        0: "small",
        1: "medium",
        2: "large",
        3: "super-size"
        }
    
    def __init__(self, customer = "(No customer)", size = 1):
        #The customer name, as a string
        self.customer = customer
        #The size of the pizza, used to calculate price
        self.size = size
        #The toppings to go on the pizza
        self.toppings = []
        #This set will contain all toppings that are "extra"
        self.extras = set()
        #The price of the pizza, £8 standard size
        self.price = 6 + (self.size * 2)
        #This will always be true at the start as there are no toppings
        self.isVeg = True
    
    def add(self, newTopping, addExtra = False):
        #Does the pizza already have this topping?
        if newTopping in self.toppings:
            #If its is already extra-ed, we can't add any more
            if newTopping in self.extras:
                return "pizza already has extra {}, cannot add any more".format(newTopping)
            #Otherwise we add it to the exrta set
            #and add to the cost
            self.price += 0.50
            self.extras.add(newTopping)
            
            return "added extra {}".format(newTopping)
        #The part where we acctualy add the topping
        #and add to the cost
        self.toppings.append(newTopping)
        self.price += 1
        #Adding meat to a veggie pizza
        if self.isVeg > newTopping.isVeg:
            self.isVeg = False
        #If we want extra, we just run the command a second time
        if addExtra:
            return self.add(newTopping)
        
        return "added {}".format(newTopping)
    
    def add_toppings(self, newToppings):
        #We will do this using  a cheeky bit of recursion...
        returnStr = ""
        returnStr += self.add(newToppings[0])
        if len(newToppings) > 1:
            returnStr += "\n"
            returnStr += self.add_toppings(newToppings[1:])

        return returnStr
        
    def remove(self, toppingToRemove, removeAll = True):
        #Check we acctualy have that topping
        if not toppingToRemove in self.toppings:
            return "Pizza does not have that topping"
        #if the topping extra?
        if toppingToRemove in self.extras:
            #take it out and update the price
            self.extras.remove(toppingToRemove)
            self.price -= 0.50
            #if removeAll we can just by pass this bit
            if not removeAll:
                return "Removed extra {}".format(toppingToRemove)
        #Otherwise...
        self.toppings.remove(toppingToRemove)
        self.price -= 1
        #Veggie check
        if not toppingToRemove.isVeg:
            isNowVeg = True
            for topping in self.toppings:
                if not topping.isVeg:
                    isNowVeg = False
                    break
            self.isVeg = isNowVeg
                    
        return "removed {}".format(toppingToRemove)
        
    def remove_toppings(self,toppingsToRemove):
        #the exact same principle of recursion as add_toppings()
        returnStr = ""
        returnStr += self.remove(toppingsToRemove[0])
        #No need to keep recuring if self.toppings is empty
        if len(toppingsToRemove) > 1 and self.toppings:
            returnStr += '\n'
            returnStr += self.remove_toppings(toppingsToRemove[1:])

        return returnStr

    def remove_all(self):
        #The method will clear the pizza of all toppings
        #We have to use a copy, else it will skip toppings as it removes them
        allToppings = self.toppings.copy()
        returnStr = "removing all toppings pizza...\n"
        returnStr += self.remove_toppings(allToppings)
            
        return returnStr

    def resize(self, newSize):
        #change the size of the pizza, and update price
        if self.size != newSize:
            #update the price first
            self.price -= 6 + (self.size * 2)
            self.price += 6 + (newSize * 2)
            #then resize
            self.size = newSize
            return "resized pizza"
        else:
            return "pizza is already that size"
    
    def copy(self, newCustomer = None, newSize = None):
        #This will return an identical pizza object by default...
        if newCustomer is None:
            newCustomer = self.customer
        if newSize is None:
            newSize = self.size
        #with the option of a different customer or size
        newPizza = Pizza(newCustomer, newSize)
        for topping in self.toppings:
            newPizza.add(topping, (topping in self.extras))
        
        return newPizza

    def veg(self):
        #This method will return an a copy of the pizza without meat
        newPizza = self.copy()
        for topping in newPizza.toppings:
            if not topping.isVeg:
                newPizza.remove(topping)

        return newPizza

    def clear(self):
        #Returns a copy with no toppings
        newPizza = self.copy()
        newPizza.remove_all()

        return newPizza
    
    def describe(self):
        description = "A {} pizza ".format(Pizza.sizes[self.size])

        if len(self.toppings) > 0:
            description += "with:\n"
            for topping in self.toppings:
                description += " - "
                if topping in self.extras:
                    description += "extra "
                description += "{}\n".format(topping)

        description += "for {} ".format(self.customer)

        if self.isVeg:
            description += "(V) "

        description += "... £{}".format(self.price)
        
        print(description)

#Topping "dictionary"
pepperoni = Topping("pepperoni", False)
chicken = Topping("chicken", False)
mushroom = Topping("mushroom")
olive = Topping("olive")
pineapple = Topping("pineapple")


#   TEST SPACE
myPizza = Pizza("Hugo")
myPizza.add(pepperoni)
myPizza.add(mushroom)
myPizza.add(olive)
myPizza.describe()
myPizza.resize(2)
myPizza.describe()
#TO DO LIST:
# - Streamline + standardise the returnStr/rtrnString
# - Sort into multiple modules/files 


                      
                                           
                    

