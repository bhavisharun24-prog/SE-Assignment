# L6_L7_36 — Highway Toll Calculator

Lab 7: Fuzz Testing

## About

A small Python module that reads vehicle plates, prices trips and classifies vehicles by axle count.

## Files

| File | Description |
|------|-------------|
| `highway_toll.py` | The code under test |
| `test_highway_toll.py` | Starter test file |

Refer to the lab handout for instructions.
# Highway Toll - Lab 7

**Student:** Bhavish A
**SRN:** PES2UG24AM040

## Run

```bash
pip install pytest hypothesis
python highway_toll.py
pytest -q test_highway_toll.py
```

The three functions validate malformed plate strings, trip-cost expressions,
and axle counts before processing them.
