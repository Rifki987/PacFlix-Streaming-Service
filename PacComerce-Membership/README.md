# PacComerce Membership Prediction

This project simulates a membership system for an e-commerce platform called **PacComerce**.  
It predicts user membership tiers based on their monthly expenses and income, and calculates discounts accordingly.

## Features

- **View Membership Benefits:** See the benefits for each membership tier.
- **View Membership Requirements:** See the requirements for each membership tier.
- **Predict Membership:** Predicts the user's membership tier using the Euclidean distance method based on their monthly expense and income.
- **Calculate Discounted Price:** Calculates the total price after applying the membership discount.

## How It Works

1. **Initialize a User:**
   ```python
   user = Membership("Shandy")
   ```
2. **Show Membership Benefits:**
   ```python
   user.show_benefit()
   ```
3. **Show Membership Requirements:**
   ```python
   user.show_requirement()
   ```
4. **Predict Membership:**
   ```python
   user.predict_membership(9, 12)
   ```
5. **Calculate Discounted Price:**
   ```python
   user.calculate_price([150000, 200000, 400000])
   ```

## Requirements

- Python 3.x
- pandas
- tabulate

Install dependencies with:
```sh
pip install pandas tabulate
```

## Author

Rifki (BFP)