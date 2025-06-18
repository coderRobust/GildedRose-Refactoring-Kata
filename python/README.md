# Gilded Rose Kata – Python (Refactored)

This is a clean implementation of the Gilded Rose Kata in Python using the **Factory Design Pattern**.  
It includes complete support for **Conjured items** and full unit test coverage.

##  Directory

All changes are in the `python/` directory.


##  Setup Instructions

# 1. Create Virtual Environment

```bash
python -m venv venv
```

# 2. Activate the Virtual Environment

  ```bash
  source venv/bin/activate
  ```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```


```bash
pip install coverage
```

---

# Run Unit Tests

```bash
python -m unittest test_gilded_rose.py
```

Test cases cover:
- Normal Items
- Aged Brie
- Backstage Passes
- Sulfuras
- Conjured Items

---

# Test Coverage

```bash
coverage run test_gilded_rose.py
coverage report -m
```


# Code Structure Highlights

- Factory Pattern for item type logic
- Separate updater classes per item
- Easy to extend and test
- Clean, Pythonic code



# Conjured Item Support

- Items starting with `"Conjured"` degrade in quality twice as fast
- After expiration, degrade 4x as fast
- Fully tested with edge cases



# Example Commands Summary

# bash

python -m venv venv
source venv/bin/activate        # or venv\Scripts\activate
pip install -r requirements.txt
python -m unittest test_gilded_rose.py
coverage run test_gilded_rose.py
coverage report -m
python texttest_fixture.py 10


