#  File: Bowling.py
#  Description: The goal is to simulate tenpin bowling.

def main(): 
	
	#open's file for reading, each line of text is processed, chars are stored in list var
	inFile = open('scores.txt', 'r')
	for line in inFile: 
		scores = line.strip()
		scores = line.split()

		#original list's data is replicated, all "-" are replaced 
		numScores = scores[::]
		for i in range(len(numScores)): 
			if numScores[i] == '-': 
				numScores[i] = '0'

		#initializes variables to be used, while loop is designed to configure the running total & scores of frames 1->9
		i, total, frame, frameTotals = 0, 0, [], []
		while i > -1: 

			#unique case of 10th frame, breaks out of loop, appends corresp scores
			if len(frameTotals) == 9: 
				frame.append(scores[i:])
				tenth = scores[i:]
				break
			
			#case a strike is scored, score is appended, running total is configured based on 2 bonus bowls
			if numScores[i] == 'X':
				total += 10
				frame.append([scores[i], ' ', ' '])

				if '/' in numScores[i : i+3]: 
					total += 10
					frameTotals.append(total)
					i += 1 
					continue

				if numScores[i + 1].isdigit():
					total += int(numScores[i + 1]) 
				else: 
					total += 10
				if numScores[i + 2].isdigit(): 
					total += int(numScores[i + 2])
				else: 
					total += 10
				frameTotals.append(total)
				
			#case a spare is scored, scores are appended, running total is configured based on 1 bonus bowl
			if numScores[i] == '/': 
				total += 10  
				if numScores[i + 1] == 'X':
					total += 10
					frameTotals.append(total) 
					frame.append([scores[i - 1], ' ', scores[i]])
				else: 
					total += int(numScores[i + 1])
					frameTotals.append(total) 
					frame.append([scores[i - 1], ' ', scores[i]])
				
			#case neither a spare or a strike is rolled, scores are appended, running total is configured
			if numScores[i].isdigit() and numScores[i + 1].isdigit(): 
				total += (int(numScores[i]) + int(numScores[i + 1]))
				frameTotals.append(total)
				frame.append([scores[i], ' ', scores[i + 1]])
				i += 1

			i += 1							


		#calls recursive function which returns a list containing a running total of ea frame
		frameTotals = tenthFrame(i, numScores, total, frameTotals)

		#printing the requested output
		if len(tenth) == 3: 
			tenth.insert(1, ' ')
			tenth.insert(3, ' ')
		else: 
			tenth.insert(1, ' ')
		
		print('  1   2   3   4   5   6   7   8   9    10  ')
		print('+---+---+---+---+---+---+---+---+---+-----+')

		#prints the scores of each frame
		print('|', end = '')
		j = 0
		for turn in frame: 
			if j == 9:
				for idx2 in tenth: 
					print(idx2, end = '')
				if len(tenth) == 3: 
					print('  ', end = '')
			else: 
				for idx in turn:  
					print(idx, end = '')
				j += 1

			print('|', end = '')
		
		print()

		#prints the running total per each frame
		print('|', end = '')
		j = 0
		for subtotal in frameTotals: 
			if j == 9: 
				print('%5d|' % (subtotal), end = '')
				break
	
			print('%3d|' % (subtotal), end = '')
			j += 1

		print()
		print('+---+---+---+---+---+---+---+---+---+-----+')
		print()

	inFile.close()


#recursive function is utilized to acquire the 10th frame total for all variations
def tenthFrame(start, numScores, total, frameTotals): 

	if start >= len(numScores):
		frameTotals.append(total)
		return frameTotals

	elif numScores[start] == 'X':
		total += 10
		return(tenthFrame(start + 1, numScores, total, frameTotals))

	elif numScores[start] == '/': 
		total += 10
		total -= int(numScores[start - 1])
		return(tenthFrame(start + 1, numScores, total, frameTotals))

	else: 
		total += int(numScores[start])
		return(tenthFrame(start + 1, numScores, total, frameTotals))

main()