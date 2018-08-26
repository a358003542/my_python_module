#!/usr/bin/env python
# -*-coding:utf-8-*-


from bihu.algorithms.longest_common_subsequence import longest_common_subsequence


def test_lcs():
    longest_common_subsequence('fort', 'fosh')
    longest_common_subsequence('fish', 'fosh')

from bihu.algorithms.longest_increasing_subsequence import longest_increasing_subsequence


def test_lis():
    longest_increasing_subsequence('fish', 'hish')
    longest_increasing_subsequence('hish', 'vista')