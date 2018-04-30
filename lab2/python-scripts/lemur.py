from subprocess import Popen, PIPE
import os
import random

if __name__ == '__main__':

	log_file = 'aiciscuipamtat'
	random.seed(42)
	out = open('data.dat', 'w')
	try:
		with open('../data/l.bak', 'w') as fw:
			with open('../data/lemur_plus.bak', 'r') as fr:
				data = fr.read()
				fw.write(data)
				data = {w for w in data.split('\n')}
	
		for i in range(10):
			with open('../data/lemur-stopwords.txt', 'w') as f:			
				f.write('\n'.join(sorted(random.sample(data, 300))))

			f = open(log_file, 'w')
			p=Popen("./competition config.toml", shell=True, stdout=f, stdin=PIPE)
			p.stdin.write("EU\n")
			p.stdin.flush()
			p.wait()
			f.close()

			with open(log_file, 'r') as f:
				res = float(f.readlines()[-1].split(": ")[1])
				out.write('%f\n' % res)
			os.rename('../data/lemur-stopwords.txt', '../data/lemur_%d' % i)
	except:
		raise
	finally:
		with open('../data/lemur-stopwords.txt', 'w') as fw:
			with open('../data/l.bak', 'r') as fr:
				fw.write(fr.read())

	out.close()	
