# NthPrime WebAPI
- Finding the 'n'th prime number.
- version: 1.2.1
- author: Saeid Mokaram
- copyright: Copyright 2017
- credits: Saeid Mokaram
- license: GPL
- maintainer: Saeid Mokaram
- email: saeid.mokaram@gmail.com
- status: Production

## Description
This repository contains a Python-based web service/API for calculating the nth prime number.
In the current production, the application is intended to be executed on a single-core embedded device like a Raspberry Pi, although it can also be executed on different Linux-based OSs.

The application was developed in PyCharm (Community Edition 2016.3.1) on an Ubuntu 16.04 LTS 64-Bit.
The application can be called with a single argument, 'n' (which can be any integer up to 10 million), and will return the 'n'th prime number.

The application implements a REST service that will reply the nth prime and elapsed_time (as a JSON data) via an HTTP GET method with a URL format of:

    http://[hostname]:5000/primes/api/v1.2/nthprime/[n]

example for running on local host:

    http://127.0.0.1:5000/primes/api/v1.2/nthprime/152

JSON response format:

    {
      "elapsed_time": [float], 
      "nthprime": [int]
    }

## System requirements:
- Linux OS.
- Python2/3
- Flask (a micro web framework in Python): to create a web application.

# To run this application:
Install Flask: http://flask.pocoo.org/docs/0.12/installation/

Set permissions:

    $ chmod a+x nthprime.py

Run application:
    
    $ ./nthprime.py~/anaconda3/bin/python nthprime.py 
      * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

Launch your web browser (FireFox) and type for example:

    http://127.0.0.1:5000/primes/api/v1.2/nthprime/152

You will receive a JSON response of:
    
    elapsed_time:    0.007896661758422852
    nthprime:    881

## The implementation approach:
Fact: Any number that is not prime is divisible by one prime that comes before its square root in the number series.
Given n primes, we just need to check the divisibility of the numbers after the nth prime with all the n primes until finding the n+1th prime.

For optimization purposes, all the calculated primes are stored in a Dictionary to be used for future queries.

## Further improvements:
All the calculated primes can be saved in a file for future use. So after re-running the application or transferring the application to other systems/servers, there will be no need for recalculating them.

Finding the next prime requires comparing every new number with all the previously found primes. This process can be parallelized on a system with multiple cores (CPUs) by first, getting the number of CPUs on the local machine and then, dividing the search space of all the previously found primes. In the case that non of the processing threads find the number divisible by any of the previous primes, we have found the next prime number.
