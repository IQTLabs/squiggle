 .. _guide:

User Guide
==========

Squiggle is designed to be easy to use while still providing complete
flexibility to the user. For the sake of demonstration, we'll be using four
different species' β-globin genes (human, chimpanzee, rhesus macaque, and Norway
rat).

For a full list of the command line options and their meanings, see the
:ref:`cli`.

Basic Usage
-----------

The easiest way to visualize a sequence is by passing a FASTA file to Squiggle::

    $ squiggle human_HBB.fasta

.. raw:: html
    :file: figures/human_hbb.html

To use a different visualization method, provide ``--method`` with a setting
(see :ref:`methods` for a description of the supported methods)::

    $ squiggle human_HBB.fasta --method=gates

.. raw:: html
    :file: figures/human_hbb_gates.html

Plotting Multiple Sequences
---------------------------

If your FASTA file has multiple sequences, they will get plotted together
automatically. If, however, your sequences are in separate files, you can still
plot them together by passing multiple files to Squiggle::

    $ squiggle human_HBB.fasta chimpanzee_HBB.fasta norway_rat_HBB.fasta rhesus_HBB.fasta

.. raw:: html
    :file: figures/multiple.html

To put them on separate plots, use the ``--separate`` flag::

    $ squiggle human_HBB.fasta chimpanzee_HBB.fasta --separate

.. raw:: html
    :file: figures/separate.html

By default, their :math:`x` axes are linked. This can be disabled with
``--no-link-x`` (try if for yourself by panning around)::

    $ squiggle human_HBB.fasta chimpanzee_HBB.fasta --separate --no-link-x

.. raw:: html
    :file: figures/no-link-x.html

Similarly, the :math:`y` axes can be linked and unlinked with
``--link-y/--no-link-y``.

Note that when plotting seperately, Squiggle will try to make the layout as
square as possible. If you want to specify the number of columns, you can do so
with the ``-c`` option.

If you want to compare FASTA files, you can use the ``--mode=file`` flag to
treat each file as a separate entity, as opposed to each sequence. The
``--mode=auto`` flag (which is the default) will attempt to visualize each
sequence independently unless there are too many, in which case it will switch
to file mode.

As an example, let's compare the highly expressed genes of *E. coli* and *B.
anthracis*. Because there are so many sequences, we are going to `downsample
<https://en.wikipedia.org/wiki/Decimation_(signal_processing)>`_ them by a
factor of 25 using the ``-s`` flag in order to improve performance::

    $ squiggle ecol.heg.fasta banth1.heg.fasta -s 25

.. raw:: html
    :file: figures/file_mode.html

Also, be aware that the ``--hide`` flag will make it so that clicking on the
name of a sequence or file in the legend will hide it for easier comparisons.

.. note::

    Using the ``--hide`` flag may result in a significant slowdown when
    visualizing a large number of sequences.

Finally, the palette can be controlled by the ``-p`` option. Valid palettes can
be seen `here <https://bokeh.pydata.org/en/latest/docs/reference/palettes.html>`_::

    $ squiggle human_HBB.fasta chimpanzee_HBB.fasta -p Accent

.. raw:: html
    :file: figures/colors.html

Controlling Output
------------------

If you don't want to show your plot in a browser but would rather save it for
later, you can do so with the ``-o`` option::

    $ squiggle human_HBB.fasta -o output.html

If you don't have an internet connection, you can still use Squiggle by telling
it to include the full Bokeh plotting library in its output with ``--offline``::

    $ squiggle human_HBB.fasta --offline

.. warning::

   This will signifcantly increase the size of your output file.

To adjust the dimensions of your output, use the ``-d`` option, providing the
width and height (in that order)::

    $ squiggle human_HBB.fasta -d 650 150

.. raw:: html
    :file: figures/dimensions.html

By default, Squiggle titles the plot with the name of the sequence, as
determined by the FASTA file. If you want to override it, you can manually
provide the title::

    $ squiggle human_HBB.fasta -t β-globin

.. raw:: html
    :file: figures/title.html

If applicable, you can also specify the location of the legend using the
``--legend-loc`` flag. The default setting is to put the legend in the top left.

Python API
----------

Squiggle also has a Python API that you can interface with to get access to the
low level :math:`x` and :math:`y` coordinates being plotted::

    >>> from squiggle import transform
    >>> transform("ATGC")
    ([0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0], [0, 0.5, 0, -0.5, -1, -0.5, 0, -0.5, 0])
    >>> transform("ATGC", method="gates")
    ([0, 0, 0, 1, 0], [0, -1, 0, 0, 0])

For the full details, take a look at the :ref:`API <API>` specification page.
