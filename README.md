# Create conda environment

Conda environment can be created with conda as follows:

```
conda env create -f conda/env/dev.yml
conda develop src
```

# Build one file binary

These are the steps to create a binary that runs just as `entry_point.py`

```
python -m nuitka --onefile entry_point.py
./entry_point.bin
```

# Build package (using `entry_point.py`)

These are the steps to compile the package as a module:

```
python -m nuitka --module entry_point.py --include-package='company.project_name'
```

This creates `entry_point.cpython-36m-x86_64-linux-gnu.so` even if
`entry_point.py` is an empty file.

Alternatively, the path to the `__init__.py` as follows can be passed:
```
python -m nuitka --module src/company/project_name/__init__.py --include-package='company.project_name'
```

As in the previous example, this creates `__init__.cpython-36m-x86_64-linux-gnu.so`,

What is the expected way to compile a package? Once the `.so` file is created,
what would be the best way to use this as the replacement for the
`company.project_name` package?


# Build package (using module name)

If module name is passed to `--module` option instead of a `.py` file:

```
python -m nuitka --module 'company_project_name' --include-package='company.project_name'
```

The following error message is returned:
```
Nuitka-Options:INFO: Used command line options: --module company_project_name --include-package=company.project_name
Nuitka:INFO: Starting Python compilation with Nuitka '0.7.6' on Python '3.6' commercial None.
Traceback (most recent call last):
  File "/home/user/miniconda3/envs/company.project_name/lib/python3.6/site-packages/nuitka/__main__.py", line 137, in <module>
    main()
  File "/home/user/miniconda3/envs/company.project_name/lib/python3.6/site-packages/nuitka/__main__.py", line 123, in main
    MainControl.main()
  File "/home/user/miniconda3/envs/company.project_name/lib/python3.6/site-packages/nuitka/MainControl.py", line 919, in main
    main_module = _createNodeTree(filename=filename)
  File "/home/user/miniconda3/envs/company.project_name/lib/python3.6/site-packages/nuitka/MainControl.py", line 119, in _createNodeTree
    is_main=not Options.shallMakeModule(),
  File "/home/user/miniconda3/envs/company.project_name/lib/python3.6/site-packages/nuitka/tree/Building.py", line 1144, in buildMainModuleTree
    hide_syntax_error=False,
  File "/home/user/miniconda3/envs/company.project_name/lib/python3.6/site-packages/nuitka/tree/Building.py", line 1244, in buildModule
    logger=general,
  File "/home/user/miniconda3/envs/company.project_name/lib/python3.6/site-packages/nuitka/importing/Importing.py", line 697, in decideModuleSourceRef
    assert type(module_name) is ModuleName
AssertionError
```

Is this the expected behavior?
