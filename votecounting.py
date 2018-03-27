#-------------------------------------------------------------------------------------------------------#
#_________________________________________ QUESTION ____________________________________________________#
#-------------------------------------------------------------------------------------------------------#


import random
import sys
import time

#Class definition of Candidate
class Candidate:
    #Creating an empty dictionary to hold items(keys & values)
    all_candidates = {}

     #Code for constructor function __init__
    def __init__(self, name = "", party = ""):
        self.name = name
        self.party = party
        self.votes = 0
        Candidate.all_candidates[name] = self #Storing each Candidate details
    
    #Code for function add_vote
    def add_vote(self):
        self.votes = self.votes + 1
        return self.votes

    #Code for function clear_votes
    def clear_votes(self):
        self.votes = 0

    #Code for function lookup(name)
    def lookup(self,name):
        # Lookup the name of the candidate in the voting list.
        if name in Candidate.all_candidates.keys():
            return name
        else:
            return 'None'
    
    #Code for function get_candidate : Defined additionally for program requirement
    def get_candidatelist():
        return list(Candidate.all_candidates.values())
    
    #Code for function initialize(fname)
    def initialize(fname):
        try: #Employs exception handling
            file = open(fname, "r") #Read the data from csv file
            for line in file:
                if not line.isspace():
                    vals = [x.strip("\n") for x in line.split(",")]
                    Candidate(vals[0], vals[1])
            return Candidate.get_candidatelist()
        except: #Throws errors with some waiting time
            time.sleep(1)
            print(sys.exc_info())
            print("***Issue reading CSV File {0}".format(fname))


#Class definition of Individual Vote
class Vote:
    #Creating an empty list to hold values
    all_votes = []
    
    #Code for constructor function __init__
    def __init__(self ,preferences):
        self.__pref = preferences
        Vote.all_votes.append(self)

    #Code for function most_preferred(cands)
    def most_preferred(cands):
        preferred = cands[0]
        return preferred

    #Code for function get_votelist: Defined additionally for program requirement
    def get_votelist():
        return list(Vote.all_votes)

    #Code for function get_pref
    def get_pref(self):
        return (self.__pref)
    
    #Code for function initialize(fname)
    def initialize(fname):
        try: #Employs exception handling
            file = open(fname, "r") #Reads data from csv
            for line in file:
                if not line.isspace():
                    vals = [x.strip("\n") for x in line.split(",")]
                    cands = list(vals)
                    Vote(cands)
            return Vote.get_votelist()
        except: #Throws error with some waiting time
            time.sleep(1)
            print(sys.exc_info())
            print("***Issue reading CSV File {0}".format(fname))

#Ingesting the data from csv files
mycandidate = "candidate.csv"
myvote = "voter.csv"

#Creating class object to initialize
candidates = Candidate.initialize(mycandidate )
votes = Vote.initialize(myvote)
int_cand_name = []
highest = 0

#Creating by_votes to receive votes
by_votes = lambda x: x.votes

#Round 1 of voting begins
for pref in votes:
    preference = pref.get_pref()
    most_pref = Vote.most_preferred(preference)
    for cand in list(candidates):
        candidate_name, candidate_party, candidate_vote = cand.name, cand.party, cand.votes
        if (cand.lookup(most_pref) != None):
            if (candidate_name == most_pref):
                cand.add_vote()

#Results with highest order of Votes received
candidates.sort(key = by_votes, reverse = True)

for cand in list(candidates):
    print(cand.name,cand.party,cand.votes)
    
    #Condition Statement to eliminate the voters with quarterly votes
    if(cand.votes < (len(votes)//4)):
        candidates.remove(cand)
        print("Candidate {0} has been eliminated".format(cand.name))
    cand.clear_votes()    

for cand in list(candidates):
    print(cand.name, cand.party)
    int_cand_name.append(cand.name)

#Round 2 of Preference
for pref in votes:
    preference = pref.get_pref()
    preference = [x for x in preference if x in int_cand_name]
    if(len(preference) >= 1):
        most_pref = Vote.most_preferred(preference)
    else:
        most_pref = "None"
    for cand in list(candidates):
        candidate_name, candidate_party, candidate_vote = cand.name, cand.party, cand.votes
        if (candidate_name == most_pref):
            cand.add_vote()

#Randomly choosing candidates in case of time
random.shuffle(candidates)
candidates.sort(key = by_votes, reverse = True)
for result in candidates:
    print(result.name,result.party,result.votes)
    if(result.votes > highest):
        highest = result.votes
        win_name = result.name
        win_party = result.party

print("Winner is {0} from {1} party".format(win_name,win_party))
