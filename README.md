## LISE reader to isolate isotope name, charge information and cross section

**#!! Construction in Progress !!#**

Requires [Barion](https://github.com/xaratustrah/barion) from Xaratustrah to pull ame data.

A test file can be found in `/data` to check that the program is operational. It will automatically be executed when running `lisereader.py`.

# Functions

For all search functions, the search string should be formatted "\[element]\[A]" e.g. "80Kr"

`.get_index(name)` returns the line of the lise data that the searched element appears on

`.get_info(name)` returns \[element name, A, N, Z, charge state, cross section] for the searched element

`.get_info_all` returns a list of data for all the elements taken from the lise file, formatted identically to .get_info()