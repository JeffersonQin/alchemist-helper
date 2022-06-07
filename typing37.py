import os
import re
import sys

patterns = [
	r'-> Tuple(\[).*?(\])',
	r'-> list(\[).*?(\])',
	r'-> set(\[).*?(\])',
	r'-> dict(\[).*?(\])',
	r'-> tuple(\[).*?(\])',
	r': Tuple(\[).*?(\])',
	r': list(\[).*?(\])',
	r': set(\[).*?(\])',
	r': dict(\[).*?(\])',
	r': tuple(\[).*?(\])',
	r'->Tuple(\[).*?(\])',
	r'->list(\[).*?(\])',
	r'->set(\[).*?(\])',
	r'->dict(\[).*?(\])',
	r'->tuple(\[).*?(\])',
	r':Tuple(\[).*?(\])',
	r':list(\[).*?(\])',
	r':set(\[).*?(\])',
	r':dict(\[).*?(\])',
	r':tuple(\[).*?(\])',
]

if __name__ == '__main__':
	args = sys.argv
	if len(args) != 2:
		print('Usage: {} <path>'.format(args[0]))
		sys.exit(1)
	target_path = args[1]
	for path, _, file_list in os.walk(target_path):
		for file_name in file_list:
			if file_name.endswith('.py'):
				file_path = os.path.join(path, file_name)
				with open(file_path, 'r') as f:
					data = f.read()
					for pattern in patterns:
						data = re.sub(pattern, '', data)
				with open(file_path, 'w') as f:
					f.write(data)
