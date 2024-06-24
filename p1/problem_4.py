class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name

# Function to check if the user is in the group or its subgroups
def is_user_in_group(user, group):
    if user in group.get_users():
        return True
    for sub_group in group.get_groups():
        if is_user_in_group(user, sub_group):
            return True
    return False

# Test Cases

# Test Case 1: Check if "sub_child_user" is in the parent group
parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)

print(is_user_in_group("sub_child_user", parent))  # Expected output: True

# Test Case 2: Check if a non-existent user is in the parent group
print(is_user_in_group("non_existent_user", parent))  # Expected output: False

# Test Case 3: Check if a user in a deeply nested subgroup is found
deep_nested_group = Group("deep_nested")
deep_user = "deep_user"
deep_nested_group.add_user(deep_user)
sub_child.add_group(deep_nested_group)

print(is_user_in_group("deep_user", parent))  # Expected output: True

# Edge Case 1: Check with an empty group
empty_group = Group("empty")
print(is_user_in_group("any_user", empty_group))  # Expected output: False

# Edge Case 2: Check with None as user
print(is_user_in_group(None, parent))  # Expected output: False

# Edge Case 3: Large group with many users and subgroups
large_group = Group("large")
for i in range(1000):
    user = f"user_{i}"
    large_group.add_user(user)
    sub_group = Group(f"subgroup_{i}")
    large_group.add_group(sub_group)

print(is_user_in_group("user_999", large_group))  # Expected output: True
print(is_user_in_group("user_1000", large_group))  # Expected output: False
