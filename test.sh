# python3 -m unittest discover -s src
# code from putting tests in src

# run the test by running ./test.sh in the base location of the file (static-site-generator)

PYTHONPATH=$PYTHONPATH:src python3 -m unittest discover -s tests
