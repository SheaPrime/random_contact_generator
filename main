import random
import faker
from datetime import datetime, timedelta

fake = faker.Faker()

# Function to generate a random date of birth between 18 and 74 years ago
def random_dob():
    today = datetime.today()
    start_date = today - timedelta(days=365*74)
    end_date = today - timedelta(days=365*18)
    random_days = random.randint(0, (end_date - start_date).days)
    birth_date = start_date + timedelta(days=random_days)
    return birth_date.strftime('%m/%d/%Y')

#List of industries
# List of industries
industries = ["Technology", "Finance", "Healthcare", "Retail", "Manufacturing", "Hospitality", "Education", "Media", "Transportation", "Real Estate"]

# Function to generate random 10-digit phone numbers that begin with "555"
def generate_phone_number():
    return '555' + ''.join([str(random.randint(0, 9)) for _ in range(7)])

# Generate 5000 rows of random data
rows = []
for _ in range(5000):
    first_name = fake.first_name()
    last_name = fake.last_name()
    #middle_name = fake.first_name()
    #access_card = ''.join([str(random.randint(0, 9)) for _ in range(10)])
    #sso = ""
    email_address = f"{first_name.lower()}.{last_name.lower()}.@tbxofficial.com"
    address_line_1 = fake.street_address()
    #address_line_2 = ""
    city = fake.city()
    state = fake.state_abbr()
    zip_code = fake.zipcode()
    country = "USA"
    home_phone = generate_phone_number()
    #cell_phone = generate_phone_number()
    #work_phone = generate_phone_number()
    #emergency_phone = generate_phone_number()
    #emergency_contact = fake.name()
    #gender = random.choice(["Male", "Female"])
    #birth_date = random_dob()
    #user_name = email_address
    #home_club = ""
    #company_name = f"{first_name} {last_name} Tech Solutions"
    #website = f"www.{first_name}{last_name}TechSolutions.com"
    #company_size = str(random.randint(15,1023))

    row = [first_name, last_name, email_address, address_line_1, city, state, zip_code, country, home_phone]
    rows.append(row)

# Print the first 5 rows
for row in rows[:856]:
    print(', '.join(row))
