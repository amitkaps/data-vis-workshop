SORUCES=$(wildcard ../notebooks/*.ipynb)
TARGETS=$(IPYNB:.ipynb=.html)
HTML=$(shell echo $(TARGETS) | sed 's/\.\.\/notebooks\///g')
SOURCEDIR=../notebooks

push: $(TARGETS)
	cd .. && git add docs && cd -
	git commit -m "update docs"
	git push
	#rsync -avz *.html $(REMOTE_LOCATION)
	touch push


build: $(TARGETS)

%.html: %.ipynb
	jupyter nbconvert $(SOURCEDIR)/$<

clean:
	-rm $(TARGETS) push

loop:
	@while sleep 60; do make; done
