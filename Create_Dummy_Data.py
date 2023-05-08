# Istall Faker module in your system if it is not already in your system
# Sometime this module showes error in this case first uninstall Faker by using commind(pip uninstall Faker)
# After that install it again by using command(pip install Faker)

from faker import Faker 
fake = Faker() 
print(fake.name())
print(fake.address())
print(fake.text()) 