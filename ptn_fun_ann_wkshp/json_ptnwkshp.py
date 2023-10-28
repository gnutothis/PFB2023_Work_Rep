#!/usr/bin/env python3

import json
import sys
from pprint import pprint
from Bio import SeqIO

fastafile = sys.argv[1]
jsonfile = sys.argv[2]

seqs = {}

for seq_record in SeqIO.parse(fastafile, "fasta"):
    fasta_seq = str(seq_record.seq)
    fasta_seq = fasta_seq.replace('*', '')
    seqs[fasta_seq] = {}
    seqs[fasta_seq]['id'] = seq_record.id
    seqs[fasta_seq]['desc'] = seq_record.description

#print(seqs)

with open(jsonfile, 'r') as myfile:
    data = myfile.read()

panther2go = {}
intrepro2go = {}
pfam = {}

iprscan = json.loads(data)


for result in iprscan['results']:
    sequence = result['sequence']
    if sequence == 'SEQUENCEUNAVAILABLE':
        continue
    seqid = seqs[sequence]['id']
    seqdesc = seqs[sequence]['desc']
    print(f'{seqid}\t{seqdesc} "\n")
   
    for match in result['matches']:
        if 'accession' in match:
            accession = match['accession']

            if accession.startswith('PTHR'):
                name = match['name']
                print(f"PNTHR: {accession} {name}")

                for goXRef in match['goXRefs']:
                    go_id = goXRef['id']
                    go_name = goXRef['name']
                    goinfo = f"{go_id} {go_name}"
                    print(f"\t{goinfo}")

                    if goinfo not in panther2go:
                        panther2go[goinfo] = 0
                    panther2go[goinfo] += 1

        signature_accession = match['signature']['accession']

        if signature_accession.startswith('PF'):
            name = match['signature']['name']
            desc = match['signature']['description']
            pfaminfo = f'{signature_accession} {name} {desc}'
   
            if pfaminfo not in pfam:
                pfam[pfaminfo] = 0
            pfam[pfaminfo] += 1

print('\n')
print('Summary Cumulative Counts')
print('==== GO TERM Counts ===')

for info,count in sorted(panther2go.items(), key = lambda x : x[1], reverse = True):
    if count > 1 :
        print(info,count)

print("\n")
print("==== PFAM Counts ===")
for info,count in sorted(pfam.items(), key=lambda x:x[1], reverse=True):
    if count > 1:
        print(info,count)
