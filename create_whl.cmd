::    VSenseBox - Python toolbox for visual sensing
::    GNU Affero General Public License v3.0 or later (AGPLv3+)
::    Copyright (C) 2026 UMONS-Numediart

@echo off
setlocal
cd /d %~dp0
set "PYTHONWARNINGS=ignore"
python -m pip install --upgrade pip
pip install wheel build PyYAML
python -m build --wheel --skip-dependency-check --no-isolation
pause