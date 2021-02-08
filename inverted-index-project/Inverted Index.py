import sys
class Inverted_Index:
    # intializing dictionary 
    def __init__(self):
        self.document_dic={}
        self.count=0
    # setting value by name of doc
    def Add_Document(self,name):
        self.document_dic[self.count]=name+'.txt'
        self.count+=1
    # intializing file reading and inserting words in it.
    def Records_level(self):

        Termss=self.Rf()
        Termss=Termss[0]
        w=[]
        c=[]

        for x,y in self.document_dic.items():
            #reading file and spliting with respect to each word and assigning to 'a'
            infile=open(y,'r')
            a=infile.read()
            a=a.split()
            infile.close()
            #check len and slicing them in loop and appending them in j
            for j in a:
                if len(j)>2 and (j[-2]=="'" or j[-2]==":" or j[-2]==";"):
                    w.append((j[-1*len(a):-2]).lower())
                    # replcing "." to " "
                elif '.' in j:
                    w.append((j.replace('.','')).lower())
                elif len(j)>2:
                    w.append(j.lower())
            for i in w:
                if i in Termss:
                    c.append((i,y))
                w=[]
        return c
        print(c)
    #checking word levels
    def Words_Level(self):
        File=[]
        PS=[]
        l=[]
        for x,y in self.document_dic.items():
            File.append(y)
        #reading file and spliting with respect to each word and assigning to 'b'
        for i in File:
            z=0
            infile=open(i,'r')
            b=infile.read()
            b=b.split()
            infile.close()
            #check len and slicing them in loop and appending them in j
            for j in b:
                if (len(j)>2) and  b.index(j) not in PS:
                    PS.append(b.index(j))
                else:
                    b[b.index(j)]=''
                if (len(j)>2) and  b.index(j) not in PS:
                    PS.append(b.index(j))
            l.append(PS)
            # Removing previously added values so i next itration or call we dont get previous added values 
            PS=[]
        return l
    #appending dict values in file list
    def Rf(self):
        Filess=[]
        Termss=[]
        stp=[]
        for x,y in self.document_dic.items():
            Filess.append(y)
            #reading file and spliting with respect to each word and assigning to 'a'
        for i in Filess:
            infile=open(i,'r')
            a=infile.read()
            a=a.split()
            infile.close()
            #check len and slicing them in loop and appending them in j
            for j in a:
                if len(j)>2 and (j[-2]=="'" or j[-2]==":" or j[-2]==";"):
                    Termss.append((j[-1*len(a):-2]).lower())
                elif '.' in j:
                    Termss.append((j.replace('.','')).lower())
                elif len(j)>2:
                    Termss.append(j.lower())
                elif len(j)<=3 and j not in stp:
                    stp.append(j.lower())
        Termss,stp.sort()
        return Termss,stp
# class main for calling functions
class test:
    
    def __init__(self):
        self.i=Inverted_Index()
    def run(self):
        while True:
            print('''
            --------------INVERTED INDEX--------------------
            1.ADD DOCUMENT *Note add all docs before testing
            2.Words Collected From your Document
            3.Stop word in the file
            4.Record Level
            5.Word level inverted index
            6.Press 6 to Exit
            ''')
            CHoicE=int(input('Enter the Choice Here------>'))
            if CHoicE==1:
                a=input('Enter Your Document Name Here----->')
                self.i.Add_Document(a)
            if CHoicE==2:
                a=(self.i.Rf())
                print(a[0])
            if CHoicE==3:
                a=self.i.Rf()
                print(a[1])
            if CHoicE==4:
                a=(self.i.Records_level())
                d=list(dict.fromkeys(a))
                d.sort()
                for x in d:
                    print(x[1],x[0])
            if CHoicE==5:
                #a=(self.i.Rf())
                j=(self.i.Records_level())
                k=(self.i.Words_Level())
                c=0
                while c!=len(k):
                    for i in range(len(k[c])):
                        print(j[i],k[c][i], sep = ':', end = '\t')
                    c+=1
            if CHoicE==6:
                sys.exit()
aa=test()
aa.run()
