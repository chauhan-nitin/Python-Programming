############################################################
#----------------------- QUESTION -------------------------#
############################################################

#Save the required text files mary_roche.txt and nicholas.txt in same folder

import re

#Defining the class marriage
class Marriage:
    #Creating a constructor function
    def __init__(self , name, year, groupReg , district , quarter , volumeNo , pageNo):
        self.name = name
        self.year = year
        self.groupReg = groupReg
        self.district = district
        self.quarter = quarter
        self.volumeNo = volumeNo
        self.pageNo = pageNo

    #Creating function definition for get_Name   
    def get_Name(self):
        return self.name

    #Creating function definition for get_Year
    def get_Year(self):
        return self.year

    #Creating function definition for get_GroupReg
    def get_GroupReg(self):
        return self.groupReg

    #Creating function definition for get_District
    def get_District(self):
        return self.district

    #Creating function definition for get_Quarter
    def get_Quarter(self):
        return self.quarter

    #Creating function definition for get_VolumeNo
    def get_VolumeNo(self):
        return self.volumeNo

    #Creating function definition for get_PageNo
    def get_PageNo(self):
        return self.pageNo

#Creating two empty lists that holds Mary and Nicholas details
maryDetailsList = []
nicholasDetailsList = []
tempName = ""
tempYear = ""
tempGroupReg = ""
tempDistrict = ""
tempQuarter = ""
tempVolumeNo = ""
tempPageNo = ""

filelist = ["mary_roche.txt","nicholas.txt"]

for file in filelist:
    with open(file) as currentFile:
        for line in currentFile:
            checkMarr = re.search(r'Marriage' , line)
            if(checkMarr != None):
               wordlist = line.split()
               surname = wordlist[len(wordlist)-1]
               if(file  == "mary_roche.txt"):
                   tempName = "MARY ANNE " + surname
               else:
                   tempName = "NICHOLAS " + surname
            checkYear = re.search(r'Year' , line)
            if(checkYear != None):
                wordlist = line.split()
                tempYear = wordlist[len(wordlist)-1]
            checkGroupReg = re.search(r'Group' , line)
            if(checkGroupReg != None):
                wordlist = line.split()
                tempGroupReg = wordlist[len(wordlist)-1]
            checkDistrict = re.search(r'District' , line)
            if(checkDistrict != None):
                wordlist = line.split()
                tempDistrict = wordlist[len(wordlist)-1]
            checkQuarter = re.search(r'Quarter' , line)
            if(checkQuarter != None):
                wordlist = line.split()
                tempQuarter = wordlist[len(wordlist)-1]
            checkVolume = re.search(r'Volume' , line)
            if(checkVolume != None):
                wordlist = line.split()
                tempVolume = wordlist[len(wordlist)-1]
            checkPage = re.search(r'Page' , line)
            if(checkPage != None):
                wordlist = line.split()
                tempPageNo = wordlist[len(wordlist)-1]
                tempObj = Marriage(tempName , tempYear , tempGroupReg , tempDistrict , tempQuarter , tempVolume , tempPageNo)
                if(file  == "mary_roche.txt"):
                   maryDetailsList.append(tempObj)
                else:
                   nicholasDetailsList.append(tempObj)
count = 0
for maryOb in maryDetailsList:
    for nichOb in nicholasDetailsList:
        if (maryOb.get_Year() == nichOb.get_Year() and
            maryOb.get_GroupReg() == nichOb.get_GroupReg() and
            maryOb.get_District() == nichOb.get_District() and
            maryOb.get_Quarter() ==  nichOb.get_Quarter() and
            maryOb.get_VolumeNo() == nichOb.get_VolumeNo() and
            maryOb.get_PageNo() == nichOb.get_PageNo()):
            print("******************************")
            print("Possible match!")
            print(nichOb.get_Name() + " and " + maryOb.get_Name() + " in  " + maryOb.get_District() + " in  " + maryOb.get_Year() )
            print("Quarter = " + maryOb.get_Quarter() + " , Volume = " + maryOb.get_VolumeNo() + " , Page =  " + maryOb.get_PageNo() )
            print("******************************")
            print()
            
            count = count + 1
          
            
            
            
            
            
            
































