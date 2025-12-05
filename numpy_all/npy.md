# Getting started with numpy

1. What is Numpy?
    - NumPy is a Python library used for working with arrays.

2. Why to use Numpy?
    - In Python we have lists that serve the purpose of arrays, but they are slow to process.
    - NumPy aims to provide an array object that is up to 50x faster than traditional Python lists.
    - The array object in NumPy is called ndarray, it provides a lot of supporting functions that make working with ndarray very easy.

3. Why is Numpy faster then Lists?
    - NumPy arrays are stored at one continuous place in memory unlike lists, so processes can access and manipulate them very efficiently.
    - This behavior is called locality of reference in computer science.
    - This is the main reason why NumPy is faster than lists. Also it is optimized to work with latest CPU architectures

4. Import NumPy
    - Once NumPy is installed, import it in your applications by adding the import keyword: import numpy
    - Now NumPy is imported and ready to use.

5. NumPy as np: 
    - NumPy is usually imported under the np alias.
    - alias: In Python alias are an alternate name for referring to the same thing.
    - Create an alias with the as keyword while importing: import numpy as np
    - Now the NumPy package can be referred to as np instead of numpy

6. Create a NumPy ndarray Object:
    - NumPy is used to work with arrays. The array object in NumPy is called ndarray.
    - We can create a NumPy ndarray object by using the array() function.
    - Example in file(npy2.py)
    