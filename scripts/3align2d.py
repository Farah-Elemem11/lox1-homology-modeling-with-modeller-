from modeller import *

env = Environ()
aln = Alignment(env)
mdl = Model(env, file='7W5DA', model_segment=('FIRST:A','LAST:A'))
aln.append_model(mdl, align_codes='7W5DA', atom_files='7W5DA.pdb')
aln.append(file='lox1.ali', align_codes='lox1')
aln.align2d(max_gap_length=50)
aln.write(file='lox1-7W5DA.ali', alignment_format='PIR')
aln.write(file='lox1-7W5DA.pap', alignment_format='PAP')
