#!/usr/bin/python
__author__ = "Saeid Mokaram"
__copyright__ = "Copyright 2017"
__credits__ = ["Saeid Mokaram"]
__license__ = "GPL"
__version__ = "1.1.1"
__maintainer__ = "Saeid Mokaram"
__email__ = "saeid.mokaram@gmail.com"
__status__ = "Production"
# ==============================================

from flask import Flask, make_response, jsonify
import time, math, multiprocessing

APP_REST = Flask(__name__)
PRIMES_DICT = {}    # Dictionary to store and fast-retrieve all primes for future use.


@APP_REST.route('/primes/api/v1.2/nthprime/<int:nth>', methods=['GET'])
def get_nthprime(nth):
    if nth <= 0 or nth > 10000000:   # Invalid input; Generating a 400 (Bad Request) JSON response.
        return make_response(jsonify({'error': 'Invalid Entry'}), 400)

    start_time = time.time()    # Measuring the elapsed time

    PRIMES_DICT[1] = 2  # First prime number.
    PRIMES_DICT[2] = 3  # Second prime number.

    if nth in PRIMES_DICT:    # Check if nth prime has already calculated.
        elapsed_time = time.time() - start_time
        return jsonify({'nthprime': PRIMES_DICT[nth], 'elapsed_time': elapsed_time})
    else:
        max_calced_prime = max(PRIMES_DICT)    # The max calculated prime so far
        pri_tmp = int(PRIMES_DICT[max_calced_prime]) + 2
        for i in range(max_calced_prime, nth):
            k = 1
            while PRIMES_DICT[k] <= math.sqrt(pri_tmp):   # Searching for next prime.
                if pri_tmp % PRIMES_DICT[k] == 0:
                    pri_tmp += 2
                    k = 1
                else:
                    k += 1
            PRIMES_DICT[i + 1]= pri_tmp
            pri_tmp += 2

        elapsed_time = time.time() - start_time
        return jsonify({'nthprime': PRIMES_DICT[nth], 'elapsed_time': elapsed_time})


@APP_REST.errorhandler(404)  # Handeling errors by generating a 404 (Not Found) JSON response instead of default Flask HTML error message.
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

# ==============================================

if __name__ == '__main__':
    APP_REST.run(host='0.0.0.0', debug=False)