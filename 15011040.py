dna = input('enter DNA sequence:')
arr = list(dna)
i=0
for j in arr:
    if j=='T':
        arr[i]='A'
        i=i+1
        
    if j=='C':
        arr[i]='G'
        i=i+1
        
    if j=='A':
        arr[i]='T'
        i=i+1
        
    if j=='G':
        arr[i]='C'
        i=i+1

for j in range(0, len(dna)):
    if arr[j]=='T':
        arr[j]='U'


dna = ''.join(map(str, arr))

table = {
        'AUA':'I', 'AUC':'I', 'AUU':'I', 'AUG':'M',
        'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACU':'T',
        'AAC':'N', 'AAU':'N', 'AAA':'K', 'AAG':'K',
        'AGC':'S', 'AGU':'S', 'AGA':'R', 'AGG':'R',                 
        'CUA':'L', 'CUC':'L', 'CUG':'L', 'CUU':'L',
        'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCU':'P',
        'CAC':'H', 'CAU':'H', 'CAA':'Q', 'CAG':'Q',
        'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGU':'R',
        'GUA':'V', 'GUC':'V', 'GUG':'V', 'GUU':'V',
        'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCU':'A',
        'GAC':'D', 'GAU':'D', 'GAA':'E', 'GAG':'E',
        'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGU':'G',
        'UCA':'S', 'UCC':'S', 'UCG':'S', 'UCU':'S',
        'UUC':'F', 'UUU':'F', 'UUA':'L', 'UUG':'L',
        'UAC':'Y', 'UAU':'Y', 'UAA':'_', 'UAG':'_',
        'UGC':'C', 'UGU':'C', 'UGA':'_', 'UGG':'W',
    }

aminoacid =""

if len(dna)%3 == 0:
    for i in range(0, len(dna), 3):
        codon = dna[i:i + 3]
        aminoacid+= table[codon]

print('amino acid sequence:',aminoacid)
