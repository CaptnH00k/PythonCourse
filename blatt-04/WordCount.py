#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Copyright 2017, University of Freiburg,
Chair of Algorithms and Data Structures.
Hannah Bast <bast@cs.uni-freiburg.de>
Axel Lehmann <lehmann@cs.uni-freiburg.de>

Author: Leon Gnädinger <leon.gnaedinger@gmail.com>.
"""

import re

from HashMap import HashMap


class WordCount:
    def __init__(self):
        self.hash_map = HashMap(3000)

    def read_text_file(self, file_path):
        """
        Read in a text file and add all words to the Internal
        HashMap. Value will be updated to how often the word was
        found.

        Copyright:
            Code taken and minimally modified
            from public/code/vorlesung-04/python/words_main.py
            Original written by Hannah Bast and Axel Lehmann.

        Args:
            file_path (string) - path to text file to read in

        Examples:
            >>> wc = WordCount()
            >>> wc.read_text_file('./WordCount.TIP')
            >>> wc.hash_map.lookup('to')
            7
            >>> wc.hash_map.lookup('freiburg')
            4
            >>> wc.hash_map.lookup('wordcount')
            6
            >>>
        """
        with open(file_path) as fh:
            for line in fh:
                for word in re.split('\W+', line):
                    word = word.lower()
                    if len(word):
                        count = self.hash_map.lookup(word) + 1
                        self.hash_map.insert(word, count)

    def compute_frequency_lines(self):
        """
        Figures out the 500 most occuring words currently in our HashMap
        and returns them as [(word, frequency)]. First element will be highest
        occuring word, last least occuring word.

        Returns:
            List of word/frequency pairs

        Examples:
            >>> wc = WordCount()
            >>> wc.read_text_file('WordCount.TIP')
            >>> mow = wc.compute_frequency_lines()
            >>> mow[0]
            '1\\t9\\twc'
            >>> mow[1]
            '2\\t7\\tto'
            >>> mow[-1]
            '120\\t1\\tcomputefrequencylines'
        """
        word_frequencies = self.hash_map.get_key_value_pairs()
        sorted_word_frequencies = sorted(
            word_frequencies,
            key=(lambda kv: kv[1]),
            reverse=True
        )
        most_occuring_words = []
        i = 1
        for (word, frequency) in sorted_word_frequencies[:500]:
            most_occuring_words.append(
                str(i) + "\t" + str(frequency) + "\t" + word
            )
            i += 1
        return most_occuring_words


if __name__ == "__main__":
    wc = WordCount()
    wc.read_text_file("./pruefungsordnung.txt")
    most_occuring_words = wc.compute_frequency_lines()
    f = open('words.txt', 'w')
    for line in most_occuring_words:
        f.write(line + "\r\n")
    f.close()
