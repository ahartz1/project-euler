# Project Euler Solutions

My solutions to [Project Euler](https://projecteuler.net/archives) problems.

### Tests

There are tests associated with the solutions in each language's `tests` subfolder.


### Running the Code

Python:
 * `$ cd python`
 * Create a python virtual environment of your choice (direnv, virtualenv, etc.). Code is compatible with Python 2 and Python 3.
 * `$ pip install -r requirements.txt`
 * To run code: `$ python [filename.py]`
 * To run tests: `$ nosetests`


JavaScript:
 * `$ cd js`
 * Requires [node](https://nodejs.org/) to be installed
 * Running tests requires [npm](https://www.npmjs.com/) to be installed
   * Once installed, run `$ npm install` to install `package.json`
 * To run code: `$ node [filename.js]`
 * To run tests: `$ ./node_modules/mocha/bin/mocha tests`


PHP:
 * `$ cd php`
 * Requires PHP56
 * Tests require [composer](https://getcomposer.org/download/); download into `php` directory
   * Once installed, run `$ php composer.phar install` to install `composer.lock`
 * To run code: `$ php src/[filename.php]`
 * To run tests: `$ ./vendor/bin/phpunit`
