# This repository has moved to https://github.com/Benjamin-Lee/squiggle

<p align ="center">
<img src='https://github.com/Lab41/squiggle/raw/master/images/logo.png' height="150">
</p>

[![DOI](https://img.shields.io/badge/DOI-10.1093%2Fbioinformatics%2Fbty807-brightgreen.svg)](https://doi.org/10.1093/bioinformatics/bty807)
[![Build Status](https://travis-ci.org/Lab41/squiggle.svg?branch=master)](https://travis-ci.org/Lab41/squiggle)
[![Docs](http://readthedocs.org/projects/squiggle/badge/?version=latest)](http://squiggle.readthedocs.io/en/latest/?badge=latest)
[![PyPI](https://img.shields.io/pypi/v/squiggle.svg)](https://pypi.org/project/squiggle/)

Squiggle is a two-dimensional DNA sequence visualization library that can turn FASTA sequence files like this:

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
    <a href="https://htmlpreview.github.io/?https://github.com/Lab41/squiggle/blob/master/docs/figures/hbb_comparison.html">
    <img src="https://github.com/Lab41/squiggle/raw/master/images/HBB_squiggle.png" alt="Human Squiggle" width="750px"/>
</p>

(Click the picture to view an [interactive version](https://htmlpreview.github.io/?https://github.com/Lab41/squiggle/blob/master/docs/figures/hbb_comparison.html).)

## Installation

If you don't have Python 3.5 or greater installed, be sure to [get it](https://www.python.org/downloads/).
To get the current stable version of Squiggle, run:

    $ pip install squiggle

Or, alternatively, if you want to get the latest development version:

    $ pip install git+https://github.com/Lab41/squiggle.git

## Usage

Using Squiggle is as easy as:

    $ squiggle your_sequence.fasta

Squiggle has tons of options available to make beautiful, interactive visualizations of DNA sequences.
To get a full rundown of the various option, take look at the documentation [here](https://squiggle.readthedocs.io).

## Citation

Using Squiggle in your research? Please cite it!

- Lee, B. D. (2018). Squiggle: a user-friendly two-dimensional DNA sequence visualization tool. _Bioinformatics_. doi:[10.1093/bioinformatics/bty807](doi.org/10.1093/bioinformatics/bty807)

```
@article{Lee2018,
  doi = {10.1093/bioinformatics/bty807},
  url = {https://doi.org/10.1093/bioinformatics/bty807},
  year  = {2018},
  month = {sep},
  publisher = {Oxford University Press ({OUP})},
  author = {Benjamin D Lee},
  editor = {John Hancock},
  title = {Squiggle: a user-friendly two-dimensional {DNA} sequence visualization tool},
  journal = {Bioinformatics}
}
```
