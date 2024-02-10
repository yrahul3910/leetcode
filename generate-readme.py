import subprocess
import os
import threading

class list(list):
    def map(self, f):
        return list(map(f, self))

from typing import Literal


class Problem:
    colors = {
        'easy': '10B981',
        'medium': 'FAC31D',
        'hard': 'EF4444'
    }
    style = 'for-the-badge'  

    def __init__(self, difficulty: Literal['easy', 'medium', 'hard'], name: str):
        self.difficulty = difficulty
        self.name = name

    def _title_case(self, name: str):
        exceptions = ['a', 'an', 'of', 'the', 'is']
        words = name.split()
        final = [words[0].capitalize()]
        for word in words[1:]:
            final.append(word if word in exceptions else word.capitalize())

        return ' '.join(final)

    def __repr__(self):
        name_with_spaces = ' '.join(self.name.split('.')[0].split('-'))
        return f'* [{self._title_case(name_with_spaces)}]({difficulty}/{self.name}) ![Static Badge](https://img.shields.io/badge/{self.difficulty.capitalize()}-{self.colors[self.difficulty]}?style={self.style})\n'


out = open('README.md', 'w')
out.write('# LeetCode Solutions\n\n# Problems by topic\n\n')

problems = {}
for difficulty in ['easy', 'medium', 'hard']:
    __proc = subprocess.Popen(f'ls {difficulty}/*.md', shell=True, cwd=os.getcwd(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    __proc.wait()
    EXIT_CODE = __proc.returncode
    __comm = __proc.communicate()
    _, STDERR = __comm[0].decode('utf-8').rstrip(), __comm[1].decode('utf-8').rstrip()
    _ = _.split('\n')
    for file in _:
        name = file.split('/')[-1]
        if name.strip() == '':
            continue

        in_file = open(file, 'r')
        lines = in_file.readlines()
        idx = [i for i, line in enumerate(lines) if line.startswith('## Topics')][0]
        topics = lines[idx + 2].strip().split('; ')

        for topic in topics:
            if topic not in problems:
                problems[topic] = []

            problems[topic].append(Problem(difficulty, name))

for topic in sorted(problems.keys()):
    out.write(f'## {topic}\n\n')
    for problem in problems[topic]:
        out.write(str(problem))
    out.write('\n')
