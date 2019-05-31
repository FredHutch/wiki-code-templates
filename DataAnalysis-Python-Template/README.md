# Data Analysis Template Usage

This template is built to accommodate a Python project used primarily for data analysis. While sharing results is encouraged, it is not anticipated that the underlying code will be packaged for re-use. This template is set up for when you need a single Jupyter notebook, or a single `.py` file to batch for your results. All additional files in the template represent the minimum requirements to keep in mind when developing or sharing any data analysis project.

To review the coding standards at Fred Hutch, please see the [Scientific Computing Wiki](https://sciwiki.fredhutch.org/scicomputing/software_standards/). By maintaining these standards across Fred Hutch, our work is reproducible and easier for other researchers to review and adapt to their own purposes. To browse the library of examples originating from this template (or submit your own code to be shared), see our linked [Data Analysis Examples Repository](https://github.com/FredHutch/wiki-code-examples/data-analysis).

With this template, you can choose between building your data analysis project in an interactive Jupyter notebook, or in a python script to be run on the command line. Details for both options are described below.

## Jupyter Notebook Project

You may want to build your entire data analysis project within a Jupyter notebook. In this case, you can find a template `ProjectName.ipynb` file in the root folder of this template directory. Please replace `ProjectName` with a name meaningful to your project. By saving your final notebooks in this location, anyone following up on your code can readily and unambiguously access the conclusions of your work. 

Jupyter notebooks allow the flexibility to add interactive features, as well as mark-down text for documentation clarity. In a standalone notebook project, no further documentation is required in the directory if the workbook is well-documented. A well-documented notebook should include contextual information in markdown cells, and docstrings for all functions.

When you run your Jupyter notebook, a `.ipynb_checkpoints\` directory will be created in the root folder. This directory stores information needed to run your Jupyter notebook. It should be left alone if you are developing an interactive notebook. 

Here is an example of a data analysis project contained in a Jupyter notebook, developed from this template: [TODO: Standalone Notebook](https://github.com/FredHutch/wiki-code-examples).

If you choose to work in an interactive notebook instead of the command line, then the `project_name.py` file is not needed. Deleting it will not affect the remainder of files in the template.

## Command Line Project

To run a Python module on the command line, you simply need to run Python with the path to the code you wish to run. In this case, you should write your code to the `project_name.py` file (after giving it a meaningful name).

For example, using a python 3 environment from the project root directory in rhino, we can run the contents of a file `project_name.py` in the source code folder:
```
username@rhino2:~/DataAnalysis-Python-Template$ ml Python
username@rhino2:~/DataAnalysis-Python-Template$ python project_name.py
```
Batching is simply automating what you would do on the command line. In general, the automation steps go in a `.bat` file. For computing at Fred Hutch, we refer to the description and instructions available on the [Scientific Computing Wiki](https://sciwiki.fredhutch.org/computing/cluster_usingSlurm/).

Here is an example of a data analysis project contained in a python script, developed from this template: [TODO: commmand line data analysis project example](https://github.com/FredHutch/wiki-code-examples).

Please note that if you do not wish to use a notebook interface, then the `ProjectName.ipynb` file can be deleted without affecting the remainder of the template.

# File Structure

The minimum file structure is diagrammed below, followed by further discussion of the usage of each item. (See above for discussion of `project_name.py` and `ProjectName.ipynb`).

```
DataAnalysis-Python-Template/
  |- README.md
  |- LICENSE
  |- ProjectName.ipynb
  |- project_name.py
  |- data/
      |- raw_data/
      |- processed_data/
  |- doc/
      |- doc_instructions.md
```

#### README

Every project should have a README file, that describes the contents of the project directory and the intended use of the code. This document can be plain text, although markdown is convenient for sharing links and formatting. The [Scientific Computing Wiki](https://sciwiki.fredhutch.org/compdemos/vscode_markdown_howto/) contains several resources for markdown tips as well as the VS Code editor.

#### License

All shared code and anlaysis needs to be released under a license. The default template license is the MIT license, as it comes with very limited restrictions and is considered a good choice for open research and code sharing. For more information on the MIT license, see the [full text](https://opensource.org/licenses/MIT). 

To set a different license for your project, you will need to delete the MIT license and [replace it](https://help.github.com/en/articles/adding-a-license-to-a-repository) before publicly releasing your project.

#### Data Storage ([+data/](data/))

Raw data should be kept separate from processed data, and code to process data should be located in either the source code directory or a jupyter notebook, depending on the project design. In practice, you might store the data directly in these folders, or instead you might document an external location where the data is stored. To keep the examples repository lightweight, we ask that data not be stored in the repository. 

#### Documentation ([+doc/](doc/))

This directory is a catch-all for any supporting work for your project. Depending on how you are sharing your code, you may want to build a brief tutorial or provide instruction in a README file. For code associated with research, background/source documents, papers, and presentations can all be included here.
