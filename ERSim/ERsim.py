#  File: War.py
#  Description: The goal is to simulate the card game War between two players.

#queue class defined, queue operations are defined as methods
class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    #overrided string method that allows for printing the current queue items
    def __str__(self):
        return(str(self.items))

#function defined to update the queue
def update(fairQueue, seriousQueue, criticalQueue): 
    print('   Queues are:')
    print('   Fair:    ', fairQueue)
    print('   Serious: ', seriousQueue)
    print('   Critical:', criticalQueue)
    return('\n')

#main function
def main():   
    #opens file for reading
    inFile = open('ERsim.txt', 'r')

    #initializing the three conditional queues 
    fair = Queue()
    serious = Queue()
    critical = Queue()
    status = ('Fair', 'Serious', 'Critical')

    #reads data line by line in file and processes it
    for line in inFile: 
        command = line.strip()
        command = line.split()

        #case of add command
        if command[0] == 'add': 
            name, condition = command[2], command[1]
            print('Command: Add patient', name, 'to', condition, 'queue\n')

            #patient's are added to condition specified queue
            if condition == 'Fair': 
                fair.enqueue(name)
            elif condition == 'Serious': 
                serious.enqueue(name)
            else: 
                critical.enqueue(name)

            print(update(fair, serious, critical))


        #case of treat next command
        if (command[0] == 'treat') and (command[1] == 'next'):
            print('Command: Treat next patient\n')

            #the next patient's treated (first in line) prioritizing most severe status & removed from queue
            if not critical.isEmpty(): 
                treated = critical.dequeue()
                print('   Treating', '\'' + treated + '\'', 'from Critical queue')
                print(update(fair, serious, critical))

            elif not serious.isEmpty(): 
                treated = serious.dequeue()
                print('   Treating', '\'' + treated + '\'', 'from Serious queue')
                print(update(fair, serious, critical))

            elif not fair.isEmpty():
                treated = fair.dequeue()
                print('   Treating', '\'' + treated + '\'', 'from Fair queue')
                print(update(fair, serious, critical))

            else: 
                print('   No patients in queues\n\n')


        #case of treat specified condition command
        if (command[0] == 'treat') and (command[1] in status):
            print('Command: Treat next patient on', command[1], 'queue\n')
            
            #the first patient in line of the specified condition is treated & removed from queue
            if (command[1] == 'Critical') and (not critical.isEmpty()): 
                treated = critical.dequeue()
                print('   Treating', '\'' + treated + '\'', 'from Critical queue')
                print(update(fair, serious, critical))

            elif (command[1] == 'Serious') and (not serious.isEmpty()): 
                treated = serious.dequeue()
                print('   Treating', '\'' + treated + '\'', 'from Serious queue')
                print(update(fair, serious, critical))

            elif (command[1] == 'Fair') and (not fair.isEmpty()):
                treated = fair.dequeue()
                print('   Treating', '\'' + treated + '\'', 'from Fair queue')
                print(update(fair, serious, critical))

            else: 
                print('   No patients in queue\n\n')    


        #case of treat all command
        if (command[0] == 'treat') and (command[1] == 'all'):
            print('Command: Treat all patients\n')

            #loop designed to treat all remaining patients (first in line) & remove them based on severity 
            while True: 
                if not critical.isEmpty(): 
                    treated = critical.dequeue()
                    print('   Treating', '\'' + treated + '\'', 'from Critical queue')
                    print(update(fair, serious, critical))              

                elif not serious.isEmpty(): 
                    treated = serious.dequeue()
                    print('   Treating', '\'' + treated + '\'', 'from Serious queue')
                    print(update(fair, serious, critical))

                elif not fair.isEmpty():
                    treated = fair.dequeue()
                    print('   Treating', '\'' + treated + '\'', 'from Fair queue')
                    print(update(fair, serious, critical))

                else: 
                    print('   No patients in queues\n\n')
                    break


        #case of exit command
        if command[0] == 'exit': 
            print('Command: Exit')
            break

    #closes file
    inFile.close()

main()