from faker import Faker

sample = Faker()

# using some functions
print("Your Name: ", sample.name())
print("Your Date of Birth: ", sample.date_of_birth())
print("Your Address: ", sample.address())
print("Your Country: ", sample.country())
print("Your E-mail Address: ", sample.email())
