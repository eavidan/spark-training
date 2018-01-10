FROM andypetrella/spark-notebook:0.9.0-SNAPSHOT-scala-2.11.8-spark-2.2.0-hadoop-2.7.2

COPY overview /opt/docker/notebooks
RUN mkdir /data
COPY ./pageviews-by-second-tsv /data