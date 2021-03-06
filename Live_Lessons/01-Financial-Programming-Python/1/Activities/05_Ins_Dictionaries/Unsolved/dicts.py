# -*- coding: utf-8 -*-
"""Instructor Demo: Dictionaries

This script showcases basic operations of Python Dicts.
"""
top_traders_2021 = {
    "january": "Karen", 
    "february": "Harold",
    "march": "Sam"
    }

print() # Remmeber this is to help with organized outputs in terminal. Could be dashes or whatever.
print(f"Dictionary: {top_traders_2021}")
print()

trading_pnl = {
    "title": "Trading Log",
    "03-18-2019": -224,
    "03-19-2019": 352,
    "03-20-2019": 252,
    "03-21-2019": 354,
    "03-22-2019": -544,
    "03-23-2019": -650,
    "03-24-2019": 56,
    "03-25-2019": 123,
    "03-26-2019": -43,
    "03-27-2019": 254,
    "03-28-2019": 325,
    "03-29-2019": -123,
    "03-30-2019": 47,
    "03-31-2019": 321,
    "04-01-2019": 123,
    "04-02-2019": 133,
    "04-03-2019": -151,
    "04-04-2019": 613,
    "04-05-2019": 232,
    "04-06-2019": -311,
}

print()
print(f"Dictionary: {trading_pnl}")
print()

print(f"03-31-2019: {trading_pnl['03-31-2019']}")
print()

trading_pnl["04-07-2019"] = 413
print(trading_pnl)
print()

trading_pnl["04-07-2019"] = 542
print(trading_pnl)
print()

print(trading_pnl.get("03-29-2019"))
print()

del trading_pnl["04-07-2019"]
print(trading_pnl)
print()