import os
import sys
import sqlite3

dirname = os.path.dirname(os.path.abspath(__file__))

db = sqlite3.connect(os.path.abspath(os.path.join(
    dirname, 'db', 'employee.db')))

cursor = db.cursor()

marks = 0
line_no = 0
checker = 1


def Execute(line):
    global marks, remarks, line_no, testOutput, checker
    try:
        checker = 1
        marks += 2
        cursor.execute(line)
    except Exception as e:
        checker = 0
        marks -= 2
        remarks.write("Line: "+str(line_no)+"     "+str(e)+"\n")
    if(checker == 1):
        testOutput.write(str(cursor.fetchall())+"\n")
    else:
        testOutput.write("\n")


if __name__ == "__main__":
    # Execute the commands of the student file

    if(len(sys.argv) != 2):
        print("Invalid no. of arguments")
        sys.exit(0)

    studentId = sys.argv[1].strip()
    testFilePath = os.path.abspath(os.path.join(
        dirname, '..', 'test', '{id}.txt'.format(id=studentId)))
    testOutputPath = os.path.abspath(os.path.join(
        dirname, '..', 'test', '{id}-output.txt'.format(id=studentId)))
    remarksPath = os.path.abspath(os.path.join(
        dirname, '..', 'test', '{id}-remarks.txt'.format(id=studentId)))

    testFile = open(testFilePath, 'r')
    testOutput = open(testOutputPath, 'w')
    remarks = open(remarksPath, 'w')
    for line in testFile:
        line_no += 1
        Execute(line)
    testFile.close()
    testOutput.close()
    db.commit()
    db.close()

    # Compare the output of the executions with the expected outputs
    testOutput = open(os.path.abspath(os.path.join(
        dirname, '..', 'test', '{id}-output.txt'.format(id=studentId))), 'r')
    expectedOutput = open(os.path.abspath(os.path.join(
        dirname, '..', 'assignments', '1', 'answers-output.txt')), 'r')
    counter = 0
    score_x = 10
    for given in testOutput:
        counter += 1
        for actual in expectedOutput:
            if(given != actual):
                score_x -= 2
                remarks.write("Answer:" + str(counter) +
                              " not matching the answer key\n")
            break

    print("Score:", min(score_x, marks))
    remarks.close()
    testOutput.close()
    expectedOutput.close()

    os.remove(testFilePath)
    os.remove(testOutputPath)
