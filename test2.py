class Mystring:
    def __init__(self,s):
        self.s=s
        pass
    
    def reverse_words(self):
        mot= self.s.split()
        mot.reverse()
        return mot
    
    def reverse_characters(self):
          return self.s[::-1]
        
    def count_words(self):
        return len(self.s.split())
    
    def count_characters(self):
         return len(self.s) 
     
    def replace_words(self,words,thiaw):
        return self.s.replace(words,thiaw)  
        
    def replace_letter(self,letter,de):
        return self.s.replace(letter,de)       
          
p=Mystring("thiaw")
print(p.reverse_characters())
print(p.count_characters())
print(p.count_words())
print(p.replace_letter("thiaw","letter"))
print(p.replace_words("words","thiaw"))
print(p.reverse_words())