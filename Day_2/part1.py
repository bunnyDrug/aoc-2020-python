def parse_policy(some_policy):
    numeric_requirement = str(some_policy).rsplit(' ')[0]

    class Policy:

        def __init__(self):
            self.enforced_char = str(some_policy).rsplit(' ')[1]
            self.min_char = int(numeric_requirement.rsplit('-')[0])
            self.max_char = int(numeric_requirement.rsplit('-')[1])

        def validate_password(self, password):
            if self.enforced_char not in password:
                return False
            if self.min_char <= int(password.count(self.enforced_char)) <= self.max_char:
                return True
            else:
                return False

    return Policy()


# input_file = "testInput.txt"
input_file = "Input.txt"

user_input = open(input_file).readlines()


valid_passwords = 0
for line in user_input:
    # Chop up password and policy
    raw_policy = line.rsplit(':')[0]
    raw_password = line.rsplit(':')[1]

    # Make a policy object
    policy = parse_policy(raw_policy)
    valid_passwords += policy.validate_password(raw_password)

print("There are", valid_passwords, "valid passwords")
