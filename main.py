import argparse

from modules.low_cov_gene_summary_sample import low_cov_gene_summary_sample

parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("input", help="Source location")
parser.add_argument("sampleID", help="Sample identifier")
args = parser.parse_args()

def main(file, sample_id):
	low_cov_gene_summary_sample(file, sample_id)

if __name__== "__main__":
    low_cov_gene_summary_sample(str(args.input), str(args.sampleID))