# Project Euler Solutions

My solutions to [Project Euler](https://projecteuler.net/archives) problems.

### Tests

There are tests associated with each solution in the `tests` folder.


### Running the Code

Python:
 * Create a python3 virtual environment of your choice (direnv, virtualenv, etc.)
 * `$ pip install -r requirements.txt`
 * To run code: `$ python [filename.py]`
 * To run tests: `$ nosetests`


JavaScript:
 * Requires [node](https://nodejs.org/) to be installed
 * Running tests requires [npm](https://www.npmjs.com/) to be installed
   * Once installed, run `$ npm install` to install `package.json`
 * To run code: `$ node [filename.js]`
 * To run tests: `$ ./node_packages/mocha/bin/mocha`


PHP:
 * Requires PHP56
 * Requires [PHPUnit](https://phpunit.de/)
 * To run code: `$ php [filename.php]`
 * To run individual tests: `$ phpunit --bootstrap [filename.php] [test_filename.php]`
