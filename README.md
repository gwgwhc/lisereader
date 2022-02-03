# LISEreader

Requires [Barion](https://github.com/xaratustrah/barion) from [@Xaratustrah](https://github.com/xaratustrah) to pull ame data.

A test file can be found in `/test` to check that the program is operational. It will automatically be executed when running `lisereader.py`.

### Functions

For all search functions, the search string should be formatted "\[element]\[A]" e.g. "80Kr"

`.get_index(name)` returns the line of the lise data that the searched element appears on

`.get_info(name)` returns \[element name, A, Z, N, [charge states], yield] for the searched element

`.get_info_all()` returns a list of data for all the elements taken from the lise file, formatted identically to .get_info()

`.get_info_specific(index_list)` returns a list of data at the given indexes in index_list from the lise file