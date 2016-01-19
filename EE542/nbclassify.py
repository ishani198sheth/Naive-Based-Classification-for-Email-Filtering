import sys
import glob
import math
file_in=sys.argv[1]
def read_model_file(file_in):
	in_file_open=open(file_in,"r")
	vocab_count=0
	prior_dict={}
	individual_counts={}
	total_count={}
	for line in in_file_open.readlines():
		line=line.strip('\n')
		id_model=line.split( )[0]
		if id_model=='vocab_count':
			vocab_count=line.split( )[1]
		if id_model=='prior':
			prior_dict=dict(u.split(":") for u in line.split(" ")[1:])
		if id_model=='individual_wc':
			label=line.split( )[1]
			individual_counts[label]=dict(u.split(":") for u in line.split(" ")[2:])
		if id_model=='total_wc':
			total_count=dict(u.split(":") for u in line.split(" ")[1:])
	return vocab_count,prior_dict,individual_counts,total_count

vocab_count,prior_dict,individual_counts,total_count=read_model_file(file_in)

test_file=sys.argv[2]

def calc_naive_bayes(vocab_count,prior_dict,individual_counts,total_count,test_file):
	t_file=open(test_file,"r")
	for line in t_file.readlines():
		cond_prob={}
		line=line.strip('\n').strip(" ")
		feature_dict=dict(u.split(":") for u in line.split(" "))
		for label in individual_counts.keys():
			for k,v in feature_dict.items():
				if k not in individual_counts[label]:
					individual_counts[label][k]=0
				if label in cond_prob:
						smoothing_numerator=int(individual_counts[label][k])+1
						smoothing_denominator=int(vocab_count)+int(total_count[label])
						cond_prob[label]=cond_prob[label]+int(v)*(math.log(smoothing_numerator,10)-math.log(smoothing_denominator,10))
				else:
						smoothing_numerator=int(individual_counts[label][k])+1
						smoothing_denominator=int(total_count[label])+int(vocab_count)
						cond_prob[label]=int(v)*(math.log(smoothing_numerator,10)-math.log(smoothing_denominator,10))
				
			cond_prob[label]=cond_prob[label]+math.log(float(prior_dict[label]),10)
		label_test=max(cond_prob.keys(), key=(lambda k: cond_prob[k]))
		
		print(label_test)
	
calc_naive_bayes(vocab_count,prior_dict,individual_counts,total_count,test_file)
	
