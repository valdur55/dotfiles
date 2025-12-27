#!/bin/bash
#Install:
pipx inject py3status pydevd-pycharm~=253.29346.138
#MONKEY-PATCH version reporting to make buggy .142 plugin happy (IntelliJ IDEA 2025.3.1)
sed -i "s/253.29346.142/253.29346.138/" ~/.local/share/pipx/venvs/py3status/lib/python3.13/site-packages/_pydevd_bundle/pydevd_comm.py
