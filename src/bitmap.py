#!/usr/bin/env python
# coding: utf-8

"""
   File Name: bitmap.py
      Author: Wan Ji
      E-mail: wanji@live.com
  Created on: Thu May  1 15:26:18 2014 CST

  Description: BitMap Class
"""

import array
try:
    from past.builtins import range
except ImportError:
    pass

class BitMap(object):
    """
    BitMap class
    """

    BITMASK = [0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80]
    BIT_CNT = [bin(i).count("1") for i in iter(range(256))]

    def __init__(self, maxnum=0, bitmap=None, preset=False):
        """
        Create a BitMap
        """
        self.bits = maxnum
        nbytes = (maxnum + 7) // 8
        bit_value = 0xFF if preset else 0x00
        if bitmap:
            self.bitmap = bytearray(bitmap)
        else:
            self.bitmap = array.array('B', [bit_value for i in range(nbytes)])

    def __del__(self):
        """
        Destroy the BitMap
        """
        pass
    
    def __bytes__(self):
        return self.to_bytes()

    def to_bytes(self):
        return bytes(self.bitmap)

    def bit_size(self):
        return self.bits

    def byte_size(self):
        """
        Return size
        """
        return len(self.bitmap)

    def set(self, pos):
        """
        Set the value of bit@pos to 1
        """
        self.bitmap[pos // 8] |= self.BITMASK[pos % 8]

    def unset(self, pos):
        """
        Reset the value of bit@pos to 0
        """
        self.bitmap[pos // 8] &= ~self.BITMASK[pos % 8]

    def reset(self, pos):
        """
        Reset the value of bit@pos to 0
        """
        self.unset(pos)

    def flip(self, pos):
        """
        Flip the value of bit@pos
        """
        self.bitmap[pos // 8] ^= self.BITMASK[pos % 8]

    def count(self):
        """
        Count bits set
        """
        return sum([self.BIT_CNT[x] for x in self.bitmap])

    def size(self):
        """
        Return size
        """
        return len(self.bitmap) * 8

    def test(self, pos):
        """
        Return bit value
        """
        return (self.bitmap[pos // 8] & self.BITMASK[pos % 8]) != 0

    def any(self):
        """
        Test if any bit is set
        """
        return self.count() > 0

    def none(self):
        """
        Test if no bit is set
        """
        return self.count() == 0

    def all(self):
        """
        Test if all bits are set
        """
        return (self.count() + 7) // 8 * 8 == self.size()

    def nonzeros(self):
        """
        Get all non-zero bits, returns generator
        """
        for i in iter(range(self.size())):
            if self.test(i):
                yield i

    def nonzero(self):
        """
        Get all non-zero bits, returns list
        """
        return [i for i in iter(range(self.size())) if self.test(i)]

    def zeros(self):
        """
        Get all zero bits, returns generator
        """
        for i in iter(range(self.size())):
            if not self.test(i):
                yield i

    def zero(self):
        """
        Get all zero bits, returns list
        """
        return [i for i in iter(range(self.size())) if not self.test(i)]

    def tostring(self):
        """
        Convert BitMap to string
        """
        return "".join([("%s" % bin(x)[2:]).zfill(8)
                        for x in self.bitmap[::-1]])

    def __str__(self):
        """
        Overloads string operator
        """
        return self.tostring()

    def __getitem__(self, item):
        """
        Return a bit when indexing like a array
        """
        if isinstance(item, slice):
            # these attrs are readonly
            start = item.start
            stop = item.stop
            step = item.step
            if not isinstance(item.start, int):
                start = 0
            if not isinstance(item.step, int):
                step = 1
            if not isinstance(item.stop, int):
                stop = self.bit_size()
            return [self.test(i) for i in range(start, min(stop, self.bit_size()), step)]
        else:
            return self.test(item)

    def __setitem__(self, key, value):
        """
        Sets a bit when indexing like a array
        """
        if not isinstance(value, bool):
            raise Exception("Use a boolean value to assign to a bitfield")
        if isinstance(key, slice):
            # these attrs are readonly
            start = key.start
            stop = key.stop
            step = key.step
            if not isinstance(key.start, int):
                start = 0
            if not isinstance(key.step, int):
                step = 1
            if not isinstance(key.stop, int):
                stop = self.bit_size()
            if value:
                [self.set(i) for i in range(start, min(stop, self.bit_size()), step)]
            else:
                [self.reset(i) for i in range(start, min(stop, self.bit_size()), step)]
        else:
            if value:
                self.set(value)
            else:
                self.reset(value)

    def tohexstring(self):
        """
        Returns a hexadecimal string
        """
        val = self.tostring()
        st = "{0:0x}".format(int(val, 2))
        return st.zfill(len(self.bitmap) * 2)

    def tofile(self, path):
        """
        Save bitmap to file
        """
        with open(path, 'wb') as file:
            if isinstance(self.bitmap, bytearray):
                file.write(self.bitmap)
            else:
                self.bitmap.tofile(file)

    @classmethod
    def fromhexstring(cls, hexstring):
        """
        Construct BitMap from hex string
        """
        bitstring = format(int(hexstring, 16), "0" + str(int(len(hexstring)/4)) + "b")
        return cls.fromstring(bitstring)

    @classmethod
    def fromstring(cls, bitstring):
        """
        Construct BitMap from string
        """
        nbits = len(bitstring)
        bm = cls(nbits)
        for i in iter(range(nbits)):
            if bitstring[-i - 1] == '1':
                bm.set(i)
            elif bitstring[-i - 1] != '0':
                raise Exception("Invalid bit string!")
        return bm

    @classmethod
    def fromfile(cls, path, maxnum=None):
        if maxnum is None:
            with open(path, 'rb') as file:
                bitmap = file.read()
            return cls(bitmap=bitmap)
        else:
            bm = cls(maxnum)
            file = open(path, 'rb')
            bm.bitmap = array.array('B')
            bm.bitmap.fromfile(file, (maxnum + 7) // 8)
            file.close()
            return bm

