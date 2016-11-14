from _env import addPaths
addPaths('.')
from config import TestRunner

if __name__ == '__main__':
    runner = TestRunner('dev')
    runner.run()
