# SORT ANALYZER STARTER CODE

import time

# RETURN DATA FROM FILE AS AN ARRAY OF INTERGERS

def loadDataArray(fileName):
	temp = []

	# Read file line by line
	fileref = open(fileName, "r")
	for line in fileref:
		line = line.strip()  # Clean up line
		temp.append(int(line))  # Add integer to temp list

	fileref.close()

	return temp

# LOAD DATA FILE INTO GLOBAL VARIABLES

randomData          = loadDataArray("data-files/random-values.txt")
reversedData        = loadDataArray("data-files/reversed-values.txt")
nearlySortedData    = loadDataArray("data-files/nearly-sorted-values.txt")
fewUniqueData       = loadDataArray("data-files/few-unique-values.txt")

# VERIFY LOADED DATA BY PRINTING FIRST 50 ELEMENTS

# print(randomData[0:50])
# print(reversedData[0:50])
# print(nearlySortedData[0:50])
# print(fewUniqueData[0:50])

# FUNCTIONS

def bubble_sort(list):
	for i in range(len(list) - 1):
		for j in range(len(list) - i - 1):
			if list[j] > list[j + 1]:
				list[j], list[j + 1] = list[j + 1], list[j]

def selection_sort(list):
	for i in range(len(list) - 1):
		min_index = i

		for j in range(i + 1, len(list)):
			if (list[j] < list[min_index]):
				min_index = j
		
		list[i], list[min_index] = list[min_index], list[i]

def insertion_sort(list):
	for i in range(1, len(list)):
		value = list[i]
		insert_index = i
		
		while insert_index > 0 and list[insert_index - 1] > value:
			list[insert_index] = list[insert_index - 1]
			insert_index -= 1
		
		list[insert_index] = value

iteration_count = 20

def run_sorting(algorithm_name, algorithm, array_name, array):
	print(f"[!] Timing {algorithm_name} on {array_name} data.")
	print()

	sum		= 0
	results	= []

	for i in range(iteration_count):
		print(f"{i}/{iteration_count}", end="\r")

		data = array.copy()

		start = time.time()
		algorithm(data)
		end = time.time()

		result = (end - start) * 1000

		sum += result
		results.append(result)

	print("     ", end='\r') # clear progress coutner

	for i, result in enumerate(results):
		print(f"{i + 1}.\t{result}\tms")

	print()
	print(f"Mean:\t{sum / iteration_count}\tms")
	print()

# TIME DURATIONS OF SORT ALGORITHMS

print()

run_sorting("bubble sort"	, bubble_sort	, "random",			randomData		)
run_sorting("bubble sort"	, bubble_sort	, "reversed",		reversedData	)
run_sorting("bubble sort"	, bubble_sort	, "nearly sorted",	nearlySortedData)
run_sorting("bubble sort"	, bubble_sort	, "few unique",		fewUniqueData	)

run_sorting("selection sort", selection_sort, "random",			randomData		)
run_sorting("selection sort", selection_sort, "reversed",		reversedData	)
run_sorting("selection sort", selection_sort, "nearly sorted",	nearlySortedData)
run_sorting("selection sort", selection_sort, "few unique",		fewUniqueData	)

run_sorting("insertion sort", insertion_sort, "random",			randomData		)
run_sorting("insertion sort", insertion_sort, "reversed",		reversedData	)
run_sorting("insertion sort", insertion_sort, "nearly sorted",	nearlySortedData)
run_sorting("insertion sort", insertion_sort, "few unique",		fewUniqueData	)
