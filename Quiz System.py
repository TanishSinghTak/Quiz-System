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
# 2.  Matrices

class Matrix:
    def __init__(self,matrix):
        self.matrix = matrix
    # method to represent the object matrix in nicely formatted manner 
    def __str__(self):
        s = ""
        # taking different rows to add in string
        for i in range(len(self.matrix)):
            # taking elements one by one from the row to add in the string
            for j in range(len(self.matrix[0])):
                s =  s + ' ' + str(self.matrix[i][j]) 
            # adding new line after adding a row 
            s = s + '\n'
        return s  
    # method to add 2 matrices 
    def __add__(self,b):
        n = len(self.matrix)
        m = len(self.matrix[0])
        # creating the matrix to put elements of sum of 2 matrix 
        c = []
        # raise error if the order of 2 matrix is not same 
        if len(self.matrix) != len(b.matrix) or len(self.matrix[0]) != len(b.matrix[0]):
            raise Exception("matrix order is not same")
        for i in range(n):
            # adding a row in the list
            c+=[[0]*m]
            # adding the (i*j)'th element in the matrix
            for j in range(m):
                c[i][j] = self.matrix[i][j] + b.matrix[i][j]
        return Matrix(c)
    # method to subtract 2 matrices 
    def __sub__(self,b):
        n = len(self.matrix)
        m = len(self.matrix[0])
        # creating the matrix to put elements of difference of  2 matrix 
        c = []
        # raise error if the order of 2 matrix is not same 
        if len(self.matrix) != len(b.matrix) or len(self.matrix[0]) != len(b.matrix[0]):
            raise Exception("matrix order is not same")
        for i in range(n):
            # adding a row in the list
            c+=[[0]*m]
            # adding the (i*j)'th element in the matrix
            for j in range(m):
                c[i][j] = self.matrix[i][j] - b.matrix[i][j]
        return Matrix(c)
    # method to get product of a matrix either with a scalar or another matrix
    def __mul__(self,B):
        n = len(self.matrix)
        l = len(self.matrix[0])
        C = []
        # for scalar multiplication
        if isinstance(B,int):
            for i in range(n):
                C+=[[0]*l]
                for j in range(l):
                    # multiplying each element of matrix with the given scalar
                    C[i][j] = B*self.matrix[i][j]
        # for multiplication with another matrix
        elif isinstance(B,Matrix):
            m = len(B.matrix[0])
            # raise error if the matrix multiplication is not possible for 2 matrices 
            if len(self.matrix[0]) != len(B.matrix):
                raise Exception("matrix multiplication is not possible")
            for i in range(n):
                C+=[[0]*m]
                for j in range(m):
                    for k in range(l):
                        # multiplying and adding every element of i'th row of self matrix
                        # with the every element of j'th column of matrix B in the proper order 
                        # to get i*j'th element of the product matrix
                        C[i][j] += (self.matrix[i][k]*B.matrix[k][j])
        return Matrix(C)
    # method to convert the matrix in sparse format 
    def toSparse(self):
        n = len(self.matrix)
        m = len(self.matrix[0])
        # creating list for sparse format 
        c = []
        for i in range(n):
            # adding i'th row
            c+=[[]]
            for j in range(m):
                # adding a element from original list only if it is not equal to 0
                if self.matrix[i][j] != 0:
                    c[i].append((j,self.matrix[i][j]))
        return c

