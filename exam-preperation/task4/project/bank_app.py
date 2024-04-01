from typing import List
from project.loans.base_loan import BaseLoan
from project.loans.student_loan import StudentLoan
from project.loans.mortgage_loan import MortgageLoan
from project.clients.base_client import BaseClient
from project.clients.student import Student
from project.clients.adult import Adult



class BankApp:
    TYPE_OF_LOANS = {"StudentLoan": StudentLoan, "MortgageLoan": MortgageLoan}
    TYPE_OF_CLIENTS = {"Student": Student, "Adult": Adult}


    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.loans: List[BaseLoan] = []
        self.clients: List[BaseClient] = []


    
    def add_loan(self, loan_type: str):
        if loan_type not in self.TYPE_OF_LOANS:
            raise Exception("Invalid loan type!")
        
        new_loan = self.TYPE_OF_LOANS[loan_type]()  # Instantiate the loan class to create a new loan object
        self.loans.append(new_loan)
        return f"{loan_type} was successfully added."


    def add_client(self, client_type: str, client_name: str, client_id: str, income: float):
        if client_type not in self.TYPE_OF_CLIENTS:
            raise Exception("Invalid client type!")
        
        if len(self.clients) >= self.capacity:
            return "Not enough bank capacity."
        
        new_client = self.TYPE_OF_CLIENTS[client_type](client_name, client_id, income)
        self.clients.append(new_client)
        return f"{client_type} was successfully added."


    def grant_loan(self, loan_type: str, client_id: str):
        try:
            client = self.find_client_by_id(client_id)
            loan = self.find_loan_by_type(loan_type)
        except ValueError as e:
            return str(e)

        if isinstance(client, Student) and loan_type != "StudentLoan":
            return "Inappropriate loan type!"
        elif isinstance(client, Adult) and loan_type != "MortgageLoan":
            return "Inappropriate loan type!"

        self.loans.remove(loan)
        client.loans.append(loan)
        return f"Successfully granted {loan_type} to {client.name} with ID {client.client_id}."


    def remove_client(self, client_id: str):
        client = self.find_client_by_id(client_id)
        if client is None:
            raise Exception("No such client!")

        if client.loans:
            raise Exception("The client has loans! Removal is impossible.")

        self.clients.remove(client)
        return f"Successfully removed {client.name} with ID {client.client_id}."
            


    def increase_loan_interest(self, loan_type: str):

        changed_loans = 0  # Counter for the number of loans whose interest rates have been changed

        # Iterate through the bank's loans
        for loan in self.loans:
            # Check if the loan is of the specified type
            if isinstance(loan, self.TYPE_OF_LOANS.get(loan_type)):
                # Increase the loan's interest rate
                loan.increase_interest_rate()
                changed_loans += 1  # Increment the counter

        # Return a message indicating the number of loans whose interest rates have been changed
        return f"Successfully changed {changed_loans} loans."




    def increase_clients_interest(self, min_rate: float):
        changed_client_rates_number = 0  # Counter for the number of clients whose interest rates have been changed
        # Iterate through the bank's clients
        for client in self.clients:
            # Check if the client's interest rate is less than the min_rate value
            if client.interest < min_rate:
                # Increase the client's interest rate
                client.interest = min_rate
                changed_client_rates_number += 1  # Increment the counter

        # Return a message indicating the number of clients whose interest rates have been changed
        return f"Number of clients affected: {changed_client_rates_number}."


    def get_statistics(self):
        total_income = sum([client.income for client in self.clients])
        granted_loans_count = sum([len(client.loans) for client in self.clients])
        granted_amount = sum([sum([loan.amount for loan in client.loans]) for client in self.clients])
        not_granted_sum = sum([loan.amount for loan in self.loans])
        avg_client_rate = sum([client.interest for client in self.clients]) / len(self.clients) if self.clients else 0

        return f"""Active Clients: {len(self.clients)}
Total Income: {total_income:.2f}
Granted Loans: {granted_loans_count}, Total Sum: {granted_amount:.2f}
Available Loans: {len(self.loans)}, Total Sum: {not_granted_sum:.2f}
Average Client Interest Rate: {avg_client_rate:.2f}"""


    #helper methods
    def find_client_by_id(self, client_id):
        client = [client for client in self.clients if client.client_id == client_id]
        return client[0] if client else None
    

    def find_loan_by_type(self, loan_type: str) -> BaseLoan:
        for loan in self.loans:
            if isinstance(loan, self.TYPE_OF_LOANS.get(loan_type)):
                return loan
        raise ValueError("Loan not found.")