import random

nucloes='AGTC'
#dna generator
def dnagenerate(limit):  
    d=str()
    for x in range(limit):
        dd=random.choice(nucloes)
        d=d+dd
    return d


Dnaseq=dnagenerate(12)
print("Generated origianl Seq: ",Dnaseq)


#Mutating dna
def dnaMutator(): 
    mutatDna=Dnaseq   
    char_list=list(mutatDna)
    for i in range(1):#number of mutation=1
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
def aa_convertion(seq):
    table = { 
        'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M', 
        'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T', 
        'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K', 
        'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
        'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
        'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
        'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q', 
        'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R', 
        'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V', 
        'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A', 
        'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E', 
        'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G', 
        'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S', 
        'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L', 
        'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_', 
        'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W', 
    } 
    protien=''
    for x in range(0,len(seq),3):
        codon=seq[x:x+3]
        protien+=table[codon]
    print("Protien Sequence of mRNA:\t",protien)

aa_convertion(Dnaseq)

#gc content
def gc_content(seq):
    count=0
    for x in seq:
        if x=='G'or x=='C':
            count+=1
    print("GC Content is:\t",(count/len(seq))*100,'%')


whichtogc=input("which DNA to check for gc content 1(original) or else: ")
if(whichtogc==1):
    gc_content(Dnaseq)
else:
    gc_content(mutatedDnaseq)

#freq score cal
