BitMap for python
=================

An updated version of the bitmap library from https://github.com/wanji/bitmap since the original 
project is no longer maintained.

This package provides a `BitMap` class which is an array of bits stored in compact format.

# Installation

`bitmap` can be installed from `pip`:

```bash
pip3 install bitmap2
```

# Functions

- `BitMap(maxnum)`: construct a `BitMap` object with `maxnum` bits
- `set(pos)`: set the bit at position `pos` to 1
- `reset(pos)`: reset the bit at position `pos` to 0
- `flip(pos)`: flip the bit at position `pos`
- `count()`: return the number of 1s
- `size()`: return the size of the `BitMap`
- `test(pos)`: check if bit at position `pos` has been set to 1
- `any()`: check if any bit in the `BitMap` has been set to 1
- `none()`: check if none of the bits in the `BitMap` has been set to 1
- `all()`: check if all bits in the `BitMap` has been set to 1
- `nonzero()`: return indexes of all non-zero bits
- `tostring()`: convert a `BitMap` object to `0` and `1` string
- `tofile(path)`: save a `BitMap` object to a file on `path`
- `fromstring(bitstring)`: create a `BitMap` object from `0` and `1` string
- `fromhexstring(hexstring)`: construct a `BitMap` object from hex string
- `fromfile(path, maxnum)`: construct a `Bitmap` object from a file at `path` of size `maxnum` bits

# Examples

```python
from bitmap import BitMap
bm = BitMap(32)
print bm.tostring()
bm.set(1)
print bm.tostring()

bm = BitMap.fromstring("00011101")
print bm.tostring()
bm.flip(1)
print bm.tostring()
```
