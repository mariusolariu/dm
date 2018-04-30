from subprocess import Popen, PIPE
from itertools import product

line_oi = 28
string_oi = 'k1=%f\nb=%f\nk3=%f'
log_file = 'aiciscuipamtat'

f_data = None
with open('config.toml', 'r') as f:
	f_data = f.read()

out = open('data.dat', 'w')
v=1.2
step = 0.1
k1 = []
while v <= 2.0000001:
	k1.append(v)
	v += step

v=0.
step = 0.1
b = []
while v <= 1.00001:
	b.append(v)
	v += step

k3 = [i for i in range(100, 1000, 100)]
try:
	for l in product(k1, b, k3):
		with open('config.toml', 'w') as f:
			f.write(f_data % l)
		f = open(log_file, 'w')
		p=Popen("./competition config.toml", shell=True, stdout=f, stdin=PIPE)
		p.stdin.write("EU\n")
		p.stdin.flush()
		p.wait()
		f.close()

		k1, b, k3 = l
		with open(log_file, 'r') as f:
			res = float(f.readlines()[-1].split(": ")[1])
        		print(res)
			out.write('k1=%f, b=%f, k3=%d:\t%f\n' % (k1, b, k3, res))
except:
	raise
finally:
	with open('config.toml', 'w') as f:
		f.write(f_data)

out.close()
