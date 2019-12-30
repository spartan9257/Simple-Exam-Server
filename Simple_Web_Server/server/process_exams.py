from os import path

#Parses through the data file containing exam results
#Then generates statistics.
#Currently only a correct answers value is generated.
#Additional stats can be easily implemented.

#enter the name of the file that contains the results
valid_response = False
while(not valid_response):
    student_data_file = input("Enter the name of the file including .txt: ")
    if path.exists(student_data_file):
        read_file = open(student_data_file,"r")
        break
    else:
        print("Error! File: " + student_data_file + " doesn't exist.")

#Determin pass/fail and save "name: status" to a text file
students = {}
for line in read_file:

    #Determin the index values for each comma
    found = True
    start = 0
    comma_indexes = [0]
    last_comma_index = 0
    while(found):
        index = line.find(",", start)
        if index == -1:
            break
        else:
            comma_indexes.append(index)
            start = index + 1
            last_comma_index = index

    #Transform the data into a list for easy parsing
    counter = 1
    student_info = []
    for item in comma_indexes:
        #if the last comma is being evaluated STOP the appending
        if item != last_comma_index:
            end_index = comma_indexes[counter]
            if item > 0:
                item = item + 1
            student_info.append(line[item:end_index])
            counter = counter + 1


    #Determine if each student passed/failed
    #Open answer sheet file
    answers_file = open("answer_sheet.txt", "r")
    start_counter = 3
    stop_counter = 4
    correct_answers = 0
    for answer in answers_file:
        start = comma_indexes[start_counter]
        stop = comma_indexes[stop_counter]
        student_answer = line[start+1:stop]
        if student_answer == answer.rstrip():
            correct_answers = correct_answers + 1
        start_counter = start_counter + 1
        stop_counter = stop_counter + 1
    print(line[comma_indexes[0]:comma_indexes[2]] + " " + "correct answers: " + str(correct_answers))
    answers_file.close()
read_file.close()