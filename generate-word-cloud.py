#!/usr/bin/env python2
# -*- coding:utf8 -*-
"""
A simple Python script to generate a square wordcloud from a file or a bunch of files.


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

   Take a look to the latest version at https://bitbucket.org/lbesson/bin/src/master/generate-word-cloud.py

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

from __future__ import print_function
from sys import exit, argv
import argparse
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from os import path

# Options
version = '0.1'
show = False


def readfiles(filenames):
    """ Return the content of each file, concatenated as one big string.

    - Path should be relative or absolute, but nothing fancy is done here.
    """
    # d = path.dirname(__file__)
    text = ""
    # Read the whole text for each file
    for filename in filenames:
        try:
            # text += open(path.join(d, 'constitution.txt')).read()
            text += open(filename, 'r').read()
            text += r"\n"
        except Exception as e:
            print("Error, exception:", e)
            print("Skipping file '%s'..." % filename)
    # return "\n".join(open(filename, 'r').read() for filename in filenames)
    return text


def generate(text, max_words=200, width=800, height=600):
    """ Generate a word cloud image from the given text (one huge string). """
    # wordcloud = WordCloud().generate(text)
    # take relative word frequencies into account, lower max_font_size
    # https://amueller.github.io/word_cloud/generated/wordcloud.WordCloud.html#wordcloud.WordCloud
    wc = WordCloud(max_font_size=40,
                   relative_scaling=.5,
                   max_words=max_words,
                   width=width,
                   height=height
                   )
    # wordcloud = wc.generate(text)
    return wc.generate(text)


def makeimage(wordcloud,
              outname='wordcloud.png', title='Word cloud', show=False, force=False):
    """ Display or save the wordcloud as a image. """
    try:
        # Display the generated image:
        # the matplotlib way:
        # plt.imshow(wordcloud)
        # plt.axis("off")
        plt.figure()
        plt.imshow(wordcloud)
        plt.axis("off")
        if title:
            print("Using title '%s'." % title)
            plt.title(title)
        if show:
            print("Showing the generated image...")
            plt.show()
        else:
            print("Saving the generated image to '%s'..." % outname)
            if (not force) and path.exists(outname):
                erase = raw_input("The outfile '%s' already exists, should I erase it ?  [y/N]")
                if erase == 'Y':
                    plt.savefig(outname)
                else:
                    print("Not erasing it...")
                    print("Showing the generated image...")
                    plt.show()
            else:
                if force:
                    print("-f or --force has been used, overwriting the image '%s' without asking you..." % outname)
                plt.savefig(outname)
    except Exception as e:
        print("Error, exception:", e)
        # The pil way (if you don't have matplotlib)
        print("Something went wrong with matplotlib, switching to PIL backend... (just showing the image, not saving it)")
        image = wordcloud.to_image()
        image.show()
    return True


#: Help for the cli
description = """
A simple Python script to generate a square wordcloud from a file or bunch of files.
Requires https://github.com/amueller/word_cloud/

Examples:
$ generate-word-cloud.py --help
Gives this help.

$ generate-word-cloud.py ./hamlet.txt
Generate a wordcloud from the textfile hamlet.txt, saving to hamlet.png.

$ generate-word-cloud.py -o mywordcloud.png ./*.txt
Generate a wordcloud from all the txt files in the current directory, save it to mywordcloud.png.
"""

epilog = """
Copyright 2016 Lilian Besson (License GPLv3)
generate-word-cloud.py is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
"""


def main(argv):
    """ Use the arguments of the command line. """
    # infiles = []
    # title = None
    # We use the argparse std library
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawTextHelpFormatter,
        description=description,
        epilog=epilog,
        prefix_chars='-+'
    )
    parser.add_argument('-v', '--version', action='version', version='%(prog)s '+version)

    group = parser.add_argument_group()
    group.add_argument('-s', '--show', action='store_true', default=False,
                       help="show the image but do not save it")
    group.add_argument('-f', '--force', action='store_true', default=False,
                       help="force to write the image, even if present (default is to ask before overwriting an existing file)")
    group.add_argument('-o', '--outfile', default=None,
                       help="filename for the generated image, default is 'wordcloud.png'")
    group.add_argument('-t', '--title', default=None,
                       help="title for the image, default is None")
    group.add_argument('-m', '--max', action='store', default=100,
                       help="max number of words to display on the cloud word")
    group.add_argument('-w', '--width', action='store', default=400,
                       help="width of the generate image")
    group.add_argument('-H', '--height', action='store', default=300,
                       help="height of the generate image")

    # The rest of the arguments are INFILE
    group.add_argument('infiles', metavar='INFILE', type=str, nargs='+',
                       help='a text file to read')

    # Use the arg parser
    args = parser.parse_args(argv)
    print("Args:", args)

    # Read the files
    print("Reading the files, from:", args.infiles)  # XXX
    text = readfiles(args.infiles)
    # Decide where to save it
    if args.outfile:
        outname = args.outfile
    else:
        outname = 'wordcloud.png'
    # Generate the wordcloud
    # print("Making a wordcloud from this text:\n", text)  # XXX
    wordcloud = generate(text,
                         max_words=int(args.max), width=int(args.width), height=int(args.height)
                         )
    # Finally, saving the image
    print("Making the image and saving it to", outname)  # XXX
    makeimage(wordcloud,
              outname=outname, title=args.title,
              force=args.force, show=args.show
              )
    return 0


if __name__ == "__main__":
    exit(int(main(argv[1:])))

# End of generate-word-cloud.py
