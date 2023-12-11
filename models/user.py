#!/usr/bin/python3
"""
A module for the User class.
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    a class User that handles users' information
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""