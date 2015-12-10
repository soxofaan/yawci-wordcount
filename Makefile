

.PHONY: default
default:
	echo hello world

.PHONY: input
input: input/hamlet.txt
	hadoop fs -ls -R yawci-wordcount

.PHONY: clean-input
clean-input:
	rm -fr input

input/hamlet.txt:
	mkdir -p $(shell dirname $@)
	wget -O $@ http://www.gutenberg.org/ebooks/1524.txt.utf-8
	hadoop fs -mkdir -p $(shell dirname yawci-wordcount/$@)
	hadoop fs -put $@ yawci-wordcount/$@
