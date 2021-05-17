# satellite-frequency-coordination

## Table export (optional)

Download a tool for exporting mdb to csv:

```apt install mdbtools```

or

```brew install mdbtools```

as in https://github.com/mdbtools/mdbtools.


Export tables you would like to use:

```mdb-export srs2936_part1of2.mdb sat_oper > sat_oper.csv```

## Instructions

Install Python3 and pandas.

```pip3 install -r requirements.txt```

Modify `config.py` file for desired satellite names.

Run ```python3 read_csv.py```.

Check your results in `results.csv` file.
