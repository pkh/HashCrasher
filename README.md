HashCrasher
===========

#### Python-Flavored Password Recovery

A Python tool to recover a variety of hashes. As of 0.0.1 limited to numerical passwords of 1-6 characters using a keyspace of 0-9. HashCrasher does not _YET_ support hashes with salt.

The following hash types are currently supported:

- MD5
- SHA1
- SHA224
- SHA256
- SHA384
- SHA512

To view usage instructions, run the following command from your terminal: 

`$ python hashcrasher.py -h`


HashCrasher was created primarily to be an exercise in learning Python syntax and conventions. However, hopefully a useful tool also emerges.