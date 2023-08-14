import unittest
import pandas as pd
from pandas.util.testing import assert_frame_equal
from pathlib import Path
import os

import sys
sys.path.append('..')

from modules.summarize_gene_data import summarize_gene_data
from modules.low_cov_sample_filter import low_cov_sample_filter

THIS_DIR = Path(__file__).parent
my_data_path = THIS_DIR

class TestSummarizeGeneData(unittest.TestCase):
    def test_no_gene_column(self):
        no_gene_df = pd.read_csv(os.path.join(my_data_path,'test_filtering_pass_simple.csv'))
        self.assertRaises(RuntimeError, summarize_gene_data, no_gene_df)

    def test_no_minimum_depth_column(self):
        no_min_depth_df = pd.read_csv(os.path.join(my_data_path,'test_summarize_gene_no_min_depth.csv'))
        self.assertRaises(RuntimeError, summarize_gene_data, no_min_depth_df)

    def test_decimal_in_minimum_depth(self):
        min_depth_decimal_df = pd.read_csv(os.path.join(my_data_path,'test_summarize_gene_invalid_decimal_min_depth.csv'))
        self.assertRaises(TypeError, summarize_gene_data, min_depth_decimal_df)

    def test_string_in_minimum_depth(self):
        min_depth_string_df = pd.read_csv(os.path.join(my_data_path,'test_summarize_gene_invalid_string_min_depth.csv'))
        self.assertRaises(TypeError, summarize_gene_data, min_depth_string_df)

    def test_no_num_sites_column(self):
        no_num_sites_df = pd.read_csv(os.path.join(my_data_path,'test_summarize_gene_no_num_sites.csv'))
        self.assertRaises(RuntimeError, summarize_gene_data, no_num_sites_df)

    def test_decimal_in_num_sites(self):
        num_sites_decimal_df = pd.read_csv(os.path.join(my_data_path,'test_summarize_gene_invalid_decimal_num_sites.csv'))
        self.assertRaises(TypeError, summarize_gene_data, num_sites_decimal_df)

    def test_string_in_num_sites(self):
        num_sites_string_df = pd.read_csv(os.path.join(my_data_path,'test_summarize_gene_invalid_string_num_sites.csv'))
        self.assertRaises(TypeError, summarize_gene_data, num_sites_string_df)

    def test_simple_correct_usage(self):
        expected_result = pd.DataFrame()
        gene = ["ASXL1", "CEBPA", "SH2B3", "TERT", "WT1"]
        min_cov = [95, 8, 20, 90, 144]
        total_lc = [61, 437, 170, 150, 46]
        expected_result.insert(0, "Gene", gene)
        expected_result.insert(1, "Minimum.Coverage", min_cov)
        expected_result.insert(2, "Total.Low.Coverage", total_lc)

        example_usage = summarize_gene_data(low_cov_sample_filter(os.path.join(my_data_path,'low_coverage_summary_subsample.csv'), 'p1'))

        assert_frame_equal(example_usage, expected_result)

if __name__ == "__main__":
    unittest.main()