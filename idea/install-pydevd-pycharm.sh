#!/bin/bash
#Install:
pip3 install pydevd-pycharm~=193.7288.26
#MONKEY-PATCH version reporting to make buggy .30 plugin happy (IDEA 2019.3.5)
sed -i "s/193.7288.30/193.7288.26/" ~/.local/lib/python3.*/site-packages/_pydevd_bundle/pydevd_comm.py
