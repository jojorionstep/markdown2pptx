#!/usr/bin/env python

import re
from pprint import pprint

class Parse():
    def __init__(self):
        self.title = ''
        self.sub_title = []

    def read(self,mdfile):
        try:
            with open(mdfile) as f:
                self.lines = f.read()
        except:
            print('\"{}\" cannot be opend '.format(mdfile))
            exit()

    def get_title(self):
        subtitle_split = self.lines.split('\n## ')
        titlepage  = subtitle_split.pop(0)
        pprint(titlepage)
        m = re.search('#\s+(.*)\n(.*)',titlepage)
        title = ''
        subtitle = ''
        if m:
            title = m.group(1)
            subtitle = m.group(2)
        return title,subtitle,subtitle_split

class Page():
    def __init__(self):
        self.lists = []
        self.title = []
        self.text = ''

    def split_elem(self,body):
        sentence = body.split('\n')
        self.title = sentence.pop(0)
        self.text = ''.join(sentence)
