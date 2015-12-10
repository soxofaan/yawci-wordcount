
INPUT_PATH := yawci-wordcount/input/hamlet.txt
OUTPUT_PATH := yawci-wordcount/output/java

.PHONY: default
default:
	${MAKE} run
	${MAKE} output-head

### Building ###

.PHONY: build
build: wc.jar

wc.jar: WordCount.java
	mkdir -p build
	HADOOP_CLASSPATH=${JAVA_HOME}/lib/tools.jar hadoop com.sun.tools.javac.Main WordCount.java -d build $^
	jar cf $@ -C build .

.PHONY: clean
clean:
	rm -fr wc.jar build/

### Running ###

.PHONY: clean-run
clean-run:
	hadoop fs -rm -R -f ${OUTPUT_PATH}

.PHONY: run
run: build clean-run
	hadoop jar wc.jar WordCount ${INPUT_PATH} ${OUTPUT_PATH}

.PHONY: output-head
output-head:
	hadoop fs -cat ${OUTPUT_PATH}/* | head
