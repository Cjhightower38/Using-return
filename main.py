# Defining a fuction using the return statement and the title function.
def format_name():
  
  f_name=input('What is your first name?\n')
  l_name=input('What is your last name?\n')
  return f'{f_name} {l_name}'.title()

full_name=format_name()
print(full_name)
