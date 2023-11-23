import sqlite3
from langchain.tools import Tool
from pydantic.v1 import BaseModel
from typing import List
conn = sqlite3.connect("db.sqlite")


def list_tables():
    c = conn.cursor()
    c.execute("Select name from sqlite_master where type = 'table';")
    rows = c.fetchall()
    return "\n".join(row[0] for row in rows if row is not None)


def run_sqlite_query(query):
    c = conn.cursor()

    try:
        c.execute(query)
        return c.fetchall()

    except sqlite3.OperationalError as error:
        return f"The following error occurred: {str(error)}\n"


class RunQueryArgsSchema(BaseModel):
    query: str


run_query_tool = Tool.from_function(
    name="run_sqlite_query_string",  # Can name whatever you want
    description="Run a sqlite query",
    func=run_sqlite_query,
    args_schema=RunQueryArgsSchema
)


def describe_tables(table_names):
    c = conn.cursor()
    tables = ", ".join("'" + table + "'" for table in table_names)
    rows = c.execute(f"select sql from sqlite_master where type = 'table' and name in ({tables});")
    return "\n".join(row[0] for row in rows if row is not None)


class DescribeTablesArgsSchema(BaseModel):
    table_names: List[str]


describe_table_tool = Tool.from_function(
    name="describe_tables",  # Can name whatever you want
    description="Given a list of table names, returns the schema of those tables",
    func=describe_tables,
    args_schema=DescribeTablesArgsSchema
)
