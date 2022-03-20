# Quiz-System
Python code for an automatic quiz system similar to Moodle.

## Introduction
In this the basics of an automatic quiz system, similar to Moodle have been implemented, through which students can take quizzes in their courses.Each student is assigned an entry number and a list of courses they are taking. A course code and a series of quizzes are assigned to each course. Each quiz has a title and stores the correct options for each question (assuming that the question and answer texts don’t need to be stored). Each quiz also maintains track of how many attempts each student has made. So these are the classes we'll need, along with their data attributes to implement this system:
* **Student** : This class will have a public attribute entryNo in string format, and a private attribute for a list of Course objects.
* **Course** : This class will have a public attribute courseCode in string format, and a private attribute for a list of Quiz objects.
* **Quiz** : This class will have a public attribute title in string format, and a private attribute for the list of correct options. It also have other private attributes to store the students’ attempts so that they can be retrieved later.

Now the public method in the class **Course** is : 
* **quiz** : This method is used to find the list of quizzes of the given course.

Now the public methods in the class **Student** is :
* **attempt** : The student's answers to the quiz with the specified title in the course with the given course code are recorded using this method. If the student has already attempted the quiz, the fresh attempt will be ignored.
* **getUnattemptedQuizzes** : This method returns a list of pairs (courseCode, quizTitle) representing quizzes in the student’s courses that they have not attempted yet.
* **getcourseans** : This method is used to get a list of student's answers with the quiz title.
* **getAverageScore** : This method returns the student’s average score, i.e. (total correct answers)/(number of attempted quizzes), in the course with the given code.
