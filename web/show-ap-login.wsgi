import sys
import os

project_root = os.path.dirname(__file__)
sys.path.append(project_root)

from app import app as application
