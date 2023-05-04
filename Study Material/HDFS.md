# HDFS

> Hdfs is a distributed file system that provides access to data across hadoop cluster 

* HDFS is open course (free)
* Can read/write terabyte of data in seconds
* HDFS makes copies 

> Regular file system vs HDFS

Regular file system     | hdfs 
--------------------    |------
51 bytes block of data  | 128 mb block of data
No access to large data | reads huge data sequentilly 


## Characteristics of hdfs 

* Fault Tolerant (replication of data)(default: 3X)
* scalable  (vertical and horizontal)
* Rack-Aware (**Rack**: Collection of machines )(Avalibility of data across other rack)
* Support for hetergenous clusters (SSD)
* Bulit for Large Datasets (splits huge file into blocks) (deafult size : 128mb)


> NameNode (Master)
* A transaction log called Edit log (record every change)
* A namespace image called an FsLmage (consist complete state of the file system namespace since the start of the NameNode)
* NameNode stores the metadata of datanode (name, permission, location etc)  
> DataNode  (slave) 
* Each DataNode contains multiple data blocks.
* These data blocks are used to store data.
* Default replication factor is 3x
> Secondary NameNode 
* The secondary NameNode merges the fsimage and the edits log files periodically and keeps edits log size within a limit

