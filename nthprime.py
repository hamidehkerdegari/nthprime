#!/usr/bin/python
__author__ = "Saeid Mokaram"
__copyright__ = "Copyright 2017"
__credits__ = ["Saeid Mokaram"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Saeid Mokaram"
__email__ = "saeid.mokaram@gmail.com"
__status__ = "Production"
#==============================================

from flask import Flask, make_response, jsonify
import time

app = Flask(__name__)
primes_dict = {}    # Dictionary to store and fast-retrieve all primes for future use.


@app.route('/primes/api/v1.0/nthprime/<int:nth>', methods=['GET'])
def get_nthprime(nth):
    if nth<=0 or nth>10000000:   # Invalid input; Generating a 400 (Bad Request) JSON response.
        return make_response(jsonify({'error': 'Invalid Entry'}), 400)

    start_time = time.time()    # Measuring the elapsed time

    primes_dict[1] = 2  # First prime number.

    if nth in primes_dict:    # Check if nth prime has already calculated.
        elapsed_time = time.time() - start_time
        return jsonify({'nthprime': primes_dict[nth], 'elapsed_time': elapsed_time})
    else:
        m = max(primes_dict)    # The max calculated prime so far
        pri_tmp = int(primes_dict[m]) + 1
        for j in range(m, nth):
            k = 1
            while k <= j:   # Searching for next prime.
                if pri_tmp % primes_dict[k] == 0:
                    pri_tmp+=1
                    k=1
                else:
                    k+=1
            primes_dict[j + 1]= pri_tmp

        elapsed_time = time.time() - start_time
        return jsonify({'nthprime': primes_dict[nth], 'elapsed_time': elapsed_time})


@app.errorhandler(404)  # Handeling errors by generating a 404 (Not Found) JSON response instead of default Flask HTML error message.
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

#==============================================

if __name__ == '__main__':
    app.run(debug=False)
