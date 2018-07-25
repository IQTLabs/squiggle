.. Squiggle documentation master file, created by
   sphinx-quickstart on Thu Jul  5 23:24:54 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Squiggle
========

|Build Status| |Cov| |CodeFactor| |Docs| |PyPI|


`Squiggle <https://github.com/Lab41/squiggle>`_ is a two-dimensional DNA
sequence visualization library that can turn FASTA sequence files like this:

.. code-block:: text

    >lcl|NC_000011.10_cds_NP_000509.1_1 [gene=HBB]
    ATGGTGCATCTGACTCCTGAGGAGAAGTCTGCCGTTACTGCCCTGTGGGGCAAGGTGAACGTGGATGAAG
    TTGGTGGTGAGGCCCTGGGCAGGCTGCTGGTGGTCTACCCTTGGACCCAGAGGTTCTTTGAGTCCTTTGG
    GGATCTGTCCACTCCTGATGCTGTTATGGGCAACCCTAAGGTGAAGGCTCATGGCAAGAAAGTGCTCGGT
    GCCTTTAGTGATGGCCTGGCTCACCTGGACAACCTCAAGGGCACCTTTGCCACACTGAGTGAGCTGCACT
    GTGACAAGCTGCACGTGGATCCTGAGAACTTCAGGCTCCTGGGCAACGTGCTGGTCTGTGTGCTGGCCCA
    TCACTTTGGCAAAGAATTCACCCCACCAGTGCAGGCTGCCTATCAGAAAGTGGTGGCTGGTGTGGCTAAT
    GCCCTGGCCCACAAGTATCACTAA

into gorgeous, interactive visualizations like this:

.. raw:: html
    :file: figures/human_hbb.html

Installation
------------

If you don't have Python 3.4 or greater installed, be sure to `get it
<https://www.python.org/downloads/>`_. To get the current stable version of
Squiggle, run::

    $ pip install squiggle

Or, alternatively, if you want to get the latest development version::

    $ pip install git+https://github.com/Lab41/squiggle.git

Usage
-----

Using Squiggle is as easy as::

    $ squiggle your_sequence.fasta

Squiggle has tons of options available to make beautiful, interactive
visualizations of DNA sequences. To get a full rundown of the various option,
take a look at the :ref:`guide`.

Citation
--------

To be determined!


Table of Contents
-----------------

.. toctree::
   :maxdepth: 2

   methods
   user_guide
   api
   cli
   license


Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

.. |Build Status| image:: https://travis-ci.org/Lab41/squiggle.svg?branch=master
   :target: https://travis-ci.org/Lab41/squiggle

.. |Cov| image:: https://codecov.io/gh/Lab41/squiggle/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/Lab41/squiggle

.. |Docs| image:: http://readthedocs.org/projects/freqgen/badge/?version=latest
   :target: http://squiggle.readthedocs.io/en/latest/?badge=latest

.. |CodeFactor| image:: https://www.codefactor.io/repository/github/Lab41/squiggle/badge
   :target: https://www.codefactor.io/repository/github/Lab41/squiggle/

.. |PyPI| image:: https://img.shields.io/pypi/v/squiggle.svg
   :target: https://pypi.org/project/squiggle/
