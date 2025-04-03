![GitHub last commit (branch)](https://img.shields.io/github/last-commit/Dr4k3z/enigma/main)

[![Unit-testing](https://github.com/Dr4k3z/enigma/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/Dr4k3z/enigma/actions/workflows/main.yml)

# Python Enigma
This repo contains a Python implementation of the Enigma Machine, as described by Professor [Mike Pound](https://www.nottingham.ac.uk/research/beacons-of-excellence/future-food/meet-the-team/michael-pound/index.aspx) in this [video](https://www.youtube.com/watch?v=RzWB5jL5RX0). 

The code structure and the test cases have been ported from Java to Python; for the original work, please see [this repo](https://github.com/mikepound/enigma). 

## Setup
Download the code or clone the repo. Inside the folder, you may find a `setup.cfg` file, so that the package is installable with `pip`.

Run `pip install -e .` to configure the package in your current python enviroment. Then you should be able to just import the package, as in `import enigma`. To check your configuration, you can ran the unit tests, provided you have installed `pytest`.

Inside the `test` folder, just type `pytest` and you shall see all the tests being passed. Unit testing is part of the CI/CD workflow. To see if the current's version is passing the tests, refer to the Github Actions page. 


## Example
In the `example.py` file, you can find a basic example of how the encryption machine work. 

At the moment, the decryption mechanism is still missing: I hope to start working on it soon! If you wish to contribute, consider opening a pull request :)

