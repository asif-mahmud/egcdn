egcdn
================

CDN development library utilizing `RabbitMQ` RPC and `nginx`.

This project provides a process pool (a pool of processes) where
every process takes in a `Queue` message from `com.eg.cdn` `Route`,
then parses it, then saves it in a file which will be served by a
content delivery server like `nginx`.

It is only a bridge between web application and the cdn server of
choice. by using pluggable processors one can use any kind of cdn
(Filesystem based, Amazon AWS, CloudFlare etc) to store and deliver
his static contents.

Lets see what it does -
```
             ----->                  ----->        ---->
            /                       /             /
Web Clients ------> Web Application ------> egcdn -----> Storage - 
            \                       \             \               |
             ----->                  ----->        ---->          |
                                                                  |
                    <---------------                       <------|
Web Clients         <---------------    CDN Server         <------|
                    <---------------                       <------|


```