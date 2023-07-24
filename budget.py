class Category:
    
    def __init__(self, category):
        self.category = category
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def get_balance(self):
        return sum([i["amount"] for i in self.ledger])
    
    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": amount * -1, "description": description})
            return True 
        else:
            return False
        
    def transfer(self, amount, transfer):
        if self.check_funds(amount):
            self.ledger.append({"amount": amount * -1, "description": "Transfer to " + transfer.category})
            transfer.ledger.append({"amount": amount, "description": "Transfer from " + self.category})
            return True
        else:
            return False

    def check_funds(self, amount):
        return True if self.get_balance() >= amount else False
    
    def __str__(self):
        title = self.category.center(30, "*") + "\n"
        budget = ""
        for i in self.ledger:
            description = i["description"][:23]
            amount = "{:.2f}".format(i["amount"])[:7]
            space = 30 - (len(description) + len(amount))
            budget += description + " " * space + amount + "\n"
        total = "Total: " + "{:.2f}".format(self.get_balance()) 

        return title + budget + total
 

def create_spend_chart(categories):

    
    # Loop for get total of amount withdrow of all categories
    total_amount = 0
    arr_total_amount = []
    for i in categories:
        arr_total_amount += [j["amount"] for j in i.ledger if j["amount"] < 0]

    total_amount = sum(arr_total_amount) * -1

    # Loop for create a list with name of category and the percentage with relation of total_amount
    data_graph = []
    for k in categories:
        tmp_amount = [l["amount"] for l in k.ledger if l["amount"] < 0]
        data_graph.append({ "category_name": k.category, "percentage_category": ((sum(tmp_amount) * -1) * 100) / total_amount})

    # Title of graph
    title = "Percentage spent by category\n"

    # Loop for create the graph part
    tmp_graph = []
    graph = ""
    for k in range(100, -1, -10):
        for l in data_graph:
            if(l["percentage_category"] > k):
                tmp_graph.append("o")
            else:
                tmp_graph.append(" ")
        graph += str(k).rjust(3) + "| " + "  ".join(tmp_graph) + "  \n"
        tmp_graph = []

    # Horizontal Lines of the Graph
    horizontal_line = "    -" + "---" * len(data_graph) + "\n"

    # Create Vertical Names Category

    # Get max lenght of name category
    max_len_category = max([len(m["category_name"]) for m in data_graph])

    # Create a list with names of categorys
    category_names = [n["category_name"].ljust(max_len_category) for n in data_graph]

    # Put each character of vertical names in his position
    tmp_names = []
    vertical_names = ""

    for m in range(max_len_category):
        for n in category_names:   
            tmp_names.append(n[m])
        vertical_names += " " * 5 + "  ".join(tmp_names) + "  "
        if m != max_len_category - 1:
            vertical_names += "\n"
        tmp_names = []

    return title + graph + horizontal_line + vertical_names