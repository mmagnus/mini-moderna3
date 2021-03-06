#!/usr/bin/env python
#
# test_pdb_converter.py
#
# unit tests for alignment
#
# http://iimcb.genesilico.pl/moderna/
#
__author__ = "Magdalena Rother, Tomasz Puton, Kristian Rother"
__copyright__ = "Copyright 2008, The Moderna Project"
__credits__ = ["Janusz Bujnicki"]
__license__ = "GPL"
__version__ = "1.5.0"
__maintainer__ = "Magdalena Rother"
__email__ = "mmusiel@genesilico.pl"
__status__ = "Production"

from unittest import main, TestCase
from moderna.PdbConverter import *
from moderna import load_model
from .test_data import *
import os

OUT_NAME = 'out.fasta'


class PdbConverterTests(TestCase):
    """
    """ 
    def test_change_ribose(self):
        """Test conversion of ribose nomenclature ' <---> *"""
        convert(input_file=PDB_STRANGE,  output_file='converter_out.pdb',  ribose="*")
        ms = load_model('converter_out.pdb','B')
        for resi in ms:
            self.assertFalse(resi.has_id("C4'"))
            self.assertTrue(resi.has_id('C4*'))
        convert(input_file=PDB_STRANGE,  output_file='converter_out.pdb',  ribose="'")
        ms = load_model('converter_out.pdb','B')
        for resi in ms:
            self.assertTrue(resi.has_id("C4'"))
            self.assertFalse(resi.has_id('C4*'))


    def test_change_phosphate(self):
        """Tests conversion OP1 <---> O1P"""
        convert(input_file=PDB_STRANGE,  output_file='converter_out.pdb',  phosphate="OP1")
        ms = load_model('converter_out.pdb','B')
        for resi in ms:
            self.assertFalse(resi.has_id("O1P"))
            self.assertTrue(resi.has_id('OP1'))
        convert(input_file=PDB_STRANGE,  output_file='converter_out.pdb',  phosphate="O1P")
        ms = load_model('converter_out.pdb','B')
        for resi in ms:
            self.assertTrue(resi.has_id("O1P"))
            self.assertFalse(resi.has_id('OP1'))

if __name__ == '__main__':
    main()
  

