# implementing autocomplete with Ternary Search Tree
# Code taken from
# http://hacktalks.blogspot.com/2012/03/implementing-auto-complete-with-ternary.html
# Modified to Include tests
#Please Check This link For Theory Of TST :
# http://en.wikipedia.org/wiki/Ternary_search_tree

# Each node contains 5 parts They are
# self.ch => contains the character
# self.flag => Flag to Check whether the node is an end character of a valid string
# self.left, self.right => Links to the next nodes ( Working similar to Binary Search Tree)
# self.center => Link to the next valid character

global aList
class Node:     
    def __init__(self,ch,flag): # Constructor for Node Object
        self.ch = ch
        self.flag = flag
        self.left = 0
        self.right = 0
        self.center = 0                    

    def Add(self,string,node): # Function to add a string 

        key = string[0] 
        
        if node == 0 :
            node = Node(key,0) 

        if key < node.ch :          
            node.left = node.Add(string,node.left)  

        elif key > node.ch :          
            node.right = node.Add(string,node.right)

        else :  
            if len(string) == 1 :
                node.flag = 1  
            else : node.center = node.Add(string[1:],node.center)
            
        return node    

    def spdfs(self,match):  # DFS for Ternary Search Tree
        
        if self.flag == 1 :
            aList.append(match)
##            print("Match : ",match)  
            
        if self.center == 0 and self.left == 0 and self.right == 0:            
            return aList
                         
        if self.center != 0 :            
            self.center.spdfs(match + self.center.ch)
            
            
        if self.right != 0 :         
            self.right.spdfs(match[:-1]+self.right.ch)            
            
        if self.left != 0 :            
            self.left.spdfs(match[:-1]+self.left.ch)  

    def simple(self,string):  # Function to search a string in the Ternary Search Tree
        temp = self
        i=0
        while temp != 0 :
            if (string[i] < temp.ch) :  temp = temp.left;
            elif(string[i] > temp.ch) : temp = temp.right;
            else :
                i=i+1              
                if(i == len(string)):
                    return temp.flag 
                temp = temp.center

        return 0
            
    
        
    def search(self,string,match):
        # Function to implement Auto complete search
    
        if len(string) > 0:
            key = string[0]

            if key < self.ch :
                if(self.left == 0):
##                    print("No Match Found")
                    return []                           
                self.left.search(string,match)

            elif key > self.ch :
                if(self.right == 0):
##                    print("Not Match Found")
                    return []
                self.right.search(string,match)

            else :                
                if len(string) == 1:
##                    if self.flag == 1 : print("Match ",match+self.ch)
                    if self.flag == 1 : aa=1#aList.append(self.ch)
                    if self.center != 0 :
                        self.center.spdfs(match+self.ch+self.center.ch)
                    return 1                
                self.center.search(string[1:],match+key)                        
            
        else :
##            print("Invalid String")
            return []
            
def fileparse(filename,node):

    #Parse the Input Dict file and build the TST   
    fd = open(filename)    
    line = fd.readline().strip('\r\n') 
    while line !='':
        
        node.Add(line,node)
        line = fd.readline().strip('\r\n')


##if __name__=='__main__':
    
root = Node('',0)

# Give the Path to the Dictionary File in
##Path_to_dict = "dict.txt"
##
##fileparse(Path_to_dict,root)
root.Add('moorthy',root)
root.Add('cat',root)
root.Add('cap',root)
root.Add('bath',root)
root.Add('bat',root)
root.Add('beppo',root)
root.Add('rpi',root)
root.Add('rit',root)
aList=[]
root.search('abc','')
assert(aList==[]),"rror in auto completing abc"
alist=[]
root.search('moo','')
assert(aList==['moorthy']), "Error for Autocompleting moo"
aList=[]
root.search('ca','')
aList.sort()
assert(aList==['cap','cat']),"Error for autocompleting ca"
aList=[]
root.search('ba','')
aList.sort()
assert(aList==['bat','bath']),"Error for autocompleting ba"
aList=[]
root.search('r','')
aList.sort()
assert(aList==['rit','rpi']),"Error for autocompleting r"

##inp = ''
##while inp !='q':
##    aList=[]
##    inp = raw_input("Enter String : ",)
##    root.search(inp,'')
##    print(aList)

