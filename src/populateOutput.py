import sqlite3
import os

dirname = os.path.dirname(os.path.abspath(__file__))

db = sqlite3.connect(os.path.abspath(os.path.join(
    dirname, 'db', 'employee.db')))
cursor = db.cursor()

answerFile = open(os.path.abspath(os.path.join(
    dirname, '..', 'assignments', '1', 'answers.txt')), 'r')
answerOutputFile = open(os.path.abspath(os.path.join(
    dirname, '..', 'assignments', '1', 'answers-output.txt')), 'w')

for line in answerFile:
    cursor.execute(line)
    answerOutputFile.write(str(cursor.fetchall())+"\n")

answerFile.close()
answerOutputFile.close()
