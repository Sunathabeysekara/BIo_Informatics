import random

nucloes='AGTC'
#dna generator
def dnagenerate(limit):  
    d=str()
    for x in range(limit):
        dd=random.choice(nucloes)
        d=d+dd
    return d

Dnaseq=dnagenerate(10)
print("Generated origianl Seq: ",Dnaseq)


#Mutating dna
def dnaMutator(): 
    mutatDna=Dnaseq   
    char_list=list(mutatDna)
    for i in range(2):
        #random index generated for mutation indexus
        index=random.randrange(len(Dnaseq))
        #dna mutation
        originnuc=mutatDna[index]
        #print('original nucleo that gonna mutate: ',originnuc)
        mutatednuc=random.choice(nucloes)
        while (originnuc==mutatednuc):
            mutatednuc=random.choice(nucloes)
        #print('gonna mutate to : ',mutatednuc)
        #mutatDna[index]=mutatednuc use list method
        char_list[index]=mutatednuc
    return ''.join(char_list)
mutatedDnaseq=dnaMutator()
print("Mutated Dna Seq: \t",mutatedDnaseq)

#transcription
dna2rna={'A':'U','T':'A','G':'C','C':'G'}
whichtotranscript=input("which DNA to convet to RNA 1(original) or else: ")
inputdata=2
if(whichtotranscript==1):
    inutdata=Dnaseq
else:
    inputdata=mutatedDnaseq
def dnatranscription(inputdata):
    transcripteddna=str()
    for x in inputdata:
        transcripteddna+=dna2rna[x]
    return transcripteddna
transcripteddna=dnatranscription(Dnaseq)
print("Transcripted Dna Seq (mRNA): ",transcripteddna)


#rna to amino acid
