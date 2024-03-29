class Policy:
    def __init__(self, some_policy):
        numeric_requirement = str(some_policy).rsplit(' ')[0]

        self.enforced_char = str(some_policy).rsplit(' ')[1]
        self.min_char = int(numeric_requirement.rsplit('-')[0])
        self.max_char = int(numeric_requirement.rsplit('-')[1])

    def validate_password(self, password):
        if self.enforced_char not in password:
            return False
        # xor password match ^: According to the new rules...
        # We only want one char match in a location, not both!
        if bool(password[self.min_char - 1] == self.enforced_char) ^ \
                bool(password[self.max_char - 1] == self.enforced_char):
            return True
        else:
            return False


# input_file = "testInput.txt"
input_file = "Input.txt"

user_input = open(input_file).readlines()

valid_passwords = 0
for line in user_input:
    # Chop up password and policy
    raw_policy = line.rsplit(':')[0]
    raw_password = line.split(':')[1].strip()

    # Make a policy object
    policy = Policy(raw_policy)
    valid_passwords += policy.validate_password(raw_password)

print(valid_passwords, "valid password(s)")
