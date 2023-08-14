import unittest
import pandas as pd
from pandas.util.testing import assert_frame_equal
from pathlib import Path
import os

import sys
sys.path.append('..')

from modules.low_cov_gene_summary_sample import low_cov_gene_summary_sample

THIS_DIR = Path(__file__).parent
my_data_path = THIS_DIR

class TestMainFunction(unittest.TestCase):
    
    def test_not_csv(self):
        self.assertRaises(RuntimeError, low_cov_gene_summary_sample, os.path.join(my_data_path,'low_coverage_summary.txt'), 'p1')

    def test_invalid_path(self):
        self.assertRaises(FileNotFoundError, low_cov_gene_summary_sample, os.path.join(my_data_path,'low_coverage_summary_fake.csv'), 'p1')

    def test_simple_correct_usage(self):
        expected_result = pd.DataFrame()
        gene = ["ASXL1", "CEBPA", "SH2B3", "TERT", "WT1"]
        min_cov = [95, 8, 20, 90, 144]
        total_lc = [61, 437, 170, 150, 46]
        expected_result.insert(0, "Gene", gene)
        expected_result.insert(1, "Minimum.Coverage", min_cov)
        expected_result.insert(2, "Total.Low.Coverage", total_lc)
        expected_result = expected_result.to_csv(index = False, sep='\t')

        example_usage = low_cov_gene_summary_sample(os.path.join(my_data_path,'low_coverage_summary_subsample.csv'), 'p1')

        self.assertEqual(example_usage, expected_result)

if __name__ == "__main__":
    unittest.main()