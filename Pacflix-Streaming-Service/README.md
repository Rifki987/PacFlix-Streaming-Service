# Streaming Project

## Overview
The Streaming Project is a Python-based application designed to manage a streaming service's user subscriptions. It provides functionalities for users to check their subscription benefits, upgrade their plans, and register new users. The system is built around a simple data structure that holds user information and subscription details, allowing for easy management and retrieval of data.

## Files
- **Streaming.py**: This file contains the core implementation of the streaming service management system. It defines the following classes:
  - `STATUS`: A class that represents the status of subscription plans (OK and NOT_OK).
  - `User`: A class that manages user data, subscription plans, and provides methods to check benefits and upgrade plans.
  - `newUser`: A class that handles the registration of new users and their plan selections.

## Features
- Check subscription benefits based on the selected plan.
- Upgrade subscription plans with pricing adjustments based on the duration of the current plan.
- Register new users with referral code support for discounts.

## Usage
1. **Installation**: Ensure you have Python and the required libraries installed. You may need to install `pandas` and `tabulate` for data handling and display.
   ```bash
   pip install pandas tabulate
   ```

2. **Running the Application**: You can run the application by executing the `Streaming.py` file. This will demonstrate the functionality of the classes and provide sample outputs.
   ```bash
   python Streaming.py
   ```

3. **Creating a New User**: To create a new user, instantiate the `newUser` class and use the `pick_plan` method to select a subscription plan. After selecting a plan, call the `activate` method to register the user.

4. **Managing Existing Users**: To manage existing users, create an instance of the `User` class with the user's name, duration of the plan, and current plan. You can then call methods like `check_benefit`, `check_plan`, and `upgrade_plan` to interact with the user's subscription.

## Example
```python
if __name__ == "__main__":
    instan = User("Shandy", 10, "Basic Plan")
    instan.check_benefit()
    instan.check_plan()
    print(instan.upgrade_plan("Standard Plan"))
    
    userbaru = newUser("coba")
    userbaru.pick_plan("Standard Plan", 'cahya-abcd')
    userbaru.activate()
```

## License
This project is open-source and available for modification and distribution under the MIT License. Please refer to the LICENSE file for more details.