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

For an example, let's look at the human β-globin gene using the squiggle method::

    $ squiggle example_seqs/human_HBB.fasta

.. raw:: html
    :file: figures/human_hbb.html

Gates
-----

In `Gates's method <https://doi.org/10.1016/s0022-5193(86)80144-8>`_, DNA
sequences are converted into 2D walks in which Ts, As, Cs, and Gs are up, down,
left, and right, respectively. This gives each sequence a "shape." However,
there is degeneracy, meaning that a visualization is not necessarily unique. For
example, ``TGAC`` is a square (up, right, down, and left), but so is ``GTCA``
(right, up, left, down).

To see an example of Gate's method, we'll again look at human β-globin::

    $ squiggle example_seqs/human_HBB.fasta --method=gates

.. raw:: html
    :file: figures/human_hbb_gates.html

Yau
---

`Yau et. al's method <https://doi.org/10.1093/nar/gkg432>`_ uses unit vectors
with upward vectors indicating pyrimidine bases (C and T) and downward vectors
indicating purine bases (A and G). Similar to Squiggle, this method has no
degeneracy.

Specifically,

:math:`A\rightarrow\left(\frac{1}{2},-\frac{\sqrt{3}}{2}\right)`,
:math:`T\rightarrow\left(\frac{1}{2},\frac{\sqrt{3}}{2}\right)`,
:math:`G\rightarrow\left(\frac{\sqrt{3}}{2}, -\frac{1}{2}\right)`,
:math:`C\rightarrow\left(\frac{\sqrt{3}}{2}, \frac{1}{2}\right)`.

.. Warning::

   The x-coordinate in Yau's method is not equivalent to base position.

.. raw:: html
    :file: figures/yau_bases.html

It produces a visualization of β-globin like this::

    $ squiggle example_seqs/human_HBB.fasta --method=yau

.. raw:: html
    :file: figures/human_hbb_yau.html

Randić and Qi
-------------

`Randić et al. <https://doi.org/10.1016/s0009-2614(02)01784-0>`_ and `Qi and Qi
<https://doi.org/10.1016/j.cplett.2007.03.107>`_'s methods are similar to
`tablature <https://en.wikipedia.org/wiki/Tablature>`_, with a different base
(or 2-mer in the case of Qi's method) assigned to each :math:`y` value. The best
way visualize it is through an example.

Let's look at the Randić visualization of ``GATC``:

.. raw:: html
    :file: figures/randic_example.html

Look's pretty good. However, this visualization method isn't well suited to long
sequences, as we'll see when we look at β-globin::

    $ squiggle example_seqs/human_HBB.fasta --method=randic

.. raw:: html
    :file: figures/human_hbb_randic.html

Qi's method produces very similar results, just with a much larger range of
:math:`y` values::

    $ squiggle example_seqs/human_HBB.fasta --method=qi

.. raw:: html
    :file: figures/human_hbb_qi.html
