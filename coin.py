import random

class Coin:
    def __init__(self,rare =False,clean = True,heads = True,**kwargs):

        for key,value in kwargs.items():
            setattr(self,key,value)

        self.is_rare = rare
        self.is_clean = clean
        self.heads = heads

        if self.is_rare:
            self.value + self.original_value*1.25
        else:
             self.value = self.original_value

        if self.is_clean:
            self.colour = self.clean_colour
        else:
            self.colour = self.rusty_colour

    def rust(self):
        self.colour = self.rusty_colour

    def clean(self):
        self.colour = self.clean_colour

    def __del__(self):
        print("Coin spent!")

    def flip(self):
        heads_options = [True,False]
        choice = random.choice(heads_option)
        self.heads = choice

    def __str__(self):
        if self.original_value >= 1.00:
            return "{}Rupee Coin".format(int(self.original_value))
        else:
            return "{}Rupees Coin".format(int(self.original_value*100))

class One_rupee(Coin):
    def __init__(self):
        data ={"original_value":1,
             "clean_colour":"silver",
             "rusty_colour":"silver",
             "num_edges":1,
             "diameter":25,
             "thickness":1.45,
             "mass":4.85,
          }

        super().__init__(**data)


class Two_rupee(Coin):
    def __init__(self):
        data ={"original_value":2,
             "clean_colour":"silver",
             "rusty_colour":"silver",
             "num_edges":1,
             "diameter":27,
             "thickness":1.54,
             "mass":5.62,
          }

        super().__init__(**data)


class Five_rupee(Coin):
   def __init__(self):
       data ={"original_value":5,
            "clean_colour":"silver",
            "rusty_colour":"silver",
            "num_edges":1,
            "diameter":23,
            "thickness":1.9,
            "mass":6,
         }

       super().__init__(**data)


class Ten_rupee(Coin):
    def __init__(self):
        data ={"original_value":10,
             "clean_colour":"gold,silver",
             "rusty_colour":"gold,silver",
             "num_edges":1,
             "diameter":27,
             "thickness":1.7,
             "mass":7.71,
          }

        super().__init__(**data)


class Twenty_rupee(Coin):
    def __init__(self):
        data ={"original_value":20,
             "clean_colour":"gold,silver",
             "rusty_colour":"gold,silver",
             "num_edges":1,
             "diameter":27,
             "thickness":1.7,
             "mass":8.54,
          }

        super().__init__(**data)


coins =[One_rupee(),Two_rupee(),Five_rupee(),Ten_rupee(),Twenty_rupee()]

for coin in coins:
    arguments =[coin,coin.colour,coin.value,coin.diameter,coin.thickness,coin.num_edges,coin.mass]

    string = "{}-Colour:{},value:{},diameter:{},thickness(mm):{},number of edges:{},mass(g):{}"
    print(string.format(*arguments))
 


       
 

        




       

       

    

        

        

               
        
        
