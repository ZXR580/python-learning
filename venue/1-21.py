class StudentGPA:
    def __init__(self,name,num,credits,opinions):
        self.name = name
        self.num = num
        self.credits = float(credits)
        self.opinions = float(opinions)
    def getName(self):
        return self.name,self.num
    def getCredits(self):
        return self.credits
    def getOpinions(self):
        return self.opinions
    def gpa(self):
        return self.opinions/self.credits

    def makeStudent(infoStr):
        name,num,credits,opinions=infoStr.split("\t")
        return StudentGPA(name,num,credits,opinions)
