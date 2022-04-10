# Defining a fuction using mutiple return statements and the title functio
def format_name():

  f_name=input('What is your first name?\n')
  l_name=input('What is your last name?\n')
  
  if f_name == '' or l_name == '':
    return 'Error both first and last name are needed.'  
  return f'{f_name} {l_name}'.title()

full_name = format_name()
print(full_name)
