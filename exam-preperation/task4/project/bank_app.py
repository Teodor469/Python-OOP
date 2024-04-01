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
        new_loan_class = self.TYPE_OF_LOANS[loan_type]
        new_loan = new_loan_class()  # Instantiate the loan class to create a new loan object
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

        if not client:
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
                client.increase_clients_interest()
                changed_client_rates_number += 1  # Increment the counter

        # Return a message indicating the number of clients whose interest rates have been changed
        return f"Number of clients affected: {changed_client_rates_number}."


    def get_statistics(self):
    # Counters and accumulators for calculating statistics
        total_clients_count = len(self.clients)
        total_clients_income = sum(client.income for client in self.clients)
        loans_count_granted_to_clients = sum(1 for client in self.clients if client.loans)
        granted_sum = sum(loan.amount for client in self.clients for loan in client.loans)
        loans_count_not_granted = len(self.loans) - loans_count_granted_to_clients
        not_granted_sum = sum(loan.amount for loan in self.loans if loan not in [loan for client in self.clients for loan in client.loans])
        
        # Calculate the average client interest rate
        total_interest_rates = sum(client.interest for client in self.clients)
        avg_client_interest_rate = total_interest_rates / total_clients_count if total_clients_count > 0 else 0

        # Format the statistics to the 2nd decimal place
        avg_client_interest_rate = "{:.2f}".format(avg_client_interest_rate)
        total_clients_income = "{:.2f}".format(total_clients_income)
        granted_sum = "{:.2f}".format(granted_sum)
        not_granted_sum = "{:.2f}".format(not_granted_sum)

        # Construct and return the statistics string
        statistics = f"Active Clients: {total_clients_count}\n" \
                    f"Total Income: {total_clients_income}\n" \
                    f"Granted Loans: {loans_count_granted_to_clients}, Total Sum: {granted_sum}\n" \
                    f"Available Loans: {loans_count_not_granted}, Total Sum: {not_granted_sum}\n" \
                    f"Average Client Interest Rate: {avg_client_interest_rate}"

        return statistics


    #helper methods
    def find_client_by_id(self, client_id: str) -> BaseClient:
        for client in self.clients:
            if client.client_id == client_id:
                return client
        raise Exception("No such client!")
    

    def find_loan_by_type(self, loan_type: str) -> BaseLoan:
        for loan in self.loans:
            if isinstance(loan, self.TYPE_OF_LOANS.get(loan_type)):
                return loan
        raise ValueError("Loan not found.")