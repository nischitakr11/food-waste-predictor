# 🍱 Food Waste Predictor

A beginner-friendly Python project that analyzes food waste based on the amount of food prepared and consumed.

## Problem Statement

Restaurants, canteens, and food service organizations may prepare more food than is actually consumed. This can result in unnecessary food waste.

The goal of this project is to provide a simple tool that measures food waste and identifies the level of waste.

## Features

- Accepts food preparation quantity as input
- Accepts food consumption quantity as input
- Calculates total food wasted
- Calculates waste percentage
- Classifies waste as Low, Moderate, or High
- Provides a basic recommendation
- Validates user input
- Uses modular Python functions

## How It Works

```text
Food Prepared
      +
Food Consumed
      ↓
Calculate Food Waste
      ↓
Calculate Waste Percentage
      ↓
Determine Waste Level
      ↓
Generate Recommendation
      ↓
Display Report
```

## Example

```text
========== FOOD WASTE PREDICTOR ==========
Enter amount of food prepared: 100
Enter amount of food consumed: 70

========== FOOD WASTE REPORT ==========
Food Prepared     : 100.00 units
Food Consumed     : 70.00 units
Food Wasted       : 30.00 units
Waste Percentage  : 30.00%
Waste Level       : HIGH
Recommendation    : Reduce the amount of food prepared and review demand patterns.
========================================
```

## Technologies Used

- Python 3

## Python Concepts Used

- Variables
- Data types
- User input
- Type conversion
- Arithmetic operations
- Conditional statements
- Functions
- Parameters and arguments
- Return values
- Exception handling
- Input validation
- Formatted strings

## Project Structure

```text
food-waste-predictor/
│
├── food_waste_predictor.py
└── README.md
```

## Current Version

### V1 — Basic Food Waste Analysis

The first version focuses on analyzing the relationship between food prepared and food consumed.

This version does **not** use machine learning yet.

## Future Improvements

- Store historical food waste data
- Add daily and monthly tracking
- Add CSV/JSON data storage
- Analyze waste trends using Pandas
- Create visualizations using Matplotlib
- Use machine learning for food demand prediction
- Predict the optimal amount of food to prepare
- Provide data-driven recommendations
- Build a web interface
