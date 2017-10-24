
egcdn
================

A Glue application between CDN servers and Web Applications.

This application builds a glue layer between a Web Applications and 
any CDN server utilizing `RabbitMQ` RPC and `nginx`.

This project provides a process pool (a pool of processes) where
every process takes in a `Queue` message from `com.eg.cdn`( customizable 
by environmental variable) `Route`, then parses it, then saves it 
in a file which will be served by a content delivery server like `nginx`.

It is only a bridge between web application and the cdn server of
choice. by using pluggable processors one can use any kind of cdn
(Filesystem based, Amazon AWS, CloudFlare etc) to store and deliver
his static contents.

Lets see what it does -

<img src="https://github.com/asif-mahmud/egcdn/egcdn/data/Logical-Representation.jpg" alt="Logical presentation" width="512px">

This way one can completely decouple file reponse handling from web
services or web applications and grow up his file extension support
with optiomization kept in mind.

It is not a CDN server, it just saves the raq data from web application 
and let a dedicated server handle the rest of it.

The best part of it is the processors are easily customizable. One 
can write his own pluggable worker and be done with it.

Processors will be picked up by mimetype detected by `libmagic`
from raw data. See the `API` section for more details.


## Installation

Download the git repository or any release with a version tag.
Unzip it and run - `pip install .` to install it like any other
python package.


## Version History