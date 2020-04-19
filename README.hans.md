# dhubse

[English](README.md) | 简体中文

---

Docker 镜像搜索工具。
用于搜索镜像，获取镜像的标签列表。

## 支持的仓库

- Docker Hub
- ~~hardor~~
- ~~docker-registry~~

> 注：未来版本或许会支持

## 使用方法

``` bash
pip install dhubse
```

```
usage: dhubse [-h] [-m {search,tag}] [-s PAGE_SIZE] [-p PAGE]
              [--timeout TIMEOUT] [-v]
              image

Docker image search tool.

positional arguments:
  image                 image

optional arguments:
  -h, --help            show this help message and exit
  -m {search,tag}, --mode {search,tag}
  -s PAGE_SIZE, --page_size PAGE_SIZE
                        page size, default 20
  -p PAGE, --page PAGE  page number, default 1
  --timeout TIMEOUT     request timeout, default 30
  -v, --version         show program's version number and exit

unihon https://github.com/unihon
```

## 例子

```
(npy) root@unihon:~# dhubse alpine

QUERY: alpine ITEM_COUNT: 37284 PAGE_COUNT: 1865  PAGE_SIZE: 20    PAGE: 1    

IMAGE                                 DESC                     IS_OFFICIAL      STAR
------------------------------------  -----------------------  -------------  ------
alpine                                A minimal Docker ima...  True             6368
anapsix/alpine-java                   Oracle Java 8 (and 7...  False             442
byrnedo/alpine-curl                   Alpine linux with cu...  False              31
alpine/git                            A  simple git contai...  False             127
mhart/alpine-node                     Minimal Node.js buil...  False             465
yobasystems/alpine-mariadb            MariaDB running on A...  False              65
jfloff/alpine-python                  A small, more comple...  False              36
alpine/socat                          Run socat command in...  False              50
hermsi/alpine-fpm-php                 Dockerized FPM-PHP 7...  False              24
davidcaste/alpine-java-unlimited-jce  Oracle Java 8 (and 7...  False              13
hermsi/alpine-sshd                    Dockerize your OpenS...  False              30
kiasaki/alpine-postgres               PostgreSQL docker im...  False              45
frolvlad/alpine-glibc                 Alpine Docker image ...  False             239
etopian/alpine-php-wordpress          Alpine WordPress Ngi...  False              24
zenika/alpine-chrome                  Chrome running in he...  False              19
spotify/alpine                        Alpine image with `b...  False              11
mvertes/alpine-mongo                  light MongoDB contai...  False             111
gliderlabs/alpine                     Image based on Alpin...  False             181
roribio16/alpine-sqs                  Dockerized ElasticMQ...  False               8
davidcaste/alpine-tomcat              Apache Tomcat 7/8 us...  False              43

Used: 2.17023
```

```
(npy) root@unihon:~# dhubse alpine -m tag

IMAGE: alpine ITEM_COUNT: 43    PAGE_COUNT: 3     PAGE_SIZE: 20    PAGE: 1    

IMAGE_NAME       TAG       FULL_SIZE    UPDATE
---------------  --------  -----------  ------------------------
alpine:latest    latest    2.80MB       2020-03-24T06:41:01+0800
alpine:3.11.5    3.11.5    2.80MB       2020-03-24T06:40:51+0800
alpine:3.11      3.11      2.80MB       2020-03-24T06:40:46+0800
alpine:3         3         2.80MB       2020-03-24T06:40:39+0800
alpine:edge      edge      2.80MB       2020-03-20T12:36:00+0800
alpine:20200319  20200319  2.80MB       2020-03-20T12:35:38+0800
alpine:3.9.5     3.9.5     2.76MB       2020-01-24T01:42:13+0800
alpine:3.9       3.9       2.76MB       2020-01-24T01:42:08+0800
alpine:3.8.5     3.8.5     2.21MB       2020-01-24T01:41:40+0800
alpine:3.8       3.8       2.21MB       2020-01-24T01:41:36+0800
alpine:3.10.4    3.10.4    2.79MB       2020-01-24T01:41:10+0800
alpine:3.10      3.10      2.79MB       2020-01-24T01:41:04+0800
alpine:20200122  20200122  2.80MB       2020-01-23T08:40:54+0800
alpine:3.11.3    3.11.3    2.80MB       2020-01-18T10:41:00+0800
alpine:3.11.2    3.11.2    2.80MB       2019-12-25T04:40:48+0800
alpine:3.11.0    3.11.0    2.80MB       2019-12-20T08:41:21+0800
alpine:20191219  20191219  2.80MB       2019-12-20T08:40:50+0800
alpine:20191114  20191114  2.80MB       2019-11-15T06:41:11+0800
alpine:3.10.3    3.10.3    2.79MB       2019-10-22T02:41:18+0800
alpine:20190925  20190925  2.80MB       2019-09-26T06:40:50+0800

Used: 2.682024s
```