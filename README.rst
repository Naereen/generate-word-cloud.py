``generatewordcloud.py``
========================

A simple Python script to generate a square wordcloud from one (or more) text file(s).
Supporting both Python 2 and 3 (2.7+ and 3.4+).
|generatewordcloud in pypi|

|generate-word-cloud example meta|

Based on the great `word\_cloud <https://github.com/amueller/word_cloud/>`__ module by `@amueller <https://github.com/amueller/>`__.


|PyPI version|
|PyPI license|
|PyPI format|
|PyPI pyversions|
|PyPI implementation|
|PyPI status|

--------------

How to use it?
--------------

1. `Requirements <requirements.txt>`__
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The usual module `matplotlib <http://matplotlib.org/>`__ is needed for the plotting,
`docopt <https://github.com/docopt/docopt>`__ is needed for the command line interface,
and `word\_cloud <https://github.com/amueller/word_cloud/>`__ is needed for the actual work (generating the cloud of words after reading the files).

The required Python (2 or 3) modules can be installed with `pip <http://pip.readthedocs.io/>`__, either directly:

.. code:: bash

    # Directly:
    sudo pip install matplotlib docopt word_cloud

Or with the `requirements.txt <requirements.txt>`__ file:

.. code:: bash

    sudo pip install -r requirements.txt


*Note*: if `ansicolortags <https://pypi.python.org/pypi/ansicolortags>`__ is
available, it will be used to print nice colors in the help and during the generation of word clouds.


2. Installation
~~~~~~~~~~~~~~~

Clone the repository, copy the `script (generate-word-cloud.py) <./generate-word-cloud.py>`__ somewhere in your ``PATH`` (e.g., ``~/.local/bin/``).

You can also just download the script itself:

.. code:: bash

    $ wget https://raw.githubusercontent.com/Naereen/generate-word-cloud.py/master/generate-word-cloud.py
    $ cp generate-word-cloud.py /path/to/a/directory/in/your/PATH/


Note: The script is *also* available from `PyPI <https://pypi.python.org/pypi/>`__ : `pypi.python.org/pypi/generatewordcloud <https://pypi.python.org/pypi/generatewordcloud>`_.
You can install it using `pip <http://www.pip-installer.org/>`__.

.. code:: bash

    $ sudo pip install generatewordcloud


|PyPI version|
|PyPI license|
|PyPI format|
|PyPI pyversions|
|PyPI implementation|
|PyPI status|


3. Usage
~~~~~~~~

Help:
^^^^^

.. code:: bash

    $ generate-word-cloud.py --help

From one or two files
^^^^^^^^^^^^^^^^^^^^^

Generate a wordcloud from two ``txt`` files in the current directory,
save it to ``wordcloud_txt.png``.

.. code:: bash

    $ generate-word-cloud.py -o ./wordcloud_txt.png ./file1.txt ./file2.txt

Generate a wordcloud from the textfile ``hamlet.txt`` (~ 8000 lines),
saving to ``hamlet.png``:

.. code:: bash

    $ generate-word-cloud.py -o ./hamlet.png ./hamlet.txt

|generate-word-cloud example hamlet|

(It should work on pretty big text files without any issue.)

--------------

Other examples
--------------

From a lot of Python scripts (~ 200)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|generate-word-cloud example python|

From a lot of Bash scripts (~ 150)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|generate-word-cloud example bash|

From a lot of LaTeX files (~ 180)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|generate-word-cloud example LaTeX|

Meta example
~~~~~~~~~~~~

Generate a wordcloud from the `README.md <./README.md>`__ and
`generate-word-cloud.py <./generate-word-cloud.py>`__ files **of this
very project**, save it to ``wordcloud_meta.png``!

