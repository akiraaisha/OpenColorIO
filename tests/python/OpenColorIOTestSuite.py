import unittest, os, sys

build_location = sys.argv[1]
build_type = sys.argv[2]

opencolorio_dir = os.path.join(build_location, "src", "OpenColorIO")
pyopencolorio_dir = os.path.join(build_location, "src", "bindings", "python")
if os.name == 'nt':
    # On Windows we must append the build type to the build dirs and add the main library to PATH
    opencolorio_dir = os.path.join(opencolorio_dir, build_type)
    pyopencolorio_dir = os.path.join(pyopencolorio_dir, build_type)
    os.environ['PATH'] = "{0};{1}".format(opencolorio_dir, os.environ.get('PATH',""))
elif sys.platform == 'darwin':
    # On OSX we must add the main library location to DYLD_LIBRARY_PATH
    os.environ['DYLD_LIBRARY_PATH'] = "{0}:{1}".format(opencolorio_dir, os.environ.get('DYLD_LIBRARY_PATH', ""))

sys.path.insert(0, pyopencolorio_dir)
import PyOpenColorIO as OCIO

from MainTest import *
from ConstantsTest import *
from ConfigTest import *
from ContextTest import *
from LookTest import *
from ColorSpaceTest import *
from GpuShaderDescTest import *
from Baker import *
from TransformsTest import *
from RangeTransformTest import *

class FooTest(unittest.TestCase):
    
    def test_interface(self):
        pass

def suite():
    suite = unittest.TestSuite()
    suite.addTest(MainTest("test_interface"))
    suite.addTest(ConstantsTest("test_interface"))
    suite.addTest(ConfigTest("test_interface"))
    suite.addTest(ConfigTest("test_is_editable"))
    suite.addTest(ContextTest("test_interface"))
    suite.addTest(LookTest("test_interface"))
    suite.addTest(ColorSpaceTest("test_interface"))
    suite.addTest(RangeTransformTest("test_interface"))
    suite.addTest(RangeTransformTest("test_equality"))
    suite.addTest(RangeTransformTest("test_validation"))
    suite.addTest(TransformsTest("test_interface"))
    # Processor
    # ProcessorMetadata
    suite.addTest(GpuShaderDescTest("test_interface"))
    suite.addTest(BakerTest("test_interface"))
    # PackedImageDesc
    # PlanarImageDesc
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    test_suite = suite()
    result = runner.run(test_suite)
    if result.wasSuccessful() == False:
        sys.exit(1)
    sys.exit(0)

