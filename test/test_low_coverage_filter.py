import unittest
import pandas as pd
from pandas.util.testing import assert_frame_equal
from pathlib import Path
import os

import sys
sys.path.append('..')

from modules.low_cov_sample_filter import low_cov_sample_filter

THIS_DIR = Path(__file__).parent
my_data_path = THIS_DIR

class TestLowCoverageFilter(unittest.TestCase):
    
    def test_no_matching_sample_id(self):
        self.assertRaises(ValueError, low_cov_sample_filter, os.path.join(my_data_path,'low_coverage_summary_subsample.csv'), 'p3')
        
    def test_dataFrame_correct(self):
        expected_result = pd.DataFrame()
        patient_id = ["p1"]
        expected_result.insert(0, "patient_id", patient_id)
        
        assert_frame_equal(low_cov_sample_filter(os.path.join(my_data_path,'test_filtering_pass_simple.csv'), 'p1'), expected_result)
        
    def test_no_patient_id_column(self):
        self.assertRaises(RuntimeError, low_cov_sample_filter, os.path.join(my_data_path,'test_filtering_patient_id_error.csv'), 'test')

if __name__ == "__main__":
    unittest.main()