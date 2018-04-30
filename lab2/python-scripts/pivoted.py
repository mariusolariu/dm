from subprocess import Popen, PIPE
from itertools import product

f_data = None
log_file = "aiciscuipamtat"
with open('config.toml', 'r') as f:
	f_data = f.read()

out = open('data.dat', 'w')
try:
	for mu in [.01*i for i in range(101)]:
		with open('config.toml', 'w') as f:
			f.write(f_data % mu)
		f = open(log_file, 'w')
		p=Popen("./competition config.toml", shell=True, stdout=f, stdin=PIPE)
		p.stdin.write("EU\n")
		p.stdin.flush()
		p.wait()
		f.close()

		with open(log_file, 'r') as f:
			res = float(f.readlines()[-1].split(": ")[1])
        		print(res)
			out.write('s=%f:\t%f\n' % (mu, res))
except:
	raise
finally:
	with open('config.toml', 'w') as f:
		f.write(f_data)

out.close()
