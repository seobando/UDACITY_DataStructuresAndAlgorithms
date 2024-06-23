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


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    if user in group.get_users():
        return True
    for subgroup in group.get_groups():
        if is_user_in_group(user, subgroup):
            return True
    return False


# Test cases
if __name__ == "__main__":
    # Setup groups
    parent = Group("parent")
    child = Group("child")
    sub_child = Group("subchild")

    sub_child_user = "sub_child_user"
    sub_child.add_user(sub_child_user)

    child.add_group(sub_child)
    parent.add_group(child)

    # Test Case 1: User in nested subgroup
    assert is_user_in_group("sub_child_user", parent) == True  # should return True

    # Test Case 2: User not in any group
    assert is_user_in_group("non_existent_user", parent) == False  # should return False

    # Test Case 3: User in top-level group
    top_level_user = "top_level_user"
    parent.add_user(top_level_user)
    assert is_user_in_group(top_level_user, parent) == True  # should return True

    # Test Case 4: Edge case with empty group structure
    empty_group = Group("empty")
    assert is_user_in_group("any_user", empty_group) == False  # should return False

    # Test Case 5: Large number of nested groups
    large_group = Group("large")
    current_group = large_group
    for i in range(1000):
        new_group = Group(f"subgroup_{i}")
        current_group.add_group(new_group)
        current_group = new_group
    deep_user = "deep_user"
    current_group.add_user(deep_user)
    assert is_user_in_group(deep_user, large_group) == True  # should return True

    print("All test cases passed!")

