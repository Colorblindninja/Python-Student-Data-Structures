#CS 2420 
#Hash table
#Zach Swag Lamroeaux


import sys
from student import *
from hashclass import *
import time
import urllib2


TOTAL_AGE = 0.0

def storeAge(student):
  global TOTAL_AGE
  TOTAL_AGE += student.getAge()


def insert(allStudents):
  fin = urllib2.urlopen("http://cit.cs.dixie.edu/cs/2420/ssn/InsertNamesMedium.txt")
  before = time.time()
  for line in fin:
    word = line.split()
    s=Student(word[0], word[1], word[2], word[3], word[4])
    if not allStudents.Insert(s):
      print "Insert Error: %s." %(s)
  totalTime = time.time() - before
  print "Successfully inserted %i students, and it only took %f seconds" %(allStudents.Size(), totalTime)


def traverse(allStudents):
  before = time.time()
  allStudents.Traverse(storeAge)
  totalTime = time.time() - before
  print "The average age of all the students is %f and it took %f seconds" % (TOTAL_AGE/allStudents.Size(), totalTime)


def retrieve(allStudents):
  before = time.time()
  totalAge = 0.0
  count = 0.0
  fin = urllib2.urlopen("http://cit.cs.dixie.edu/cs/2420/ssn/RetrieveNamesMedium.txt")
  for line in fin:
    ssn = line.strip()
    blank_student = Student("", "", ssn, "", "25")
    s = allStudents.Retrieve(blank_student)
    if s:
      totalAge += s.getAge()
      count += 1
  totalTime = time.time() - before
  print "Average age of retrieved students: %f and it took %f seconds" % (totalAge/count, totalTime)


def delete(allStudents):
  before = time.time()
  fin = urllib2.urlopen("http://cit.cs.dixie.edu/cs/2420/ssn/DeleteNamesMedium.txt")
  for line in fin:
    ssn = line.strip()
    blank_student = Student("", "", ssn, "", "25")
    if allStudents.Delete(blank_student):
      continue
    else:
      print "No student found with SSN %s" % ssn
  totalTime = time.time() - before
  print "Number of Students, now: %s and it took %f seconds" % (allStudents.Size(), totalTime)


def main():
  allStudents = Hash(300000)
  insert(allStudents)
  traverse(allStudents)
  delete(allStudents)
  retrieve(allStudents)


main()