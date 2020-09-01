#  File: Friends.py
#  Description: The goal is to simulate the friend network funtionality of present social media sites

#class user is defined
class User: 
    # constructor is created & names and friends are initialized 
    def __init__(self, name): 
        self.name = name
        self.friends = UnorderedList()

    #overrided string method that allows for printing 
    def __str__(self):
        return(str(self.name))


#Node class is defined, represents item in linked list 
class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext

#unordered list class is defined
class UnorderedList:
    def __init__(self):
        self.head = None

    def __str__(self): 
        s = '[ '
        current = self.head
        for i in range(self.size()): 
            item = current.getData()
            s += str(item) + ' '
            current = current.getNext()
        s += ']'
        return(s)

    def isEmpty(self):
        return self.head == None

    def add(self,item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()

        return count

    def search(self,item):  
        current = self.head
        found = False
        while (current != None) and not found:
            obj = current.getData()
            if obj.name == item:
                found = True
            else:
                current = current.getNext()

        if found == True: 
            return obj
        else: 
            return False

    def remove(self,item):
        current = self.head
        previous = None
        found = False
        while not found:
            obj = current.getData()
            if obj.name == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())


#function defined to check for friend, unfriend, query input validation 
def inputValidation(user1, user2, name1, name2, instruction, allUsers): 
    #checks if the users, in the command statement, are valid
    if not user1 or not user2: 
        if not user1: 
            print('    A person with name', name1, 'does not currently exist.')
        if not user2:
            print('    A person with name', name2, 'does not currently exist.')
        return False
    
    #checks if friend command is valid (cant friend self, cant friend an existing friend)
    if instruction == 'Friend': 
        if name1 == name2:
            print('    A person cannot friend him/herself.')
            return False
        elif user1.friends.search(name2) == user2: 
            print('   ', name1, 'and', name2, 'are already friends.')
            return False
        else: 
            return True

    #checks if unfriend command is valid (cant unfriend self, cant unfriend someone not on friend'slist)
    if instruction == 'Unfriend': 
        if name1 == name2:
            print('    A person cannot unfriend him/herself.')
            return False
        elif not user1.friends.search(name2): 
            print('   ', name1, 'and', name2, 'aren\'t friends, so you can\'t unfriend them.')
            return False 
        else: 
            return True

    #checks if query command is valid (cant query self)
    if instruction == 'Query': 
        if name1 == name2:
            print('    A person cannot query him/herself.')
            return False
        else: 
            return True


#main function 
def main(): 
    #opens file for reading
    inFile = open('FriendData.txt', 'r')

    #unordered list is created to maintain a collection of all created accounts
    allUsers = UnorderedList()

    #reads data line by line in file and processes it
    for line in inFile: 
        command = line.strip()
        command = line.split()

        instruction = command[0]

        #case of adding an account
        if instruction == 'Person':
            username = command[1]
            print('\n--> Person', username)
            if not allUsers.search(username): 
                print('   ', username, 'now has an account.')
                account = User(username)
                allUsers.add(account)
            else:
                print('    A person with name', username, 'already exists.')


        #case of valid friending 
        if (instruction == 'Friend'):
            name1, name2 = command[1], command[2]
            print('\n--> Friend', name1, name2)
            user1, user2 = allUsers.search(name1), allUsers.search(name2)

            if inputValidation(user1, user2, name1, name2, instruction, allUsers): 
                print('   ', name1, 'and', name2, 'are now friends.')
                #Update friend UnorderedList
                user1.friends.add(user2)
                user2.friends.add(user1)


        #case of valid unfriending
        if (instruction == 'Unfriend'):
            name1, name2 = command[1], command[2]
            print('\n--> Unfriend', name1, name2)
            user1, user2 = allUsers.search(name1), allUsers.search(name2)

            if inputValidation(user1, user2, name1, name2, instruction, allUsers): 
                print('   ', name1, 'and', name2, 'are no longer friends.')
                #Update friend UnorderedList
                user1.friends.remove(name2)
                user2.friends.remove(name1)


        #case of listing all friends of specified user 
        if instruction == 'List': 
            username = command[1]
            user = allUsers.search(username)
            print('\n--> List', username)

            if not user:
                print('    A person with name', username, 'does not currently exist.')
            else:
                if not user.friends.isEmpty(): 
                    print('   ', user.friends)
                else: 
                    print('   ', username, 'has no friends.')


        #case of checking if two specified users are currenty friends
        if instruction == 'Query': 
            name1, name2 = command[1], command[2]
            print('\n--> Query', name1, name2)
            user1, user2 = allUsers.search(name1), allUsers.search(name2)

            if inputValidation(user1, user2, name1, name2, instruction, allUsers): 
                if user1.friends.search(name2) == user2: 
                    print('   ', name1, 'and', name2, 'are friends.')
                else: 
                    print('   ', name1, 'and', name2, 'are not friends.')


        #case of exit command
        if instruction == 'Exit': 
            print('\n--> Exit\n    Exiting...')
            break

    #close file
    inFile.close()

main()