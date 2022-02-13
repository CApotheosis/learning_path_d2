### Naming convention for pytest files:
- Test files should be named test_something.py or something_test.py.
- Test methods and functions should be named test_something.
- Test classes should be named Test_Something.

### Possible outcomes of a test function:
- PASSED (.): The test ran successfully.
- FAILED (F): The test did not run successfully (or XPASS + strict).
- SKIPPED (s): The test was skipped. You can tell pytest to skip a test by using either the @pytest.mark.skip() or pytest.mark.skipif() decorators, discussed in Skipping Tests, on page 34.
- xfail (x): The test was not supposed to pass, ran, and failed. You can tell pytest that a test is expected to fail by using the @pytest.mark.xfail() decorator,
discussed in Marking Tests as Expecting to Fail, on page 37.
- XPASS (X): The test was not supposed to pass, ran, and passed.
- ERROR (E): An exception happened outside of the test function, in either a fixture, discussed in Chapter 3, pytest Fixtures, on page 49, or in a hook function, discussed in Chapter 5, Plugins, on page 95.

### Running one tests:
```
pytest -v tasks/test_four.py::test_name
```