#!/usr/bin/env make
# Author:	Lilian Besson
# Email:	lilian DOT besson AT ens-cachan D O T org
# Version:	1
# Date:		05/06/16
#
# Makefile for the git repository generate-word-cloud.py
# https://github.com/Naereen/generate-word-cloud.py
#
# References:
#  - http://the-hitchhikers-guide-to-packaging.readthedocs.io/en/latest/quickstart.html#lay-out-your-project
#  - https://packaging.python.org/en/latest/distributing/#uploading-your-project-to-pypi
#  - https://jeffknupp.com/blog/2013/08/16/open-sourcing-a-python-project-the-right-way/
#
###############################################################################
# Makefile for Sphinx documentation
# You can set these variables from the command line.
SPHINXOPTS    =
SPHINXBUILD   = sphinx-build
PAPER         =
BUILDDIR      = .build

# Internal variables.
PAPEROPT_a4     = -D latex_paper_size=a4
PAPEROPT_letter = -D latex_paper_size=letter
ALLSPHINXOPTS   = -d $(BUILDDIR)/doctrees $(PAPEROPT_$(PAPER)) $(SPHINXOPTS) .
# the i18n builder cannot share the environment and doctrees with the others
I18NSPHINXOPTS  = $(PAPEROPT_$(PAPER)) $(SPHINXOPTS) .

.PHONY: help clean html dirhtml singlehtml pickle json htmlhelp qthelp devhelp epub latex latexpdf text man changes linkcheck doctest gettext

###############################################################################
# Custom items
# CP = /usr/bin/rsync --verbose --compress --human-readable --progress --archive --delete --exclude=\.htaccess
# CP = scp
CP = /home/lilian/bin/CP --delete --exclude=\.htaccess --exclude=\.git --exclude=.*~
GPG = gpg --no-batch --use-agent --detach-sign --armor --quiet --yes

total:	cleanAll dochtml sendAll pypi pythonhosted_doc clean_pyc notify

local:	cleanAll dochtml notify

dochtml:	coverage html clean_pyc

pypi:	pypi_check pypi_sdist pypi_upload

pypi_check:
	python3 ./setup.py check

pypi_sdist:
	python3 ./setup.py sdist

wheel:
	python3 ./setup.py bdist_wheel --universal

