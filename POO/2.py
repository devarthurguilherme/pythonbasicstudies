# Netflix Client
class Cliente:
    def __init__(self, nome: str, email: str, plan: str):
        self.nome = nome
        self.email = email
        self.plan = plan
        plans_list = ["basic", "premium"]
        # Check Plan
        if plan in plans_list:
            self.plan = plan
        else:
            print("Invalid Plan!")

    # methods
    def __str__(self):
        return f"Cliente(nome={self.nome}, email={self.email}, plan={self.plan})"


cliente = Cliente("Arthur Guilherme", "arthurguilherme@gmail.com", "basic")

# Print Client
print(cliente)
