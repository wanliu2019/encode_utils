#!/usr/bin/env python3                                                                                 
# -*- coding: utf-8 -*-                                                                                
                                                                                                       
###                                                                                                    
# © 2018 The Board of Trustees of the Leland Stanford Junior University                              
# Nathaniel Watson                                                                                      
# nathankw@stanford.edu                                                                                 
###

"""                                                                                                    
Tests functions in the utils module. A few test data files are used from within the 'data' folder.  
The contents of the files are explained here. When a test utilizes any of them, you can check here  
to read the documentation about the contents of that file.                                             
                                                                                                       
* replicates_for_ENCSR502NRF.json                                                                      
  Contains the value of the 'replicates' property for the actual experiment ENCSR502NRF.               
  There are two replicates:                                                                            
                                                                                                       
  * michael-snyder:L-3525-1_ENCSR502NRF with biological_replicate_number=1 and                         
    technical_replicate_number=1. It belongs to library accession ENCLB690UAL.                         
  * michael-snyder:L-3526-2_ENCSR502NRF with biological_replicate_number=2 and                         
    technical_replicate_number=1. It belongs to library accession ENCLB782CIR.                         
"""

import json
import os
import unittest

from encode_utils import utils

DATA_DIR = "data"

class TestUtils(unittest.TestCase):
  """Tests the utils.py module.
  """

  def test_add_to_set(self):
    """Tests the function utils.add_to_set() for success when all elements are already unique.
    """
    entries = [1,2,3]
    new = 4
    self.assertEqual(utils.add_to_set(entries=entries,new=new),[1,2,3,4])

  def test_add_to_set_2(self):
    """Tests the function utils.add_to_set() for success when there are duplicates.
    """
    entries = [1,2,3]
    new = 3
    self.assertEqual(utils.add_to_set(entries=entries,new=new),[1,2,3])

  def test_calculate_md5_sum(self):
    """Tests the function calculate_md5_sum() for success.
    """
    infile = os.path.join(DATA_DIR,"test_fq_40recs.fastq.gz")
    md5sum = utils.calculate_md5sum(infile) 
    self.assertEqual(md5sum,"dc991f01103594ef590d612e0caabf39")

  def test_clean_alias_name(self):
    """Tests the function clean_alias_name() for success.
    """
    alias = r"michael-snyder:a/troublesome\alias"
    self.assertEqual(utils.clean_alias_name(alias),"michael-snyder:a_troublesome_alias")

  def test_does_lib_replicate_exist(self):
    """
    Test the function utils.does_lib_replicate_exist() for 1 result when when only care about
    whether the library has any replicates, and not any particular one.
    """
    infile = os.path.join(DATA_DIR,"replicates_for_ENCSR502NRF.json")
    with open(infile,'r') as fh:
      replicates_json = json.loads(fh.read())
    lib_accession = "ENCLB690UAL"
    res = utils.does_lib_replicate_exist(replicates_json=replicates_json,
                                         lib_accession=lib_accession)
    self.assertEqual(res,["37b3dabc-bbdc-4832-88a5-78c2a8369942"])

  def test_2_does_lib_replicate_exist(self):
    """
    Test the function utils.does_lib_replicate_exist() for empty result when library accession
    doesn't belong to any of the replicates.
    """
    infile = os.path.join(DATA_DIR,"replicates_for_ENCSR502NRF.json")
    with open(infile,'r') as fh:
      replicates_json = json.loads(fh.read())
    lib_accession = "ENCLB000000" #Doesn't exist.
    res = utils.does_lib_replicate_exist(replicates_json=replicates_json,
                                         lib_accession=lib_accession)
    self.assertEqual(res,[])

  def test_3_does_lib_replicate_exist(self):
    """
    Test the function utils.does_lib_replicate_exist() for empty result when library accession
    doesn't belong to any of the replicates.
    """
    infile = os.path.join(DATA_DIR,"replicates_for_ENCSR502NRF.json")
    with open(infile,'r') as fh:
      replicates_json = json.loads(fh.read())
    lib_accession = "ENCLB000000" #Doesn't exist.
    res = utils.does_lib_replicate_exist(replicates_json=replicates_json,
                                         lib_accession=lib_accession)
    self.assertEqual(res,[])

  def test_strip_alias_prefix(self):
    """Tests the function strip_alias_prefix for success.
    """
    alias = "michael-snyder:B-167"
    self.assertEqual(utils.strip_alias_prefix(alias),"B-167")
  


if __name__ == "__main__":
  unittest.main()