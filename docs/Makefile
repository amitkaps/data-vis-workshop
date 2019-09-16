SORUCES=$(wildcard ../notebooks/*.ipynb)
IPYNB=$(shell echo $(SORUCES) | sed 's/\.\.\/notebooks\///g')
TARGETS=$(IPYNB:.ipynb=.html)
DEST=../docs/

push: $(TARGETS)
	cd .. && git add docs && cd -
	git commit -m "update docs"
	git push
	#rsync -avz *.html $(REMOTE_LOCATION)
	touch push


build: $(TARGETS)

$(DEST)%.html: %.ipynb
	jupyter nbconvert $< --output $@

clean:
	-rm $(TARGETS) push

loop:
	@while sleep 2; do make; done
