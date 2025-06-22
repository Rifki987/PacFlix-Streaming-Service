# Streaming Project

"""
Streaming.py

This module implements a streaming service management system, allowing users to manage their subscriptions, check benefits, and handle plan upgrades. 

Classes:

1. STATUS:
   - A simple class that defines constants for representing the status of services (OK and NOT_OK) using Unicode check and cross symbols.

2. User:
   - Represents a user of the streaming service.
   - Attributes:
     - data_base_user: A DataFrame containing user data, indexed by username.
     - data: A dictionary containing service details for different subscription plans.
     - Table: A DataFrame representing the services and their corresponding details for each plan.
     - PLAN_POIN: A dictionary mapping plan names to their respective point values for upgrade/downgrade logic.
   - Methods:
     - __init__(user_name, duration_plan, current_plan): Initializes a User instance with the provided user information and subscription details.
     - check_benefit(): Displays the available services and benefits for each subscription plan.
     - check_plan(): Checks and displays the current plan and duration for the user.
     - upgrade_plan(new_plan): Upgrades the user's subscription plan if eligible and returns the price, applying a discount for long-term subscribers.

3. newUser:
   - Represents a new user registering for the streaming service.
   - Attributes:
     - user_name: The name of the new user.
     - picked_plan: The plan selected by the new user.
   - Methods:
     - __init__(user_name): Initializes a newUser instance with the provided username.
     - pick_plan(new_plan=None, referal_code=None): Allows the user to select a subscription plan, optionally applying a referral code for a discount.
     - activate(): Activates the selected plan for the new user and adds them to the user database.

Usage:
- The module includes a sample usage in the __main__ block, demonstrating how to create a User instance, check benefits, check the current plan, upgrade the plan, and register a new user.

Dependencies:
- Requires the pandas library for data management and the tabulate library for formatted output.
"""

from pandas import DataFrame
from tabulate import tabulate
from random import choices
import string

# Assume data constant for now
DATA = {
    "Header": ["PLAN", "DURATION", "REFERAL"],
    "Shandy": ["Basic Plan", 13, "shandy-2134"],
    "Cahya": ["Standard Plan", 24, "cahya-abcd"],
    "Ana": ["Premium Plan", 5, "ana-2f9g"],
    "Bagus": ["Basic Plan", 11, "bagus-9f92"]
}

class STATUS:
    OK = "\u2714"
    NOT_OK = "\u2716"

class User:
    data_base_user = DataFrame(DATA).set_index("Header").T
    data: dict[str, list] = {
        "Services": ["Bisa Stream", "Bisa Download", "Kualitas SD", "Kualitas HD", "Kualitas UHD", "Number of Devices", "Jenis Konten", "Harga"],
        "Basic Plan": [STATUS.OK, STATUS.OK, STATUS.OK, STATUS.NOT_OK, STATUS.NOT_OK, 1, "3rd party Movie only", 120_000],
        "Standard Plan": [STATUS.OK, STATUS.OK, STATUS.OK, STATUS.OK, STATUS.NOT_OK, 2, "Basic Plan Content + Sports", 160_000],
        "Premium Plan": [STATUS.OK, STATUS.OK, STATUS.OK, STATUS.OK, STATUS.OK, 4, "Basic Plan + Standard Plan + PacFlix Original Series", 200_000]
    }
    Table = DataFrame(data).set_index("Services")
    PLAN_POIN = {"Basic Plan": 1, "Standard Plan": 2, "Premium Plan": 3}

    def __init__(self, user_name, duration_plan, current_plan):
        self.user_name = user_name
        self.duration_plan = duration_plan
        self.current_plan = current_plan

    def check_benefit(self):
        print("PacFlix Plan List\n")
        table = self.Table.reset_index()
        col_align = ["center"]*len(table.columns)
        print(tabulate(table.values.tolist(), headers=table.columns, colalign=col_align))

    def check_plan(self):
        username = self.user_name
        if not username in self.data_base_user.index:
            raise ValueError("Username didn't exist in database")
        Plan_type = self.data_base_user.loc[username, "PLAN"]
        if Plan_type not in self.Table.columns:
            raise ValueError("PLAN Type didn't exist")
        print(f"\n{Plan_type}")
        print(f"{self.data_base_user.loc[username, 'DURATION']} Bulan\n")
        print(f"{Plan_type} PacFlix Benefit List\n")
        print(tabulate(self.Table[[Plan_type]].reset_index().values.tolist(), headers=["Services", Plan_type], colalign=["center", "center"]))

    def upgrade_plan(self, new_plan):
        if not self.user_name in self.data_base_user.index:
            raise ValueError("Username didn't exist in database")
        current_plan = self.data_base_user.loc[self.user_name, "PLAN"]
        if current_plan not in self.PLAN_POIN or new_plan not in self.PLAN_POIN:
            raise ValueError("Plan not exist in database")
        if self.PLAN_POIN[current_plan] >= self.PLAN_POIN[new_plan]:
            raise ValueError("Upgrade Plan Failed, Can't Downgrade Plan")
        price = int(self.Table.loc["Harga", new_plan])
        return price * 0.95 if self.data_base_user.loc[self.user_name, "DURATION"] > 12 else price

class newUser:
    def __init__(self, user_name):
        self.user_name = user_name
        self.picked_plan = None

    def pick_plan(self, new_plan=None, referal_code=None):
        if not new_plan in User.PLAN_POIN:
            raise IndexError("PLAN didn't exist in our services")
        if referal_code is None:
            self.picked_plan = new_plan
            return User.Table.loc["Harga", new_plan]
        if referal_code in User.data_base_user["REFERAL"].values:
            self.picked_plan = new_plan
            return User.Table.loc["Harga", new_plan] * 0.96
        else:
            raise ValueError("Referal Code Invalid")

    def activate(self):
        if self.picked_plan is None:
            raise SyntaxError("Must declare Pickplan first before activating to database")
        referal = self.user_name.lower() + "-" + "".join(choices(string.ascii_lowercase + string.digits, k=4))
        User.data_base_user.loc[self.user_name] = [self.picked_plan, 0, referal]
        print("Activate successfully")

if __name__ == "__main__":
    instan = User("Shandy", 10, "Basic Plan")
    # instan.check_benefit()
    # print(instan.data_base_user)
    # instan.check_plan()
    # print(instan.upgrade_plan("Standard Plan"))
    # userbaru = newUser("coba")
    # userbaru.pick_plan("Standard Plan", 'cahya-abcd')
    # userbaru.activate()
    # print(instan.data_base_user)