# BMR Calculator: Basal Metabolic Rate Estimation 🧮✨  

This repository contains a Python script, `BasalMetabolicRate.py`, for calculating the **Basal Metabolic Rate (BMR)** using the **Harris-Benedict equation** and the **Katch-McArdle formula**. It provides quick estimations of BMR based on weight, height, age, and lean body weight.

---

## Features ✨  

- **Harris-Benedict Equation**: Estimate BMR using standard metrics.  
- **Katch-McArdle Formula**: Calculate BMR based on lean body mass.  
- **Simple Interface**: Easy-to-use class for testing and customization.  

---

## Prerequisites 🛠️  

- Python 3.6+ installed on your system.  

---

## Installation  

1. Clone the repository:  
git clone https://github.com/your-username/bmr-calculator.git  
cd bmr-calculator  

2. Run the script:  
python asalMetabolicRate.py  

---

## Usage 🔧  

### Example Script  

The script defines the `BasalMetabolicRate` class with the following methods:  

- `bmr()`: Calculates BMR using the Harris-Benedict equation.  
- `katchmacardle()`: Calculates BMR using the Katch-McArdle formula.  
- `show()`: Prints the BMR result to the console.  

You can modify the parameters directly in the class or extend it for dynamic input.  

### Sample Code  

```python
from asalMetabolicRate import BasalMetabolicRate

# Instantiate the BMR class
bmr_calculator = BasalMetabolicRate()

# Display BMR using the Harris-Benedict equation
print("BMR (Harris-Benedict):", bmr_calculator.bmr())

# Display BMR using the Katch-McArdle formula
print("BMR (Katch-McArdle):", bmr_calculator.katchmacardle())
