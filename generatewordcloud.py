#!/usr/bin/env python2
# -*- coding:utf8 -*-
"""
A simple Python script to generate a square wordcloud from a file or a bunch of files.
https://github.com/Naereen/generate-word-cloud.py

Requires https://github.com/amueller/word_cloud/

.. note:: Copyright 2016 Lilian Besson
.. warning:: License GPLv3.

---

Examples
--------
$ generate-word-cloud.py --help
Gives help.

$ generate-word-cloud.py ./hamlet.txt
Generate a wordcloud from the textfile hamlet.txt, saving to hamlet.png.

$ generate-word-cloud.py -o wordcloud.png ./*.txt
Generate a wordcloud from all the txt files in the current directory, save it to wordcloud.png.

------

.. sidebar:: Last version?

   Take a look to the latest version at https://github.com/Naereen/generate-word-cloud.py

.. note::

   This program is free software: you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation, either version 3 of the License, or
   (at your option) any later version.

   generate-word-cloud.py is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

   See the GNU General Public License for more details.
   You should have received a copy of the GNU General Public License v3 along with generate-word-cloud.py.
   If not, see <http://perso.crans.org/besson/LICENSE.html>.
"""

from __future__ import print_function  # Python 2/3 compatible

from sys import exit, argv
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from os import path
# import argparse  # DONE : switch to docopt (https://github.com/docopt/docopt)
from docopt import docopt

try:
    try:
        from ansicolortags import printc
    except ImportError as e:
        print("Optional dependancy (ansicolortags) is not available, using regular print function.")
        print("  You can install it with : 'pip install ansicolortags' (or sudo pip)...")
        from ANSIColors import printc
except ImportError:
    printc = print

# Options
version = '0.3'
show = False


def readfiles(filenames):
    """ Return the content of each file, concatenated as one big string.

    - Path could be relative or absolute, but nothing fancy is done here.
    """
    text = ""
    # Read the whole text for each file
    for filename in filenames:
        try:
            text += open(filename, 'r').read()
            text += r"\n"
        except Exception as e:
            printc("<ERROR>Error, exception: <reset>{}.".format(e))
            printc("<red>Skipping file <black>'{}'<reset>...".format(filename))
    # return "\n".join(open(filename, 'r').read() for filename in filenames)
    return text


def generate(text, max_words=200, width=800, height=600):
    """ Generate a word cloud image from the given text (one huge string). """
    # Take relative word frequencies into account, lower max_font_size
    # https://amueller.github.io/word_cloud/generated/wordcloud.WordCloud.html#wordcloud.WordCloud
    max_words = int(max_words) if max_words is not None else  200
    width     = int(width)     if width     is not None else  800
    height    = int(height)    if height    is not None else  600
    wc = WordCloud(max_font_size=40,
                   relative_scaling=.5,
                   max_words=max_words,
                   width=width,
                   height=height
                   )
    return wc.generate(text)


def makeimage(wordcloud,
              outname='wordcloud.png', title='Word cloud', show=False, force=False):
    """ Display or save the wordcloud as a image. """
    # Display the generated image:
    try:
        # 2. the matplotlib way:
        plt.figure()
        plt.imshow(wordcloud)
        plt.axis("off")
        if title:
            printc("<magenta>Using title<reset> <blue>'{}'<reset>.".format(title))
            plt.title(title)
        if show:
            printc("<green>Showing the generated image...<reset>")
            plt.show()
        else:
            printc("<green>Saving the generated image<reset> to <blue>'{}'<reset>...".format(outname))
            if (not force) and path.exists(outname):
                erase = raw_input("The outfile '{}' already exists, should I erase it ?  [y/N]".format(outname))
                if erase == 'y':
                    plt.savefig(outname)
                else:
                    printc("<magenta>Not erasing it...<reset>")
                    printc("<green>Showing the generated image...<reset>")
                    plt.show()
            else:
                if force:
                    printc("<WARNING> -f or --force has been used, overwriting the image '{}' <red>without<reset> asking you...".format(outname))
                plt.savefig(outname)
    except Exception as e:
        printc("<ERROR> Error, exception<reset>: {}".format(e))
        # 1. The pil way (if you don't have matplotlib)
        printc("<WARNING> Something went wrong with matplotlib, switching to PIL backend... (just showing the image, <red>not<reset> saving it!)")
        image = wordcloud.to_image()
        image.show()
    return True


#: Help for the cli
full_docopt_text = """
generate-word-cloud.py

Usage:
  generate-word-cloud.py [-s | --show] [-f | --force] [-o OUTFILE | --outfile=OUTFILE]
                         [-t TITLE | --title=TITLE] [-m MAX | --max=MAX]
                         [-w WIDTH | --width=WIDTH] [-H HEIGHT | --height=HEIGHT]
                         INFILE...
  generate-word-cloud.py [-h | --help]
  generate-word-cloud.py [-v | --version]

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


A simple Python script to generate a (square) wordcloud from a file INFILE (or bunch of files INFILE...).
Requires https://github.com/amueller/word_cloud/ (installable with pip).

Examples:
$ generate-word-cloud.py --help
Gives this help.

$ generate-word-cloud.py ./hamlet.txt
Generate a wordcloud from the textfile hamlet.txt, saving to 'wordcloud.png' (default).

$ generate-word-cloud.py -o mywordcloud.png ./*.txt
Generate a wordcloud from all the txt files in the current directory, save it to 'mywordcloud.png'.

Copyright 2016 Lilian Besson (License GPLv3)
generate-word-cloud.py is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
"""


def main(argv):
    """ Use the arguments of the command line. """
    # Use the arg parser
    args = docopt(full_docopt_text, argv=argv, version="generate-word-cloud.py v{}".format(version))
    # printc("<magenta>Arguments: {} <reset>".format(args))  # DEBUG

    # Read the files
    printc("<green>Reading the files<reset>, from: <blue>{}<reset>.".format(args['INFILE']))
    text = readfiles(args['INFILE'])
    # Decide where to save it
    outname = args['--outfile'] if args['--outfile'] else 'wordcloud.png'
    # Generate the wordcloud
    # print("Making a wordcloud from this text:\n", text)  # DEBUG
    wordcloud = generate(text,
                         max_words=args['--max'],
                         width=args['--width'],
                         height=args['--height']
                         )
    # Finally, saving the image
    printc("<green>Making the image<reset> and saving it to <blue>{}<reset>.".format(outname))
    makeimage(wordcloud,
              outname=outname, title=args['--title'],
              force=args['--force'], show=args['--show']
              )
    return 0


if __name__ == "__main__":
    exit(int(main(argv[1:])))

# End of generate-word-cloud.py
