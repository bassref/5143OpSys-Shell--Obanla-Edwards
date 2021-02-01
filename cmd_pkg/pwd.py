import threading

import sys

import os

import glob

from pathlib import Path







def pwd(**kwargs):

	path = Path.cwd()

	print("current working directory: " , path)