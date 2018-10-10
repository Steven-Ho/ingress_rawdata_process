from upc_map import upc_processor
import argparse

def parse_args():
	parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)

	parser.add_argument('--data-path', type=str, default='../Downloads/IngressData/')

	args = parser.parse_args()

	dict_args = vars(args)
	return dict_args

if __name__ == '__main__':
	args = parse_args()
	upc_processor(**args)