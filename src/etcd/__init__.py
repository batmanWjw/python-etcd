#!/usr/bin/python
# -*- coding: utf-8 -*-

from etcd import *
from .client import Client
from .lock import Lock

_log = logging.getLogger(__name__)

# Prevent "no handler" warnings to stderr in projects that do not configure
# logging.
try:
    from logging import NullHandler
except ImportError:
    # Python <2.7, just define it.
    class NullHandler(logging.Handler):
        def emit(self, record):
            pass
_log.addHandler(NullHandler())

client = None


def init(hosts='127.0.0.1:2379'):
    global client

    if not client:
        if isinstance(hosts, basestring):
            hosts = hosts.split(',')
        hosts = tuple([host.strip().split(':') for host in hosts])
        for host in hosts:
            host[1] = int(host[1])
        client = Client(hosts, read_timeout=30, allow_reconnect=True)


def get_client():
    return client
