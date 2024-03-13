from modeller import *

env = Environ()
aln = Alignment(env)
mdl = Model(env, file='4nqa', model_segment=('FIRST:A','LAST:A'))
aln.append_model(mdl, align_codes='4nqa', atom_files='4nqa.pdb')
aln.append(file='Query.pir', align_codes='yd1')
aln.align2d(max_gap_length=50)
aln.write(file='Target-template.ali', alignment_format='PIR')
aln.write(file='Target-template.pap', alignment_format='PAP')