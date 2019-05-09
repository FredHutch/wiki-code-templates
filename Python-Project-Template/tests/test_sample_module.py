"""
This is an example of a unit test class to test a python module saved in the
template source code directory. 

It is possible to have this test module automatically executed at each git push,
via Travis continuous integration tools. For manual execution, import this test
module into a jupyter notebook, or enter the following into the command line:

python -m unittest tests/test_something.py

For more information about unit tests in python, see the documentation:

https://docs.python.org/3/library/unittest.html

Full documentation should include information about the module you are testing, 
as well as the types of tests executed. When starting from this file to build 
your own test class, make sure to update module and path names below. This sample
is provided assuming that sample_module.py is a module in the source code folder 
(../project_name/) of this template, containing a python function called 
sample_function, that takes exactly one argument. 

While only one test  function is shown below, many tests are possible to confirm 
that your functions are providing expected output under different circumstances. 
Generally, you may want to think about boundary testing and sanity checks for 
computational tasks, as well as exception handling and size checking for data
processing tasks. For more resources and ideas on testing practices, Software
Carpentry provides an excellent resource: 

https://v4.software-carpentry.org/test/index.html
"""
import sys
import unittest
sys.path.append('project_name/')
from sample_module import sample_function

class TestSampleModule(unittest.TestCase):
    """
    Using the unit test framework, this class tests each of the imported
    functions (sample_function) from the sample_module.py module.
    """
    def test_sample_function_args(self):
        """
        This function tests whether the correct ValueError exception is raised 
        when an invalid parameter is provided.
        Args:
        Returns:
            True (bool) if the correct exception is raised.
        """
        self.assertRaises(ValueError, sample_function, "bad input value")

if __name__ == '__main__':
    unittest.main()
