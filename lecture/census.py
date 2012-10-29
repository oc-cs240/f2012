data = file('urpop0090.txt', 'r')
for line in data:
	line = line.strip()
	if '%' not in line:
		continue

	blacklist = ['Region', 'Division', 'Table', 'UNITED STATES', 'population']

	if 'Region' in line or 'Division' in line or 'UNITED STATES' in line:
		continue
	# states = ['Michigan', 'Florida']
	# for state in states:
	# 	if state in line:
	# 		print line
	# 		break

	print line
	print line[:27].strip()
	print line[27:38].strip()
	print line[86:96].strip()
	print line[144:154].strip()

"""
Maine                       1,227,928      547,824      680,104    44.6%   55.4% r    1,125,043      534,072      590,588    47.5%   52.5% r      993,722      504,157      487,891    50.8%   49.2%
"""