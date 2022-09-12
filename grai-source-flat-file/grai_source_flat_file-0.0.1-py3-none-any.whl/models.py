from enum import Enum
from typing import Any, Dict, List, Optional, Union

from pydantic import BaseModel, Field, root_validator, validator


class ID(BaseModel):
    name: str
    namespace: str
    full_name: str


class TableID(ID):
    table_schema: str

    @root_validator(pre=True)
    def make_full_name(cls, values):
        full_name = values.get("full_name", None)
        if values.get("full_name", None) is None:
            values["full_name"] = f"{values['table_schema']}.{values['name']}"
        return values


class ColumnID(ID):
    table_schema: str
    table_name: str

    @root_validator(pre=True)
    def make_full_name(cls, values):
        full_name = values.get("full_name", None)
        if values.get("full_name", None) is None:
            values[
                "full_name"
            ] = f"{values['table_schema']}.{values['table_name']}.{values['name']}"
        return values


class Column(BaseModel):
    name: str = Field(alias="column_name")
    namespace: str
    table: str
    data_type: str
    is_nullable: bool
    full_name: Optional[str] = None

    class Config:
        allow_population_by_field_name = True

    @validator("full_name", always=True)
    def make_full_name(cls, full_name, values):
        if full_name is not None:
            return full_name
        result = f"{values['table']}.{values['name']}"
        return result


class Table(BaseModel):
    name: str = Field(alias="table_name")
    namespace: str
    columns: Optional[List[Column]] = []
    metadata: Dict = {}
    full_name: Optional[str] = None

    class Config:
        allow_population_by_field_name = True

    @validator("full_name", always=True)
    def make_full_name(cls, full_name, values):
        if full_name is not None:
            return full_name

        return f"{values['table_schema']}.{values['name']}"

    def get_edges(self):
        return [
            Edge(
                constraint_type=Constraint("bt"),
                source=TableID(
                    table_schema=self.table_schema,
                    name=self.name,
                    namespace=self.namespace,
                ),
                destination=ColumnID(
                    table_schema=self.table_schema,
                    table_name=self.name,
                    name=column.name,
                    namespace=self.namespace,
                ),
            )
            for column in self.columns
        ]


class EdgeQuery(BaseModel):
    namespace: str
    constraint_name: str
    constraint_type: str
    self_schema: str
    self_table: str
    self_columns: List[str]
    foreign_schema: str
    foreign_table: str
    foreign_columns: List[str]
    definition: str

    def to_edge(self) -> Edge:
        assert len(self.self_columns) == 1 and len(self.foreign_columns) == 1
        destination = ColumnID(
            table_schema=self.self_schema,
            table_name=self.self_table,
            name=self.self_columns[0],
            namespace=self.namespace,
        )
        source = ColumnID(
            table_schema=self.foreign_schema,
            table_name=self.foreign_table,
            name=self.foreign_columns[0],
            namespace=self.namespace,
        )
        return Edge(
            definition=self.definition,
            source=source,
            destination=destination,
            constraint_type=self.constraint_type,
        )
