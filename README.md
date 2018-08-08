![Logo](https://github.com/Lab41/squiggle/raw/master/images/logo.png)

[![Build Status](https://travis-ci.org/Lab41/squiggle.svg?branch=master)](https://travis-ci.org/Lab41/squiggle)
[![Cov](https://codecov.io/gh/Lab41/squiggle/branch/master/graph/badge.svg)](https://codecov.io/gh/Lab41/squiggle)
[![CodeFactor](https://www.codefactor.io/repository/github/Lab41/squiggle/badge)](https://www.codefactor.io/repository/github/Lab41/squiggle/)
[![Docs](http://readthedocs.org/projects/squiggle/badge/?version=latest)](http://squiggle.readthedocs.io/en/latest/?badge=latest)
[![PyPI](https://img.shields.io/pypi/v/squiggle.svg)](https://pypi.org/project/squiggle/)

Squiggle is a two-dimensional DNA sequence visualization library that can turn
FASTA sequence files like this:

    >lcl|NC_000011.10_cds_NP_000509.1_1 [gene=HBB]
    ATGGTGCATCTGACTCCTGAGGAGAAGTCTGCCGTTACTGCCCTGTGGGGCAAGGTGAACGTGGATGAAG
    TTGGTGGTGAGGCCCTGGGCAGGCTGCTGGTGGTCTACCCTTGGACCCAGAGGTTCTTTGAGTCCTTTGG
    GGATCTGTCCACTCCTGATGCTGTTATGGGCAACCCTAAGGTGAAGGCTCATGGCAAGAAAGTGCTCGGT
    GCCTTTAGTGATGGCCTGGCTCACCTGGACAACCTCAAGGGCACCTTTGCCACACTGAGTGAGCTGCACT
    GTGACAAGCTGCACGTGGATCCTGAGAACTTCAGGCTCCTGGGCAACGTGCTGGTCTGTGTGCTGGCCCA
    TCACTTTGGCAAAGAATTCACCCCACCAGTGCAGGCTGCCTATCAGAAAGTGGTGGCTGGTGTGGCTAAT
    GCCCTGGCCCACAAGTATCACTAA
    >lcl|NC_005100.4_cds_NP_150237.1_1 [gene=HBB]
    ATGGTGCACCTGACTGATGCTGAGAAGGCTGCTGTTAATGGCCTGTGGGGAAAGGTGAACCCTGATGATG
    TTGGTGGCGAGGCCCTGGGCAGGCTGCTGGTTGTCTACCCTTGGACCCAGAGGTACTTTGATAGCTTTGG
    GGACCTGTCCTCTGCCTCTGCTATCATGGGTAACCCTAAGGTGAAGGCCCATGGCAAGAAGGTGATAAAC
    GCCTTCAATGATGGCCTGAAACACTTGGACAACCTCAAGGGCACCTTTGCTCATCTGAGTGAACTCCACT
    GTGACAAGCTGCATGTGGATCCTGAGAACTTCAGGCTCCTGGGCAACATGATTGTGATTGTGTTGGGCCA
    CCACCTGGGCAAGGAATTCTCCCCCTGTGCACAGGCTGCCTTCCAGAAGGTGGTGGCTGGAGTGGCCAGT
    GCCCTGGCTCACAAGTACCACTAA

into gorgeous, interactive visualizations like this:

<p align ="center">
    <img src="https://github.com/Lab41/squiggle/raw/master/images/HBB_squiggle.png" alt="Human Squiggle" width="750px"/>
</p>

## Installation

If you don't have Python 3.4 or greater installed, be sure to [get it
](https://www.python.org/downloads/). To get the current stable version of
Squiggle, run:

    $ pip install squiggle

Or, alternatively, if you want to get the latest development version:

    $ pip install git+https://github.com/Lab41/squiggle.git

## Usage

Using Squiggle is as easy as:

    $ squiggle your_sequence.fasta

Squiggle has tons of options available to make beautiful, interactive
visualizations of DNA sequences. To get a full rundown of the various option,
take look at the documentation [here](https://squiggle.readthedocs.io).

## Citation

To be determined!
