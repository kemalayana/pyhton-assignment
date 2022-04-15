import random
def password_generator(digits):
      password = []
  for i in range(digits):
    chars = [
  chr(random.randint(65, 90)),
  chr(random.randint(92, 122)),
  chr(random.randint(48, 57)),
  chr(random.randint(33, 47)),
  chr(random.randint(58, 64))
  ]
    password.append(random.choice(chars))
  
  random.shuffle(password)
  new_password = ''.join(password)
  return new_password