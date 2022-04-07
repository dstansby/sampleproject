from setuptools import setup, Extension, find_packages
import Cython.Build

extensions = [Extension("sampleproject.primes",
                        ["sampleproject/primes.pyx"])]

setup(
    name='sampleproject',
    packages=["sampleproject"],
    ext_modules=extensions,
    cmdclass={'build_ext': Cython.Build.build_ext},
    zip_safe=False,
    include_package_data=True,
)
