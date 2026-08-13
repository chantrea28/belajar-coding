class vehicle:
    def __init__(self,brand,model,color,maxspeed):
        self.brand = brand
        self.model = model
        self.color = color
        self.maxspeed = maxspeed

    def start(self):
        msg =str(self.brand) + "lampu hijau jalan"

        return(msg) 
    
    def stop(self):
        msg = str(self.brand) + "lampu merah berhenti"

        return(msg)

        
    def turn(self):
        msg = str(self.brand) + "dilarang putar balik "  

        return(msg)



class truck(vehicle):
    def __init__(self,size,capacity):
        self.size = size
        self.capacity = capacity



object1 = truck("big","30 orang")
print(object1.size)
print(object1.capacity) 






    
              
