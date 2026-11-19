# L6_L7_36 — Highway Toll Calculator

Lab 6: Code and Branch Coverage

## About

A small Python  module that calculates toll charges by axle count, peak hours and electronic tag, and advises on monthly passes.

## Files

| File | Description |
|------|-------------|
| `highway_toll.py` | The module under test |
| `test_highway_toll.py` | Starter test file |

Refer to the lab handout for instructions.
# Highway Toll - Lab 6

**Student:** Bhavish A
**SRN:** PES2UG24AM040

## Run

```bash
pip install pytest coverage
pytest -q CodeCoverageTest_highway_toll.py
coverage run -m pytest CodeCoverageTest_highway_toll.py
coverage report -m
```

The code-coverage suite targets at least 90% line coverage.

For branch coverage:

```bash
coverage run --branch -m pytest BranchCoverageTest_highway_toll.py
coverage report -m
```

Verified result: 18 branch tests passed; total branch coverage reached 97%.