pypi_upload:
	# python3 ./setup.py sdist upload --sign
	twine upload dist/*

pythonhosted_doc:
	./pythonhosted_doc.sh

notify:
	notify-send "Sphinx" "Generating documentation : done !"

notify_archive:	archive
	notify-send "Sphinx : archiving" "Generating archive : done ! (/home/lilian/generate-word-cloud.tar.gz)"

cleanAll: clean_build clean_pyc

pylint3k:
	-pylint --py3k generate-word-cloud.py > generate-word-cloud.pylint3k.txt
	pylint --py3k generate-word-cloud.py | less

pylint:
	-pylint -d broad-except generate-word-cloud.py > generate-word-cloud.pylint.txt
	pylint -d broad-except generate-word-cloud.py | less

pydoctxt:
	-pydoc generate-word-cloud > generate-word-cloud.pydoc.txt
	pydoc generate-word-cloud | less

archive:	clean_pyc
	if [ -f /home/lilian/generate-word-cloud.tar.xz ]; then mv -f /home/lilian/generate-word-cloud.tar.xz /home/lilian/Dropbox/ ; fi
	tar -Jcvf /home/lilian/generate-word-cloud.tar.xz ./
	$(GPG) /home/lilian/generate-word-cloud.tar.xz

sendAll: notify_archive send_zamok

send_zamok:
	# $(CP) -r ./ besson@zamok.crans.org:~/www/publis/generate-word-cloud.py/
	$(CP) -r ./.build/html/ besson@zamok.crans.org:~/www/publis/generate-word-cloud.py/
	$(CP) /home/lilian/generate-word-cloud.tar.xz* besson@zamok.crans.org:~/www/publis/

clean_pyc:
	rm -f *.*~ *.py[co] */*.*~ */*.py[co]
	@echo "All *.pyc (Python compiled scripts) and *.py~ (temporary copies) files have been deleted !"

clean_build:
	rm -rf _build/* .build/*

git:
	git add ./*.py ./*.rst README.md Makefile INSTALL LICENSE
	git commit -m "Auto commit with 'make git'."
	git push

stats:
	+git-complete-stats.sh | tee ./complete-stats.txt
	git wdiff ./complete-stats.txt

cloudwords:
	generate-word-cloud.py -s -m 100 -t "Words from generate-word-cloud.py - (C) 2016 Lilian Besson" *.rst *.txt *.md *.py
	generate-word-cloud.py -f -o ./cloudwords.png -m 100 -t "Words from generate-word-cloud.py - (C) 2016 Lilian Besson" *.rst *.txt *.md *.py

########################## End of custom stuffs ###############################
###############################################################################


help:
	@echo "Please use 'make <target>' where <target> is one of :"
	@echo "    html       to make standalone HTML files"
	@echo "    pypi       to upload the file on pypi (require twine)"
	@echo "    cleanAll   to XXX"
	@echo "    pylint     to XXX"
	@echo "    archive    to XXX"
	@echo "    sendAll    to upload the files on my personal website"
	@echo "    stats      to update the complete-stats.txt file"
	@echo "    cloudwords to create a small cloudwords.png file from the ./*.{rst,txt,md,py} files"
	@echo "    changes    to make an overview of all changed/added/deprecated items"
	@echo "    linkcheck  to check all external links for integrity"
	@echo "    doctest    to run all doctests embedded in the documentation (if enabled)"
	@echo "    coverage   to check which parts are documented"
	@echo "    pythonhosted_doc       to prepare the zip file to upload on pythonhosted.org (not anymore)"

clean:
	-rm -rf $(BUILDDIR)/*

coverage:
	$(SPHINXBUILD) -b coverage $(ALLSPHINXOPTS) $(BUILDDIR)/coverage
	@echo
	@echo "Build finished. The coverage pages are in $(BUILDDIR)/coverage."

html:
	$(SPHINXBUILD) -b html $(ALLSPHINXOPTS) $(BUILDDIR)/html
	@echo
	@echo "Build finished. The HTML pages are in $(BUILDDIR)/html."

dirhtml:
	$(SPHINXBUILD) -b dirhtml $(ALLSPHINXOPTS) $(BUILDDIR)/dirhtml
	@echo
	@echo "Build finished. The HTML pages are in $(BUILDDIR)/dirhtml."

singlehtml:
	$(SPHINXBUILD) -b singlehtml $(ALLSPHINXOPTS) $(BUILDDIR)/singlehtml
	@echo
	@echo "Build finished. The HTML page is in $(BUILDDIR)/singlehtml."

pickle:
	$(SPHINXBUILD) -b pickle $(ALLSPHINXOPTS) $(BUILDDIR)/pickle
	@echo
	@echo "Build finished; now you can process the pickle files."

json:
	$(SPHINXBUILD) -b json $(ALLSPHINXOPTS) $(BUILDDIR)/json
	@echo
	@echo "Build finished; now you can process the JSON files."

htmlhelp:
	$(SPHINXBUILD) -b htmlhelp $(ALLSPHINXOPTS) $(BUILDDIR)/htmlhelp
	@echo
	@echo "Build finished; now you can run HTML Help Workshop with the" \
	      ".hhp project file in $(BUILDDIR)/htmlhelp."

qthelp:
	$(SPHINXBUILD) -b qthelp $(ALLSPHINXOPTS) $(BUILDDIR)/qthelp
	@echo
	@echo "Build finished; now you can run "qcollectiongenerator" with the" \
	      ".qhcp project file in $(BUILDDIR)/qthelp, like this:"
	@echo "# qcollectiongenerator $(BUILDDIR)/qthelp/generate-word-cloud.qhcp"
	@echo "To view the help file:"
	@echo "# assistant -collectionFile $(BUILDDIR)/qthelp/generate-word-cloud.qhc"

devhelp:
	$(SPHINXBUILD) -b devhelp $(ALLSPHINXOPTS) $(BUILDDIR)/devhelp
	@echo
	@echo "Build finished."
	@echo "To view the help file:"
	@echo "# mkdir -p $$HOME/.local/share/devhelp/generate-word-cloud"
	@echo "# ln -s $(BUILDDIR)/devhelp $$HOME/.local/share/devhelp/generate-word-cloud"
	@echo "# devhelp"

epub:
	$(SPHINXBUILD) -b epub $(ALLSPHINXOPTS) $(BUILDDIR)/epub
	@echo
	@echo "Build finished. The epub file is in $(BUILDDIR)/epub."

latex:
	$(SPHINXBUILD) -b latex $(ALLSPHINXOPTS) $(BUILDDIR)/latex
	@echo
	@echo "Build finished; the LaTeX files are in $(BUILDDIR)/latex."
	@echo "Run \`make' in that directory to run these through (pdf)latex" \
	      "(use \`make latexpdf' here to do that automatically)."

latexpdf:
	$(SPHINXBUILD) -b latex $(ALLSPHINXOPTS) $(BUILDDIR)/latex
	@echo "Running LaTeX files through pdflatex..."
	$(MAKE) -C $(BUILDDIR)/latex all-pdf
	@echo "pdflatex finished; the PDF files are in $(BUILDDIR)/latex."

text:
	$(SPHINXBUILD) -b text $(ALLSPHINXOPTS) $(BUILDDIR)/text
	@echo
	@echo "Build finished. The text files are in $(BUILDDIR)/text."

man:
	$(SPHINXBUILD) -b man $(ALLSPHINXOPTS) $(BUILDDIR)/man
	@echo
	@echo "Build finished. The manual pages are in $(BUILDDIR)/man."

texinfo:
	$(SPHINXBUILD) -b texinfo $(ALLSPHINXOPTS) $(BUILDDIR)/texinfo
	@echo
	@echo "Build finished. The Texinfo files are in $(BUILDDIR)/texinfo."
	@echo "Run \`make' in that directory to run these through makeinfo" \
	      "(use \`make info' here to do that automatically)."

info:
	$(SPHINXBUILD) -b texinfo $(ALLSPHINXOPTS) $(BUILDDIR)/texinfo
	@echo "Running Texinfo files through makeinfo..."
	make -C $(BUILDDIR)/texinfo info
	@echo "makeinfo finished; the Info files are in $(BUILDDIR)/texinfo."

gettext:
	$(SPHINXBUILD) -b gettext $(I18NSPHINXOPTS) $(BUILDDIR)/locale
	@echo
	@echo "Build finished. The message catalogs are in $(BUILDDIR)/locale."

changes:
	$(SPHINXBUILD) -b changes $(ALLSPHINXOPTS) $(BUILDDIR)/changes
	@echo
	@echo "The overview file is in $(BUILDDIR)/changes."

linkcheck:
	$(SPHINXBUILD) -b linkcheck $(ALLSPHINXOPTS) $(BUILDDIR)/linkcheck
	@echo
	@echo "Link check complete; look for any errors in the above output " \
	      "or in $(BUILDDIR)/linkcheck/output.txt."

doctest:
	$(SPHINXBUILD) -b doctest $(ALLSPHINXOPTS) $(BUILDDIR)/doctest
	@echo "Testing of doctests in the sources finished, look at the " \
	      "results in $(BUILDDIR)/doctest/output.txt."
