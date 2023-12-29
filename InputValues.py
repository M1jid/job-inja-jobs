class Inputer:
    '''this class for Make a title and location and category
    
        inputs:
        titel which by default هوش مصنوعی 
        location which by default تهران 
        category  which by default 1
        
        outputs:
        titel & location & category
    '''
    def __init__(self,titel = 'هوش مصنوعی', location = "تهران" , category = None):

        self.titel    = titel
        self.location = location
        self.category = category
        
    #Create tite    
    def title(Inputer):
        job = input('enter your job title')
        Inputer.titel = job
        return Inputer.titel
    
    #Create locatin
    def locatin(Inputer):
        loc = input('enter your location job')
        self.location  = loc
        return self.location
    #Create category
    def category(Inputer):
        category = input('enter category ==> برنامه نویسی ') # number 2 , 3 ... for next version and or category
        self.category = category
        return self.category


