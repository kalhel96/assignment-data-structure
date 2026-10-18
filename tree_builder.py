class EmployeeNode:
    '''
    A class to represent a node in the binary tree.
    Attributes:
        name (str): The name of the employee.
        left (EmployeeNode): The left child node, representing the left subordinate.
        right (EmployeeNode): The right child node, representing the right subordinate.
    '''

    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None


class TeamTree:
    '''
    A class to represent a binary tree for managing a team structure.
    Attributes:
        root (EmployeeNode): The root node of the tree, representing the team lead.
    Methods:
        insert(manager_name, employee_name, side, current_node=None): Inserts a new employee under the specified manager.
        print_tree(node=None, level=0): Prints the tree structure starting from the given node.

    '''

    def __init__(self):
        self.root = None

    def insert(self, manager_name, employee_name, side, current_node=None):
        # If current_node is None, start at the root
        if current_node is None:
            if self.root is None:
                print("❌ The team is empty. Add a team lead first.")
                return False
            side = side.strip().lower()
            if side not in ("left", "right"):
                print(f"❌ '{side}' is not a valid side. Please choose LEFT or RIGHT.")
                return False
            current_node = self.root

        # Base case: this is the manager we are looking for
        if current_node.name == manager_name:
            if side == "left":
                if current_node.left is None:
                    current_node.left = EmployeeNode(employee_name)
                    print(f"✅ {employee_name} added to the LEFT of {manager_name}")
                else:
                    print(f"❌ {manager_name} already has {current_node.left.name} on the LEFT.")
            else:
                if current_node.right is None:
                    current_node.right = EmployeeNode(employee_name)
                    print(f"✅ {employee_name} added to the RIGHT of {manager_name}")
                else:
                    print(f"❌ {manager_name} already has {current_node.right.name} on the RIGHT.")
            return True

        # Recursive case: search the left side, then the right side
        found = False
        if current_node.left:
            found = self.insert(manager_name, employee_name, side, current_node.left)

        if not found and current_node.right:
            found = self.insert(manager_name, employee_name, side, current_node.right)

        # Print "not found" only once, at the root
        if not found and current_node is self.root:
            print(f"❌ Manager '{manager_name}' was not found in the team.")

        return found

    def print_tree(self, node=None, level=0):
        if node is None:
            if level == 0:
                node = self.root
                if node is None:
                    print("The team is empty.")
                    return
            else:
                return  # reached a leaf's child

        indent = "  " * level
        print(f"{indent}- {node.name}")

        self.print_tree(node.left, level + 1)
        self.print_tree(node.right, level + 1)


# Test your code here
employee_1 = EmployeeNode("John")
print(employee_1.name)   # John
print(employee_1.left)   # None
print(employee_1.right)  # None

company_directory_test = TeamTree()
print(company_directory_test.root)  # None

company_directory_test.root = EmployeeNode("Ms. Manager")
company_directory_test.insert("Ms. Manager", "Employee #1", "right")
company_directory_test.insert("Ms. Manager", "Employee #2", "left")
print(company_directory_test.root.right.name)  # Employee #1
print(company_directory_test.root.left.name)   # Employee #2

company_directory_test = TeamTree()
company_directory_test.root = EmployeeNode("Jordan")
company_directory_test.insert("Jordan", "Taylor", "right")
company_directory_test.insert("Jordan", "Riley", "left")
company_directory_test.insert("Riley", "Dana", "right")
company_directory_test.insert("Riley", "Morgan", "left")
company_directory_test.print_tree()


# CLI functionality
def company_directory():
    tree = TeamTree()

    while True:
        print("\n📋 Team Management Menu")
        print("1. Add Team Lead (root)")
        print("2. Add Employee")
        print("3. Print Team Structure")
        print("4. Exit")
        choice = input("Choose an option (1–4): ")

        if choice == "1":
            if tree.root:
                print("⚠️ Team lead already exists.")
            else:
                name = input("Enter team lead's name: ")
                tree.root = EmployeeNode(name)
                print(f"✅ {name} added as the team lead.")

        elif choice == "2":
            manager = input("Enter the manager's name: ")
            employee = input("Enter the new employee's name: ")
            side = input("Should this employee be on the LEFT or RIGHT of the manager? ")
            side = side.lower()
            tree.insert(manager, employee, side)

        elif choice == "3":
            print("\n🌳  Current Team Structure:")
            tree.print_tree()

        elif choice == "4":
            print("Good Bye!")
            break
        else:
            print("❌ Invalid option. Try again.")


company_directory()


'''
Design Memo
-----------
How did recursive insertion work?
The insert() method starts at the root (the team lead). At each
person, it asks: "Is this the manager I am looking for?" If yes,
this is the base case. The method checks if the left or right side is empty.
If it is, it adds a new EmployeeNode there. If the person is
not the manager, the method calls itself on the left child, and then on the
right child. Each call returns True or False, so the search stops when the
manager is found.

What challenges did you face when finding the right spot?
The first challenge was the error messages. Because the method calls itself
many times, the "manager not found" message could print many times. I fixed
this by printing it only at the root. The second challenge was a side that is
already taken. Then the method prints an error and keeps the old employee.

When might trees be better than other data structures?
A list can only go in a straight line, but a tree can branch. Trees are good
for data with parent and child relationships, like a company team, folders
on a computer, the parts of a web page (the DOM), or an adaptive quiz.
'''