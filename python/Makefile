
INPUT_PATH := yawci-wordcount/input/hamlet.txt
OUTPUT_PATH := yawci-wordcount/output/python

# TODO: Not sure at the moment how finding the hadoop-streaming can be improved
HADOOP_STREAMING_JAR := ${HADOOP_HOME}/share/hadoop/tools/lib/hadoop-streaming*.jar

.PHONY: default
default:
	${MAKE} run
	${MAKE} output-head

### Running ###

.PHONY: clean-run
clean-run:
	hadoop fs -rm -R -f ${OUTPUT_PATH}

.PHONY: run
run: clean-run
	hadoop jar ${HADOOP_STREAMING_JAR} \
		-D mapred.reduce.tasks=4 \
		-input ${INPUT_PATH} -output ${OUTPUT_PATH} \
		-mapper wcmap.py -reducer wcreduce.py \
		-file wcmap.py -file wcreduce.py

.PHONY: test
test:
	echo 'Foo bar foo baz:foo bar BAR baz foo.' | python wcmap.py | sort | python wcreduce.py

.PHONY: output-head
output-head:
	hadoop fs -cat ${OUTPUT_PATH}/* | head
