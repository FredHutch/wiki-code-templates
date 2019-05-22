# Tool Development Template Usage

This template is built to accommodate any Python project focused on tool or package development, which can ultimately be shared or imported by other users. This file structure has the flexibility to support a notebook interface, an automated script, package creation, or some hybrid thereof. Some projects will require building out additional subfolders and modules, but the basic skeleton should be consistent across all projects at Fred Hutch. This will aid in reproducibility, and make it easier for other researches to review and adapt code to their own purposes. To browse the library of examples originating from this template (or submit your own code to be shared), see our linked [Tool Development Coding Examples Repository](https://github.com/FredHutch/wiki-code-examples/tool-development).

### Jupyter Notebook Interface

You may want to use a notebook to interact with an underlying module that you develop. In this case, you can find a template `ProjectName.ipynb` file within the `results` folder of this template directory. By saving your final notebooks in this location, anyone following up on your code can readily and unambiguously access the conclusions of your work. If you choose not to develop an interactive notebook, this file can be deleted without affecting the remainder of the template.

Here is an example of a project with a notebook interface, developed from this template. This example meets the coding standards at Fred Hutch: [TODO: Notebook Interface to Modules](https://github.com/FredHutch/wiki-code-examples)

Jupyter notebooks allow the flexibility to add interactive features, as well as mark-down text for documentation clarity. A well-documented notebook should include contextual information in markdown cells, and docstrings for all functions. Any additional modules must also be documented appropriately. Continue reading below for more information on building additional source code.

### Scripting and Package Creation

Sometimes you will want to contain an entire project in source code files. You can then either create a package that can be imported and run on other machines, or set up your code to execute on the command line or run automatically with a batch script. The minimal structure for any of these cases is included in the template, although you may want to build several distinct modules within the source code (`project_name/`) folder. Note that source code folder must contain an `__init__.py` file, and module names should be all lowercase with no hyphens (underscores are recommended).

Note that for a simple batch processing of a single `.py` file, it may be more appropriate to use the [DataAnalysis-Python-Template](../DataAnalysis-Python-Template/). Please read the documentation and determine the better requirements based on the usage and scope of your project.

We've included resources below for each of these use cases, as well as our own examples built from this template.

#### Creating a Package

To create a portable Python package from your project, you'll want to update the `setup.py` file in the root directory. An example of some setup options are provided in the file. At a minimum, you should set the appropriate values for these options. If you'd like to explore further, [this web resource](https://python-packaging.readthedocs.io/en/latest/index.html) contains some additional information on setup options and package creation.

#### Command Line and Batch

To run a Python module on the command line, you simply need to run Python with the path to the module you wish to run. All source code should be saved in the `project_name/` directory.

For example, using a python 3 environment from the project root directory in rhino, we can run the contents of a file `module_name.py` in the source code folder:
```
username@rhino2:~/ToolDev-Python-Template$ ml Python
username@rhino2:~/ToolDev-Python-Template$ python project_name/module_name.py
```
Batching is simply automating what you would do on the command line. In general, the automation steps go in a `.bat` file. For computing at Fred Hutch, we refer to the description and instructions available on the [Scientific Computing Wiki](https://sciwiki.fredhutch.org/scicomputing/compute_jobs/).

# File Structure

The minimum file structure is diagrammed below, followed by further discussion of the usage of each directory.
```
ToolDev-Python-Template/
  |- README.md
  |- LICENSE
  |- setup.py
  |- data/
      |- raw_data/
      |- processed_data/
  |- doc/
      |- doc_instructions.md
  |- project_name/
      |-  __init__.py
  |- results/
      |- ProjectName.ipynb
  |- tests/
      |- __init__.py
      |- test_sample_module.py
```

#### README

Every project should have a README file, that describes the contents of the project directory and the intended use of the code. This document can be plain text, although markdown is convenient for sharing links and formatting. The [Scientific Computing Wiki](https://sciwiki.fredhutch.org/compdemos/vscode_markdown_howto/) contains several resources for markdown tips as well as the VS Code editor.

This template README should be overwritten with details relevant to your project. 

#### License

All shared code and analysis needs to be released under a license. The default template license is the MIT license, as it comes with very limited restrictions and is considered a good choice for open research and code sharing. For more information on the MIT license, see the [full text](https://opensource.org/licenses/MIT). 

To set a different license for your project, you will need to delete the MIT license and [replace it](https://help.github.com/en/articles/adding-a-license-to-a-repository) before releasing your code. You should also make sure to update the license option in the `setup.py` file to remove any potential ambiguity.

#### Setup.py

The `setup.py` file is required for creating a package from your code. The current contents are sufficient to run, as long as you update the values of the options. If you do not wish to create a shareable package from your source code, you may delete this file without affecting the rest of the template components.

#### Data Storage ([+data/](data/))

Raw data should be kept separate from processed data, and code to process data should be located in either the source code directory or a jupyter notebook, depending on the project design. In practice, you might store the data directly in these folders, or instead you might document an external location where the data is stored. 

If you submit your work to the [Coding Examples Repository](https://github.com/FredHutch/wiki-code-examples), we ask that data not be stored directly in your files in order to keep the examples repo lightweight for easy cloning/sharing. 

#### Documentation ([+doc/](doc/))

This directory is a catch-all for any supporting work for your project. Depending on how you are sharing your code, you may want to build a brief tutorial or provide install instructions/dependencies for your package. For code associated with research, background/source documents, papers, and presentations can all be included here.

#### Source Code ([+project_name/](project_name/))

This directory should contain all the source code for your project. Note that python modules should have all lower case names with no hyphens, and underscores are encouraged for word separation. You also should rename this directory to a meaningful name for your project. 

The `__init__.py` file is required in each module subfolder in order to import the contained modules. In other words, do not delete this file and make sure to create a new `__init__.py` in each subfolder that houses python modules.

#### Results ([+results/](results/))

One of the benefits of using this project template correctly is that your results will always be easy to find. By default, a jupyter notebook exists in this folder. You might also want to write your output to this directory, or include a final report or presentation.

#### Tests ([+tests/](tests/))

The tests folder is a starter stub for unit testing your source code. A `test_sample_module.py` file shows a basic import of the python unittest class and it's usage for testing your python modules. In practice, you'll want to run unit tests on all your functions to confirm expected outputs and expected exceptions. There are a few additional resources listed in the docstrings of this sample file. 

The `__init__.py` file is necessary to automate unit test execution at each git push, as is done with Travis Continuous Integration
