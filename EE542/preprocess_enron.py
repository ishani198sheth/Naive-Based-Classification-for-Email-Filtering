import sys
import glob

def create_vocab_dict(file_in):
	in_file_open=open(file_in,"r",encoding="latin1")
	vocab_dict={}
	id_word=0
	for word in in_file_open.readlines():
		word=word.strip('\n').lower()
		#if word not in vocab_dict.keys():
		vocab_dict[word]=id_word
		id_word=id_word+1
	return vocab_dict

def create_pre_prosessing(vocab_dict,path_enron):
	out_file_open = open('TrainingFile', "w+")	
	for label in ('ham','spam'):
		files=glob.glob(path_enron+'/enron*/'+label+'/*.txt') 
		dict_tot={}
		for file in files:
			out_file_open.write(label.upper())
			word_dict={}
			in_file_open=open(file,"r",encoding="latin1")
			for line in in_file_open.readlines():
				sentence=line.split(" ")
				#print(word)
				count=0
				for word in sentence:
					word=word.lower()
					if word not in word_dict:
						word_dict[word]=1
					else:
						word_dict[word]=word_dict[word]+1
			for word_key in word_dict.keys():		
				if word_key in vocab_dict:
					out_file_open.write(' '+str(vocab_dict[word_key])+':'+str(word_dict[word_key]))
					
			out_file_open.write('\n')	
	out_file_open.close()		

def create_test_prosessing(vocab_dict,path_test):
		out_file_open = open('TestFile', "w+")	
		files=glob.glob(path_test+'/*.txt') 
		dict_tot={}
		for file in files:
			word_dict={}
			in_file_open=open(file,"r",encoding="latin1")
			for line in in_file_open.readlines():
				sentence=line.split(" ")
				#print(word)
				count=0
				for word in sentence:
					word=word.lower()
					if word not in word_dict:
						word_dict[word]=1
					else:
						word_dict[word]=word_dict[word]+1
			for word_key in word_dict.keys():		
				if word_key in vocab_dict:
					out_file_open.write(str(vocab_dict[word_key])+':'+str(word_dict[word_key])+' ')
					
			out_file_open.write('\n')	
		out_file_open.close()

def main(args):
	vocab_dict=create_vocab_dict(args[2])
	if args[1]=='train':
		create_pre_prosessing(vocab_dict,args[3])
	if args[1]=='test':
		create_test_prosessing(vocab_dict,args[3])

if __name__ == '__main__':
	main(sys.argv)
