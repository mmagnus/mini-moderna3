#!/usr/bin/env python
#
# test_MODERNA_all.py
#
# runs complete set of unit tests for ModeRNA.
#
# http://iimcb.genesilico.pl/moderna/
#
__author__ = "Magdalena Rother, Tomasz Puton, Kristian Rother"
__copyright__ = "Copyright 2008, The Moderna Project"
__credits__ = ["Janusz Bujnicki"]
__license__ = "GPL"
__maintainer__ = "Magdalena Rother"
__email__ = "mmusiel@genesilico.pl"
__status__ = "Production"

from unittest import main, TestCase
import sys
from moderna.util.LogFile import log

# data infrastructure
from tests.test_rna_residue import RNAResidueTests
from tests.test_rna_chain import RNAChainTests
from tests.test_moderna_structure import ModernaStructureTests
from tests.test_check_pdb import CheckPdbTests
from tests.test_write_pdb import WritePDBTests
from tests.test_moderna_superimposer import SuperimposerTests


# RNA modeling
from tests.test_modeling_recipe import RecipeMakerTests
from tests.test_copy_residue import CopyResidueTests
from tests.test_moderna_fragment import ModernaFragmentTests, \
    ModernaFragment5Tests, ModernaFragment3Tests, ModernaFragment53Tests, AnchorResidueTests
from tests.test_secstruc_fragment import ModernaFragment2DTests, ModernaFragmentStrandTests
from tests.test_helix import HelixTests, HelixFragmentBuilderTests
from tests.test_renumerator import RenumeratorTests
from tests.test_fragment_insertion import FragmentInserterTests

# sub-packages
from tests.test_sequence import *
from tests.test_analyze import *
from tests.test_builder import *
from tests.test_isosteric import *
from tests.test_fragment_library import *
from tests.test_modifications import *

from tests.test_rnamodel import BasicRnaModelTests, RetainTemplateTests, IndelQualityTests

# toplevel functions
from tests.test_commands import CommandTests
from tests.test_util import ValidatorTests, StrucValidatorTests
from tests.test_commandline import CommandlineTests

if __name__ == '__main__':
    log.write_to_stderr = False
    log.raise_exceptions = True
    log.redirect_stdout()
    main()
