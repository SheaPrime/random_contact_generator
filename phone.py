import faker

fake = faker.Faker()

phone_numbers = [fake.phone_number() for _ in range(5000)]

# Print the first 10 phone numbers
for number in phone_numbers[:10]:
    print(number)
