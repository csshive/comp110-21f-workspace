"""Utility functions."""

__author__ = "730330844"

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a table."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all vlaues in a single column."""
    result: list[str] = []
    for row in table: 
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriended table."""
    result: dict[str, list[str]] = {}
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
    return result


def head(column_table: dict[str, list[str]], n: int) -> dict[str, list[str]]:
    """Produce a new column-based table with only the first N rows of data for each column."""
    result: dict[str, list[str]] = {}
    # 1. Establish an empty dictionary that will serve as the returned dictionary this function is building up.
    # 2. Loop through each of the columns in the first row of the table given as a parameter.
    #   A. Inside of the loop, establish an empty list to store each of the first N values in the column
    #   B. Loop through the first N items of the table's column,
    #       a. Appending each item to the previously list established in step 2.1.
    #   C. Assign the produced list of column values to the dictionary established in step 1.
    return result
    # Return the dictionary.


def select(column_table: dict[str, list[str]], names: list[str]) -> dict[str, list[str]]:
    """Produce a new column-based table with only a specific subset of the original columns"""
    result: dict[str, list[str]] = {}
    # 1. Establish an empty dictionary that will serve as the returned dictionary this function is building up.
    # 2. Loop through each of the columns in the second parameter of the function
    #   A. Assign to the column key of the result dictionary the list of values stored in the input dictionary at the same column
    return result
    # 3.Return the dictionary produced

        
def concat(column_table_one: dict[str, list[str]], column_table_two: dict[str, list[str]]) -> dict[str, list[str]]:
    """Purpose: Produce a new column-based table with two column-based tables combined."""
    result: dict[str, list[str]] = {}
    result = {**column_table_one, **column_table_two}
    for key, value in result.items():
        if key in column_table_one and key in column_table_two:
            result[key] = [value, column_table_one[key]]
    return result