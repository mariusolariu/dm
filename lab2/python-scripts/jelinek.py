from subprocess import Popen, PIPE

line_oi = 28
string_oi = 'lambda=%f'
log_file = 'aiciscuipamtat'

f_data = None
with open('config.toml', 'r') as f:
	f_data = f.read().split('\n')

out = open('data.dat', 'w')
v=0.
step = 0.01
values = []
while v <= 1.0000001:
	values.append(v)
	v += step

for l in values:
	with open('config.toml', 'w') as f:
		f_data[line_oi] = string_oi % l
		f.write('\n'.join(f_data))
	f = open(log_file, 'w')
	p=Popen("./competition config.toml", shell=True, stdout=f, stdin=PIPE)
	p.stdin.write("EU\n")
	p.stdin.flush()
	p.wait()

	with open(log_file, 'r') as f:
		out.write('%f:\t%f\n' % (l, float(f.readlines()[-1].split(": ")[1])))

	f.close()

out.close()
