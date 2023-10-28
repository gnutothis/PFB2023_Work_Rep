#!/usr/bin/env python3

import sys

rand = sys.argv[1] #expect ss_rand5-200_v_qfo_

score_matrices = ['BL50', 'BP62', 'VT10', 'VT160', 'VT20', 'VT40', 'VT80']

field_names = ['qseqid', 'sseqid', 'percid', 'alen', 'mismat', 'gaps', 'q_start', 'q_end', 's_start', 's_end','evalue', 'bits']

this_data = {}

for sm in score_matrices:
    with open(f'{rand}{sm}.txt', 'r') as data:
        x = 0
        for line in data:
            if x < 1:
                if '#' not in line:
                    line = line.rstrip()
                    this_data[sm] = dict(zip(field_names, line.split('\t')))
                    x += 1
            else:
                break
B5 = this_data['BL50']
B6 = this_data['BP62']
V1 = this_data['VT10']
V6 = this_data['VT160']
V2 = this_data['VT20']
V4 = this_data['VT40']
V8 = this_data['VT80']
print(f'''
mat\tid\talen\teval
BL50\t{B5['percid']}\t{B5['alen']}\t{B5['evalue']}
BP62\t{B6['percid']}\t{B6['alen']}\t{B6['evalue']}
VT10\t{V1['percid']}\t{V1['alen']}\t{V1['evalue']}
VT160\t{V6['percid']}\t{V6['alen']}\t{V6['evalue']}
VT20\t{V2['percid']}\t{V2['alen']}\t{V2['evalue']}
VT40\t{V4['percid']}\t{V4['alen']}\t{V4['evalue']}
VT80\t{V8['percid']}\t{V8['alen']}\t{V8['evalue']}''')

print(this_data)
