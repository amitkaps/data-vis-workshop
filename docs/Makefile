SORUCES=$(wildcard ../notebooks/*.ipynb)
TARGETS=$(SORUCES:.ipynb=.html)
HTML=$(shell echo $(TARGETS) | sed 's/\.\.\/notebooks\///g')

push: $(TARGETS)
	git add $(HTML)
	git commit -m "update docs"
	git push
	touch push


build: $(TARGETS)

%.html: %.ipynb
	jupyter nbconvert $<
	cp $@ ./$(nodir $@)

clean:
	-rm $(TARGETS) push

loop:
	@while sleep 10; do make; done
