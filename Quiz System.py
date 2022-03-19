# 1.  Quiz System Design

class Quiz:
    def __init__(self,quizno,anslist):
        self.title = quizno
        self._answers = anslist

class Course:
    def __init__(self,courseCode,quizlist):
        self.courseCode = courseCode
        self._quiz = quizlist
    # method to get the list of all quizes of the course
    def quiz(self):
        c =[]
        # adding the quiz titles with the coursecode in list 
        for elem in self._quiz:
            c.append((self.courseCode,elem.title))
        return c 

class Student:
    # list to store the answers of the students
    answers = []
    # list to store the attemptedquiz of the student
    attemptedquiz = []
    def __init__(self,entryNo,courselist):
        answers = []
        attemptedquiz = []
        self.entryNo = entryNo
        self._courselist = courselist
        self.answers = answers
        self.attemptedquiz = attemptedquiz
    # method to store all attempted quiz and their answers 
    def attempt(self, courseCode, quizTitle, attemptedAnswers):
        # if quiztitle is not in the list already we will add it into the attempted quiz list
        # and respective answers for the quiz in the answers list
        if (courseCode,quizTitle) not in self.attemptedquiz:
            self.attemptedquiz.append((courseCode,quizTitle))
            self.answers.append(attemptedAnswers)
    # method to get unattempted quizzes
    def getUnattemptedQuizzes(self):
        c =[]
        # checking for every course 
        for elem in self._courselist:
            # checking every quiz in the current course that is it present in
            # the attempted quizes of the student 
            for elem2 in elem.quiz():
                if elem2 not in self.attemptedquiz:
                    # appending quiz in the list if it is not attempted
                    c.append(elem2)
        return c
    # method to get a list of students answers with the quiz title 
    def getcourseans(self,courseCode):
        # list to store the indices of attempted quizes of the given course
        c = []
        # getting index of all the attempted quizzes of the given course  
        for i in range(len(self.attemptedquiz)):
            (a,b) = self.attemptedquiz[i]
            if a == courseCode:
                c.append(i)
        # list to store the answers with quiz titles
        d = []
        for i in range(len(c)):
            l = self.answers[c[i]]
            (m,n) = self.attemptedquiz[c[i]]
            d.append((n,l))
        return d  
    # method to get the average score of the student for given course 
    def getAverageScore(self, courseCode):
        # list of student's answers with the quiz title for given course
        l = self.getcourseans(courseCode)
        n = len(l)
        correctans = 0
        # getting the course from all the courses of the student
        for elem in self._courselist:
            if elem.courseCode == courseCode:
                d = elem 
        # getting total correct answers for given course 
        for i in range(len(l)):
            # taking a quiz item with its answers
            (a,b) = l[i]
            # finding the current quiz in the total quizzes 
            # from all the quizzes of given course
            for elem in d._quiz:
                if elem.title == a:
                    # comparing all answers of the student with the correct answers 
                    for j in range(len(b)):
                        if b[j] == elem._answers[j]:
                            # adding 1 if the answer is correct 
                            correctans+=1
        # taking the average of correct answers 
        avg = correctans/n
        return avg

#####################################################################################################################################
