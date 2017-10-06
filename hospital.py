class Patient(object):
    def __init__(self, idNum, name, allergies):
        self.id = idNum
        self.name = name
        self.allergies = allergies
        self.bed = 0

    def display(self):
        print ""
        print self.id 
        print self.name 
        print self.allergies
        print self.bed
    
class Hospital(object):
    def __init__(self,name):
        self.patients = []
        self.name = name
        self.capacity = 3

    def admit(self, p):
        if len(self.patients) < self.capacity:
            self.patients.append(p)
            p.bed = len(self.patients)
            print "welcome to the hospital"
        else:
            print "sorry u gon die"
        return self
    
    def discharge(self, p):
        p.bed = 0
        self.patients.remove(p)
        print "get out of the hospital"
        return self

    def displayPeople(self):
        print "PATENTS:"
        for i in self.patients:
            i.display()
        return self

p1 = Patient(1001, "Jon", "peanut")
p2 = Patient(2002, "Alice", "gatorade")
p3 = Patient(3003, "Zeke", "hot sauce")
p4 = Patient(4004, "Linden", "doritos")
Kaiser = Hospital("Kaiser")

Kaiser.admit(p1).admit(p2).admit(p3).admit(p4).discharge(p3).displayPeople()

    
