# -*- coding: UTF-8 -*-
"""A thread pool is an object that maintains a pool of worker threads to perform
time consuming operations in parallel. It assigns jobs to the threads
by putting them in a work request queue, where they are picked up by the
next available thread. This then performs the requested operation in the
background and puts the results in another queue.

The thread pool object can then collect the results from all threads from
this queue as soon as they become available or after all threads have
finished their work. It's also possible, to define callbacks to handle
each result as it comes in.

.. note::
    This module is regarded as an extended example, not as a finished product.
    Feel free to adapt it too your needs.

"""
# Release info for Threadpool

name = 'threadpool'
version = '1.3.0'
description = 'Easy to use object-oriented thread pool framework'
keywords = 'threads, design pattern, thread pool'
author = 'Christopher Arndt'
author_email = 'chris@chrisarndt.de'
url = 'http://chrisarndt.de/projects/threadpool/'
download_url = url + 'download/'
license = "MIT license"
long_description = __doc__
platforms = "POSIX, Windows, MacOS X"
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Developers',
  'License :: OSI Approved :: Python Software Foundation License',
  'Operating System :: Microsoft :: Windows',
  'Operating System :: POSIX',
  'Operating System :: MacOS :: MacOS X',
  'Programming Language :: Python :: 2',
  'Programming Language :: Python :: 3',
  'Topic :: Software Development :: Libraries :: Python Modules'
]
