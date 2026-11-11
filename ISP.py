from abc import ABC, abstractmethod

# ---------- Separate Interfaces (ISP) ----------
class Teachable(ABC):
    @abstractmethod
    def teach(self):
        pass

class Researchable(ABC):
    @abstractmethod
    def research(self):
        pass

class Medical(ABC):
    @abstractmethod
    def practice_medicine(self):
        pass

# ---------- Implementing Classes ----------
class ProfessorResearcher(Teachable, Researchable):
    def teach(self):
        print("Professor Researcher: teaching students")

    def research(self):
        print("Professor Researcher: doing research")

class FullTimeResearcher(Researchable):
    def research(self):
        print("Full-time Researcher: doing research")

class ProfessorHospitalResearcher(Teachable, Researchable, Medical):
    def teach(self):
        print("Professor Hospital Researcher: teaching medicine")

    def research(self):
        print("Professor Hospital Researcher: doing medical research")

    def practice_medicine(self):
        print("Professor Hospital Researcher: treating patients")

# ---------- Main ----------
if __name__ == '__main__':
    print("--- Professor Researcher ---")
    p = ProfessorResearcher()
    p.teach()
    p.research()

    print("--- Full-time Researcher ---")
    f = FullTimeResearcher()
    f.research()

    print("--- Professor Hospital Researcher ---")
    h = ProfessorHospitalResearcher()
    h.teach()
    h.research()
    h.practice_medicine()