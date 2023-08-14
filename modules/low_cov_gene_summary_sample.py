import os

from modules.low_cov_sample_filter import low_cov_sample_filter
from modules.summarize_gene_data import summarize_gene_data

# prints in a .csv format to allow '>' saving in bash
def low_cov_gene_summary_sample(file, sample_id):
	if os.path.isfile(file):
		filename, file_extension = os.path.splitext(file)
		if file_extension == '.csv':
			res = summarize_gene_data(low_cov_sample_filter(file, sample_id))
			res = res.to_csv(index = False, sep='\t')
			print(res)
			return(res)
		else:
			raise RuntimeError(f"Not a *.csv file: {file}")
	else:
		raise FileNotFoundError(f"File not found, please check if it is the correct path: {file}")