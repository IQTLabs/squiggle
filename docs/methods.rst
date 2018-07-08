Visualization Methods
=====================

There are a variety of ways to visualize DNA sequences in two dimensions.
Squiggle provides its own novel visualization method as well as implementations
of various other methods. Each method captures a different aspect of a sequence,
so it is highly recommended to try using multiple methods in order to get a feel
for a sequence.

Squiggle
--------

Squiggle's DNA visualization method is based on the `UCSC .2bit format
<http://genome.ucsc.edu/FAQ/FAQformat.html#format7>`_ and the `Qi et. al Huffman
coding method <http:/dx.doi.org/10.1002/jcc.21906>`_. In essence, a DNA sequence
is first converted into binary using the 2bit encoding scheme that maps T to 00,
C to 01, A to 10, and G to 11. For example::

    ATGC

becomes::

    10001101

Then, starting at the origin, for each bit, the following vectors are layed end to end:

.. raw:: html
    :file: figures/squiggle_vectors.html

This mapping has the effect of giving each nucleotide a distinctive shape:

.. raw:: html
    :file: figures/squiggle_bases.html

This encoding method has several handy features:

- Based on an open, common bioinformatics format.
- No degeneracy in the encoding (an encoding can only map to one sequence and vice versa).
- The overall GC-content can be inferred from at a glance based on whether the endpoint of the graph is above or below zero.
- `Regions inside the gene with varying GC-content <https://en.wikipedia.org/wiki/CpG_site>`_ can be seen as peaks and valleys.
- Is limited to quadrants I and IV and is a function
- The x-axis corresponds directly with nucleotide position