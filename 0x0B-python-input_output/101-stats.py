#!/bin/bash
python3 -m py_compile $PYFILE
cp __pycache__/*.pyc $PYFILE"c"
