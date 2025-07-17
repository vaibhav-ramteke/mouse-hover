@echo off
cd %~dp0.venv\Scripts
call activate
cd..
cd..
python hover.py
