::    VSenseBox - Python toolbox for visual sensing
::    GNU General Public License v3 or later (GPLv3+)
::    Copyright (C) 2024 UMONS-Numediart

@echo off
setlocal
cd /d %~dp0
set "PYTHONWARNINGS=ignore"
python -m pip install --upgrade pip
pip install wheel build PyYAML
python -m build --wheel --skip-dependency-check --no-isolation
pause