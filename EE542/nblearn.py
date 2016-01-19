import sys
import glob
def create_label_dict(file_in):
	in_file_open=open(file_in,"r")
	label_prior_dict={}
	total=0.0
	for line in in_file_open.readlines():
		line=line.strip('\n')
		label=line.split( )[0]
		if label in label_prior_dict:
			label_prior_dict[label]=label_prior_dict[label]+1
			total=total+1
		else:
			label_prior_dict[label]=1
			total=total+1
	for key,value in label_prior_dict.items():
		label_prior_dict[key]=round((value/total),5)
	return label_prior_dict

def calculate_word_count(file_in,model_fl):
	in_file_open=open(file_in,"r")
	d={}
	for line in in_file_open.readlines():
		line=line.strip('\n')
		line=line.strip(' ')
		label=line.split(" ")[0]
		data=dict(u.split(":") for u in line.split(" ")[1:])
		if label in d:
			for k,v in data.items():
				if k in d[label]:
					d[label][k]=int(d[label][k])+int(v)
				else:
					d[label][k]=int(v)
		else:
			d[label]=data
	return d


def calc_label_count(total_label_wc):
	label_count={}
	vocab_count={}
	for k,v in total_label_wc.items():
		
		sum_label=0
		for k1,v1 in v.items():
			vocab_count[k1]=1
			sum_label=sum_label+int(v1)
		label_count[k]=sum_label
	count=len(vocab_count)
	return label_count,count
			

def main(args):

	label_prior_dict=create_label_dict(args[1])
	word_count_dict=calculate_word_count(args[1],args[2])
	label_count,vocab_count=calc_label_count(word_count_dict)
	model_file_open = open(args[2], "w+")
	model_file_open.write('vocab_count '+str(vocab_count))
	model_file_open.write('\nprior '+str(label_prior_dict).replace("'",'').replace(' ','').replace(',',' ').strip('{').strip('}'))
	for k,v in word_count_dict.items():
		model_file_open.write('\nindividual_wc '+str(k)+' '+str(v).replace("'",'').replace(' ','').replace(',',' ').strip('{').strip('}'))
	model_file_open.write('\ntotal_wc '+str(label_count).replace("'",'').replace(' ','').replace(',',' ').strip('{').strip('}'))
	model_file_open.close()

if __name__ == '__main__':
	main(sys.argv)
