from subprocess import Popen, PIPE
from itertools import chain, combinations

def powerset(iterable):
	s = list(iterable)
	return chain.from_iterable(combinations(s, r) for r in range(1, len(s)+1))

def filters():
	for s in ["english-normalizer"]:
		yield ', {type = "%s"}' % s

def tokenizers():
	yield '"default-unigram-chain"\n'
	for tokenizer in ["icu-tokenizer", "character-tokenizer", "whitespace-tokenizer"]:
		for f in filters():
			yield '[{type = "%s"}%s]\n\n' % (tokenizer, f)	

def gen_data():
	r=""
	s0 = '[[analyzers]]\nmethod = "ngram-word"\nngram = %d\nfilter = '
	for i in range(2):
		s = s0 % (i+1)
		for t in tokenizers():
			yield s + t

if __name__ == '__main__':

	log_file = 'aiciscuipamtat'

	f_data = None
	with open('config.toml', 'r') as f:
		f_data = f.read()

	out = open('data.dat', 'w')
	try:
		for l in powerset(gen_data()):
			print(l)
			l=''.join(l)
			print(l)
                        with open('config.toml', 'w') as f:
                                f.write(f_data % l)

			f = open(log_file, 'w')
			p=Popen("./competition config.toml", shell=True, stdout=f, stdin=PIPE)
			p.stdin.write("EU\n")
			p.stdin.flush()
			p.wait()
			f.close()

			with open(log_file, 'r') as f:
				res = float(f.readlines()[-1].split(": ")[1])
        			print(res)
				out.write('%s\n<<%f>>\n\n' % (l, res))
	except:
		raise
	finally:
		with open('config.toml', 'w') as f:
			f.write(f_data)

	out.close()	
