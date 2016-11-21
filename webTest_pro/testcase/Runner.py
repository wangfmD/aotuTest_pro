from _env import addPaths
addPaths('.')
from config import TestRunner

if __name__ == '__main__':
    runner = TestRunner('dev_wf_57','is')
    runner.run()