.. code:: bash

    $ generate-word-cloud.py -o ./wordcloud_meta.png ./*.md ./*.py

|generate-word-cloud example meta|

--------------

Features
--------

-  [x] Support one or more input file(s), will cleanly skip any file it
   fails to find or fails to read,
-  [x] Custom output file, won't be overwritten (except with ``-f``
   flag),
-  [x] Nice command line interface
   (`argparse <https://docs.python.org/2.7/library/argparse.html>`__
   powered). I switched to `docopt <https://github.com/docopt/docopt>`__
   after realizing how awesome it is!
-  [x] Has a command line option for every important parameter (max nb
   of words, width, height etc).
-  [x] Input filenames with spaces in their name were seen as several
   files (e.g. ``this file.txt``), FIXED with the switch to
   `docopt <https://github.com/docopt/docopt>`__.

--------------

Complete documentation (``--help``)
-----------------------------------

::

    $ generate-word-cloud.py -h | --help
    Usage:
      generate-word-cloud.py [-s | --show] [-f | --force] [-o OUTFILE | --outfile=OUTFILE]
                             [-t TITLE | --title=TITLE] [-m MAX | --max=MAX]
                             [-w WIDTH | --width=WIDTH] [-H HEIGHT | --height=HEIGHT]
                             INFILE...
      generate-word-cloud.py (-h | --help)
      generate-word-cloud.py (-v | --version)

    Options:
      -h --help            Show this help message and exit.
      -v --version         Show program's version number and exit.
      -s --show            Show the image but do not save it [default False].
      -f --force           Force to write the image, even if present (default is to ask before overwriting an existing file) [default False].
      -o OUTFILE --outfile=OUTFILE
                           Filename for the generated image [default 'wordcloud.png'].
      -t TITLE --title=TITLE
                           Title for the image [default None].
      -m MAX --max MAX
                           Max number of words to display on the cloud word [default 150].
      -w WIDTH --width WIDTH
                           Width of the generate image [default 400].
      -H HEIGHT --height HEIGHT
                           Height of the generate image [default 300].
      INFILE               A text file to read.

--------------

TODO
----

-  [x] Start it, from `this example <https://github.com/amueller/word_cloud/blob/master/examples/simple.py>`__,
-  [x] Run it on some interesting examples, embed them here (as images),
-  [X] Check on weird encodings? (i.e., not UTF-8). It works fine!
-  [X] Test it against :closed\_book: VERY large files (million of line)
   ? It works fine, slowly but fine.
-  [X] Test it against LOTS of files (several thousands) ? It
   works fine, slowly but fine.
-  [X] Publish it on PyPI: it is available at `pypi.python.org/pypi/generatewordcloud/ <https://pypi.python.org/pypi/generatewordcloud/>`_.
-  [ ] Write a small article about it for `my blog <http://perso.crans.org/besson/>`__.

Knows issues
~~~~~~~~~~~~

-  [ ] Only tested on (X)Ubuntu (15.10), but it should work on other
   GNU/Linux distribution and Mac OS X (and probably Windows), if they
   support `docopt <https://github.com/docopt/docopt>`__ and has both
   `docopt <https://github.com/docopt/docopt>`__ and
   `word\_cloud <https://github.com/amueller/word_cloud/>`__ installed.

**Unknown issues?**
~~~~~~~~~~~~~~~~~~~

`Use the issue tracker <https://github.com/Naereen/generate-word-cloud.py/issues/new>`__ to notify me of a bug!

--------------

About
-----

*Why write this script?*
~~~~~~~~~~~~~~~~~~~~~~~~

There already is a lot of `good cloud word generator online <https://duckduckgo.com/?q=cloud+word+generator&ia=web>`__, e.g. `wordle.net <http://www.wordle.net/>`__.

#. I wanted a way to visualize the major keywords of Bash and Python (my
   two `favorite programming languages <https://wakatime.com/@lbesson>`__) and of Markdown/Strapdown, reStructuredText and LaTeX (my favorite typeset documents system),
#. The original project `word\_cloud <https://github.com/amueller/word_cloud/>`__ seemed cool. And it is. Great job
   `@amueller <https://github.com/amueller/>`__ !
#. `Clouds of words are interesting <https://www.academia.edu/20224642/>`__! And Python is awesome!

Author
~~~~~~

    `Lilian Besson (Naereen) <https://github.com/Naereen/>`__.

License ? |GitHub license|
--------------------------

This plug-in is published under the terms of the `GPLv3 License <http://www.gnu.org/licenses/gpl.html>`__ (file `LICENSE.txt <LICENSE.txt>`__), © `Lilian Besson <https://GitHub.com/Naereen>`__, 2016.

|Maintenance|
|Ask Me Anything !|
|Analytics|
|made-with-python|

|ForTheBadge uses-badges|
|ForTheBadge uses-git|

|ForTheBadge built-with-love|


.. |generatewordcloud in pypi| image:: https://img.shields.io/pypi/v/generatewordcloud.svg
   :target: https://pypi.python.org/pypi/generatewordcloud
.. |PyPI version| image:: https://img.shields.io/pypi/v/generatewordcloud.svg
   :target: https://pypi.python.org/pypi/generatewordcloud/
.. |PyPI license| image:: https://img.shields.io/pypi/l/generatewordcloud.svg
   :target: https://pypi.python.org/pypi/generatewordcloud/
.. |PyPI format| image:: https://img.shields.io/pypi/format/generatewordcloud.svg
   :target: https://pypi.python.org/pypi/generatewordcloud/
.. |PyPI pyversions| image:: https://img.shields.io/pypi/pyversions/generatewordcloud.svg
   :target: https://pypi.python.org/pypi/generatewordcloud/
.. |PyPI implementation| image:: https://img.shields.io/pypi/implementation/generatewordcloud.svg
   :target: https://pypi.python.org/pypi/generatewordcloud/
.. |PyPI status| image:: https://img.shields.io/pypi/status/generatewordcloud.svg
   :target: https://pypi.python.org/pypi/generatewordcloud/
.. |generate-word-cloud example meta| image:: https://github.com/Naereen/generate-word-cloud.py/raw/master/wordcloud_meta.png
.. |generate-word-cloud example hamlet| image:: https://github.com/Naereen/generate-word-cloud.py/raw/master/wordcloud_hamlet.png
.. |generate-word-cloud example python| image:: https://github.com/Naereen/generate-word-cloud.py/raw/master/wordcloud_python.png
.. |generate-word-cloud example bash| image:: https://github.com/Naereen/generate-word-cloud.py/raw/master/wordcloud_bash.png
.. |generate-word-cloud example LaTeX| image:: https://github.com/Naereen/generate-word-cloud.py/raw/master/wordcloud_latex.png
.. |GitHub license| image:: https://img.shields.io/github/license/Naereen/generate-word-cloud.py.svg
   :target: https://github.com/Naereen/generate-word-cloud.py/blob/master/LICENSE
.. |Maintenance| image:: https://img.shields.io/badge/Maintained%3F-yes-green.svg
   :target: https://GitHub.com/Naereen/generate-word-cloud.py/graphs/commit-activity
.. |Ask Me Anything !| image:: https://img.shields.io/badge/Ask%20me-anything-1abc9c.svg
   :target: https://GitHub.com/Naereen/ama
.. |Analytics| image:: https://ga-beacon.appspot.com/UA-38514290-17/github.com/Naereen/generate-word-cloud.py/README.md?pixel
   :target: https://GitHub.com/Naereen/generate-word-cloud.py/
.. |made-with-python| image:: https://img.shields.io/badge/Made%20with-Python-1f425f.svg
   :target: https://www.python.org/
.. |ForTheBadge uses-badges| image:: http://ForTheBadge.com/images/badges/uses-badges.svg
   :target: http://ForTheBadge.com
.. |ForTheBadge uses-git| image:: http://ForTheBadge.com/images/badges/uses-git.svg
   :target: https://GitHub.com/
.. |ForTheBadge built-with-love| image:: http://ForTheBadge.com/images/badges/built-with-love.svg
   :target: https://GitHub.com/Naereen/
