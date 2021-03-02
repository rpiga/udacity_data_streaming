1. How did changing values on the SparkSession property parameters affect the throughput and latency of the data?
I found that a good way to evaluate how sparkstream is performing, is by checking the inputRowsPerSecond and processedRowsPerSecond

2021-03-02 16:30:08 INFO  MicroBatchExecution:54 - Streaming query made progress: {
  "id" : "a872c5a4-5fde-46e2-be3d-93eea00d0637",
  "runId" : "3ea362a8-9208-4857-a60a-e75046f11837",
  "name" : "counts",
  "timestamp" : "2021-03-02T16:30:04.329Z",
  "batchId" : 21,
  "numInputRows" : 99,
  "inputRowsPerSecond" : 24.868123587038433,
  "processedRowsPerSecond" : 24.830699774266364,
  "durationMs" : {
    "addBatch" : 3923,
    "getBatch" : 4,
    "getOffset" : 2,
    "queryPlanning" : 38,
    "triggerExecution" : 3987,
    "walCommit" : 20
  },
  
  ...
  ...
  
So the change of SparkSession properties will affect those figures, resulting in an higher or lower processing rate, as well as latency.

2. What were the 2-3 most efficient SparkSession property key/value  pairs? Through testing multiple variations on values, how can you tell  these were the most optimal?

First one I directly tried is the option "maxOffsetsPerTrigger".
With value 100, the processedRows are:
    "numInputRows" : 99,
    "inputRowsPerSecond" : 24.868123587038433,
    "processedRowsPerSecond" : 24.830699774266364
    
with 1000
    "numInputRows" : 999,
    "inputRowsPerSecond" : 158.11965811965814,
    "processedRowsPerSecond" : 165.2605459057072
with 5000
  "numInputRows" : 4954,
  "inputRowsPerSecond" : 246.17372291790898,
  "processedRowsPerSecond" : 533.433832238613,
 
I tried up to the value of 10000, and results were pretty good.. but it should be checked in a system with a larger amount of data if the processing capability of the application is able to cope with the input rate.

Other properties that could help, in a more complex production system, could be the variation of the paralellism and the increase of allocated memory.
For the parallellism, we can increase the number of cores used
spark.conf.set('spark.executor.cores', '3')
spark.conf.set('spark.cores.max', '3')
or
spark.default.parallelism (this one is more for transfromation jobs)

Memory can be set ie. with the following conf options:
spark.conf.set("spark.executor.memory", '8g')
spark.conf.set("spark.driver.memory", '8g')