class SparseMatrix:
    def __init__(self,sparse_matrix,nrows,ncols):
        self.sparsematrix = sparse_matrix
        self.row = nrows
        self.column = ncols
    # method to get any i*j'th element of the list
    def elem(self,i,j):
        t = 0
        # checking that if there is an element in the i'th row with j'th index 
        while t < len(self.sparsematrix[i]):
            (a,b) = self.sparsematrix[i][t]
            if a < j:
                t+=1
            # giving 0 if we can't find element with required index
            if a > j:
                return 0
            # returning element if we find the required index
            if a == j:
                return b
        # returning 0 if we have covered all elements  of the list 
        # which means the element is 0
        if j >= len(self.sparsematrix[i]):
            return 0      
    # method to representing sparsematrix in nicely formatted manner 
    def __str__(self):
        s = ""
        # taking different rows to add in string
        for i in range(self.row):
            j = 0 
            t = 0
            # taking elements one by one from the row to add in the string
            while j < self.column:
                # adding 0's for the rest of indices if the list is completed
                if t == len(self.sparsematrix[i]):
                    s = s + " 0"*(self.column - j)
                    break
                (a,b) = self.sparsematrix[i][t]
                # adding the i*j'th element in the string 
                if a == j:
                    s = s + " " + str(b)
                    t+=1
                else:
                    s = s + " " + "0"
                j+=1
            # adding the new line in the string for the next row 
            s = s + "\n"
        return s
    # method to add 2 sparse matrices 
    def __add__(self,B):
        # creating matrix to store sum of 2 matrices
        C = []
        # raise error if the order of 2 matrix is not same 
        if self.row != B.row or self.column != B.column:
            raise Exception("matrix order is not same")
        # getting i'th row of the sum
        for i in range(self.row):
            C+=[[]]
            j = 0 
            t = 0
            u = 0
            # adding i*j'th element of sum in the matrix
            while j < self.column:
                # adding rest of the elements of matrix B if self matrix is covered 
                if t == len(self.sparsematrix[i]):
                    C[i] += B.sparsematrix[i][u:len(B.sparsematrix[i])]
                    break
                # adding rest of the elements of self matrix  if matrix B is covered 
                if u == len(B.sparsematrix[i]):
                    C[i] += self.sparsematrix[i][t:len(self.sparsematrix[i])]
                    break
                (a,b) = self.sparsematrix[i][t]
                (c,d) = B.sparsematrix[i][u]
                # directly adding the i*j'th element of self matrix if the element of matrix B is 0 
                if a == j and c != j:
                    C[i].append((j,b))
                    t+=1
                # directly adding the i*j'th element of matrix B if the element of self matrix is 0 
                if c == j and a != j:
                    C[i].append((j,d))
                    u+=1
                # adding sum of both i*j'th elements of the matrices if they both are present
                if c == j and a == j:
                    C[i].append((j,b+d))
                    t+=1
                    u+=1
                j+=1
        return SparseMatrix(C,self.row,self.column)
    # method to sbtract 2 sparse matrices 
    def __sub__(self,B):
        # creating matrix to store difference of 2 matrices
        C = []
        # raise error if the order of 2 matrix is not same 
        if self.row != B.row or self.column != B.column:
            raise Exception("matrix order is not same")
        # getting i'th row of the difference
        for i in range(self.row):
            C+=[[]]
            j = 0 
            t = 0
            u = 0
            # adding i*j'th element of difference in the matrix
            while j < self.column:
                # adding rest of the elements of matrix B by changing sign if self matrix is covered 
                if t == len(self.sparsematrix[i]):
                    while u < len(B.sparsematrix[i]):
                        (c,d) = B.sparsematrix[i][u]
                        C[i].append((c,-(d)))
                        u+=1
                    break
                # adding rest of the elements of self matrix if matrix B is covered 
                if u == len(B.sparsematrix[i]):
                    C[i] += self.sparsematrix[i][t:len(self.sparsematrix[i])]
                    break
                (a,b) = self.sparsematrix[i][t]
                (c,d) = B.sparsematrix[i][u]
                # directly adding the i*j'th element of self matrix if the element of matrix B is 0 
                if a == j and c != j:
                    C[i].append((j,b))
                    t+=1
                # directly adding the i*j'th element of matrix B by changing sign if the element of self matrix is 0 
                if c == j and a != j:
                    C[i].append((j,-(d)))
                    u+=1
                # adding difference of both i*j'th elements of the matrices if they both are present
                if c == j and a == j:
                    C[i].append((j,b-d))
                    t+=1
                    u+=1
                j+=1
        return SparseMatrix(C,self.row,self.column)
    # method to get product of a sparsematrix either with a scalar or another sparsematrix
    def __mul__(self,B):
        C = []
        # for scalar multiplication
        if isinstance(B,int):
            for i in range(self.row):
                C+=[[]]
                for j in range(len(self.sparsematrix[i])):
                    (a,b) = self.sparsematrix[i][j]
                    # multiplying each element of matrix with the given scalar
                    C[i]+=[(a,b*B)]
        # for multiplication with another matrix
        elif isinstance(B,SparseMatrix):
            n = self.row
            l = self.column
            m = B.column
            # raise error if the matrix multiplication is not possible for 2 matrices 
            if self.column != B.row:
                raise Exception("matrix multiplication is not possible")
            for i in range(n):
                C+=[[]]
                for j in range(m):
                    sum = 0
                    for k in range(l):
                        # multiplying and adding every element of i'th row of self matrix
                        # with the every element of j'th column of matrix B in the proper order 
                        # to get i*j'th element of the product matrix
                        sum += (self.elem(i,k)*B.elem(k,j))
                    # if the product is 0 then we will not add this element in the list  
                    if sum != 0:
                        C[i].append((j,sum))
        return SparseMatrix(C,self.row,B.column)
    # method to convert the matrix in dense format 
    def toDense(self):
        # creating list for sparse format 
        C = []
        for i in range(self.row):
            # adding i'th row
            C += [[]]
            j = 0 
            t = 0
            while j < self.column:
                # adding 0 in the list if the sparsematrix is completed but the row is incomplete
                if t == len(self.sparsematrix[i]):
                    C[i] =  C[i] + [0]*(self.column - j)
                    break
                (a,b) = self.sparsematrix[i][t]
                # adding i*j'th element in matrix 
                if a == j:
                    C[i] +=[b]
                    t+=1
                # adding 0 if we can't find element with current index
                else:
                    C[i]+=[0]
                j+=1
        return C
#######################################################################################################################