# ``generate-word-cloud.py``
A simple Python :snake: script to generate a square wordcloud :cloud: from one (or more) text file(s).
Supports Python 2 or 3 (2.7+ or 3.4+).

![generate-word-cloud example meta](./wordcloud_meta.png)

> Based on the great [word_cloud](https://github.com/amueller/word_cloud/) module by [@amueller](https://github.com/amueller/).

----

## How to use it?
### Installation
Clone the repository, copy the [script (generate-word-cloud.py)](./generate-word-cloud.py) somewhere in your PATH (e.g., ``~/.local/bin/``):

```bash
$ wget https://raw.githubusercontent.com/Naereen/generate-word-cloud.py/master/generate-word-cloud.py
$ cp generate-word-cloud.py /path/to/a/directory/in/your/PATH/
```

> Note: The script is *not yet* available from [pip](http://www.pip-installer.org/). It might be, soon.

### Usage
#### Help:
```bash
$ generate-word-cloud.py --help
```
#### From one or two files
Generate a wordcloud from two `txt` files in the current directory, save it to `wordcloud_txt.png`.

```bash
$ generate-word-cloud.py -o ./wordcloud_txt.png ./file1.txt ./file2.txt
```

Generate a wordcloud from the textfile `hamlet.txt` (~ 8000 lines), saving to `hamlet.png`:

```bash
$ generate-word-cloud.py -o ./hamlet.png ./hamlet.txt
```
![generate-word-cloud example hamlet](./wordcloud_hamlet.png)

(It should work on pretty big text files without any issue)

----

## Other examples
### From a lot of Python scripts (~ 200) :snake:
![generate-word-cloud example python](./wordcloud_python.png)

### From a lot of Bash scripts (~ 150) :shell:
![generate-word-cloud example bash](./wordcloud_bash.png)

### From a lot of LaTeX files (~ 180) :eggplant:
![generate-word-cloud example LaTeX](./wordcloud_latex.png)

### :art: Meta example
Generate a wordcloud from the [README.md](./README.md) and [generate-word-cloud.py](./generate-word-cloud.py) files **of this very project**, save it to `wordcloud_meta.png`!

```bash
$ generate-word-cloud.py -o ./wordcloud_meta.png ./*.md ./*.py
```
![generate-word-cloud example meta](./wordcloud_meta.png)

----

## Features
- [x] Support one or more input files, will skip the one it fails to find or fails to read,
- [x] Customize output file, won't be overwritten (except with `-f` flag),
- [x] Nice command line interface ([argparse](https://docs.python.org/2.7/library/argparse.html) powered),
- [x] Has a command line option for every important parameter (max nb of words, width, height etc).

----

## :page_with_curl: Complete documentation (`--help`)
```
$ generate-word-cloud.py -h | --help
usage: generate-word-cloud.py [-h] [-v] [-s] [-f] [-o OUTFILE] [-t TITLE]
                              [-m MAX] [-w WIDTH] [-H HEIGHT]
                              INFILE [INFILE ...]

optional arguments:
  -h, --help            show this help message and exit
  -v, --version         show program's version number and exit

  -s, --show            show the image but do not save it
  -f, --force           force to write the image, even if present (default is to ask before overwriting an existing file)
  -o OUTFILE, --outfile OUTFILE
                        filename for the generated image, default is 'wordcloud.png'
  -t TITLE, --title TITLE
                        title for the image, default is None
  -m MAX, --max MAX     max number of words to display on the cloud word
  -w WIDTH, --width WIDTH
                        width of the generate image
  -H HEIGHT, --height HEIGHT
                        height of the generate image
  INFILE                a text file to read
```

----

## :memo: TODO?
- [x] Start it, from [this example](https://github.com/amueller/word_cloud/blob/master/examples/simple.py),
- [x] Run it on some interesting examples, embed them here,
- [ ] Check on weird encodings?
- [ ] Test it against :closed_book: VERY large files (million of line) ?,
- [ ] Test it against :books: LOTS of files (several thousands) ?,
- [ ] Write a small article about it for [my blog](http://perso.crans.org/besson/).

### :bug: Knows issues
- [ ] Input filenames with spaces in their name are seen as several files. I will try to fix it asap!
- [ ] Only tested on Ubuntu (15.10).

### :bug: Unknown issues?
> [Use the issue tracker](https://github.com/Naereen/generate-word-cloud.py/issues/new) to notify me of a bug.

----

## About
### Why?
- I wanted a way to visualize the major keywords of Bash and Python (my two [favorite programming languages](https://wakatime.com/@lbesson)) and of Markdown/Strapdown, reStructuredText and LaTeX (my favorite typeset documents system),
- The original project [word_cloud](https://github.com/amueller/word_cloud/) seemed cool. And it is. Great job [@amueller](https://github.com/amueller/) :clap: !
- [Clouds of words are interesting](https://www.academia.edu/20224642/)!

### Author
> [Lilian Besson (Naereen)](https://github.com/Naereen/).

### :scroll: [License](./LICENSE)
> [GPLv3 License](http://www.gnu.org/licenses/gpl.html).

[![Analytics](https://ga-beacon.appspot.com/UA-38514290-17/github.com/Naereen/generate-word-cloud.py/README.md?pixel)](https://github.com/Naereen/generate-word-cloud.py/)
