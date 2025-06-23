"""
PacComerce Membership Prediction System

This module simulates a membership system for an e-commerce platform called PacComerce.
It allows users to:
- View membership benefits and requirements.
- Predict their membership tier based on monthly expense and income using the Euclidean distance method.
- Calculate the total price after applying membership discounts.

Classes:
    Membership: Handles membership data, prediction, and benefit/requirement display.

Example usage:
    user = Membership("Shandy")
    user.show_benefit()
    user.show_requirement()
    user.predict_membership(9, 12)
    user.calculate_price([150000, 200000, 400000])
"""


from pandas import DataFrame
from tabulate import tabulate
# Data yang digunakan untuk inisialisasi membership
# data berisi nama user dan membership yang dimiliki
# in real program data will retrieve from db

data:dict[str,str] = {
        "Sumbul": "Platinum",
        "Ana": "Gold",
        "Cahya": "Platinum"
    }

class Membership:
    #inisiasi data dari luar
    data:dict[str,str] = data
    # tabel benefit membership
    # benefit_table berisi benefit yang didapatkan dari masing-masing membership
    benefit_table = [
        ["Platinum", 0.15, "Benefit Gold + Silver + Cashback max. 30%"],
        ["Gold", 0.1, "Benefit Silver + Voucher Ojek Online"],
        ["Silver", 0.08, "Voucher Makanan"]
        ]
    benefit_table = DataFrame(benefit_table, columns=["Membership", "Discount", "Another Benefit"]).set_index("Membership")
    #requirement_table berisi requirement untuk mendapatkan masing-masing membership
    # requirement_table berisi informasi tentang pengeluaran dan pendapatan bulanan yang diperlukan untuk mendapatkan
    requirement_table = [
            ["Platinum", 8, 15],
            ["Gold", 6, 10],
            ["Silver", 5, 7],
        ]
    requirement_table = DataFrame(requirement_table, columns=["Membership", "Monthly Expense (juta)", "Monthly Income (juta)"]).set_index("Membership")

    def __init__(self,user_name):
        self.user_name = user_name
    
    def show_benefit(self):
        tables = self.benefit_table.reset_index()
        colalign = ["center"] * len(tables.columns)
        print("Benefit Membership PacCommerce\n")
        print(tabulate(tables.values.tolist(), headers=tables.columns, tablefmt="grid",colalign=colalign))

    def show_requirement(self):
        tables = self.requirement_table.reset_index()
        colalign = ["center"] * len(tables.columns)
        print("Requirement Membership PacCommerce\n")
        print(tabulate(tables.values.tolist(), headers=tables.columns, tablefmt="grid",colalign=colalign))
    
    # method untuk melakukan prediksi membership
    # menggunakan euclidean 
    
    def predict_membership(self, monthly_expense:int, monthly_income:int):

        best,best_dist = None, float("inf")
        for index, row in self.requirement_table.iterrows():
            dist_quadratic = (row["Monthly Expense (juta)"] - monthly_expense)**2+(row["Monthly Income (juta)"] - monthly_income)**2
            if dist_quadratic < best_dist:
                best, best_dist = index, dist_quadratic
        print(f"From your monthly expense Rp {monthly_expense} juta and monthly income Rp {monthly_income} juta, we predict you will get {best} membership")
        self.data[self.user_name] = best
        print(f"Your membership is now {self.data[self.user_name]}")
        return best
    
    def calculate_price(self,list_harga:list):
        if self.user_name not in self.data:
            print("You don't have membership yet, please predict your membership first")
            return None
        membership = self.data[self.user_name]
        discount = self.benefit_table.loc[membership, "Discount"]
        total_price = sum(list_harga)
        discounted_price = total_price * (1 - discount)
        print(f"Total price after {membership} discount is Rp {discounted_price:,}")
        return discounted_price



