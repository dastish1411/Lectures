class Phone:
  

  def __init__(self, name, last_name, num):
    self.name = name
    self.last_name = last_name
    self.num = num

  def get_info(self):
    return f'Контакт: {self.name} {self.last_name}, {self.num}'

phone = Phone('Ivan', 'Petrov', '+996770645418' )
print(phone.get_info())