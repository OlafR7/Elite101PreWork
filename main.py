def reply(string):
  string = string.lower()
  if 'reservation' in string:
    input('Okay can you give a name for the reservation.\n')
    input('Now I just need the time.\n')
    return 'Thank you for your cooperation. Is there anything else you need?\n'
  if 'specials' in string:
    return'Our specials include a steak dinner for a lower price along with a drink of your choice.\n'
  if 'menu' in string:
    return 'Our menu include a collections of meals including burgers, steak, a collection of soft drinks and more.\n'
  if 'order' in string:
    input('Okay what would you like to order.\n')
    return 'Okay that will be out to you soon. Do you need anything else?\n'

  return 'Do you need anything else?\n'

  
if __name__ == '__main__':
  comp_response = 'Hello and welcome to the restaurant. I am here to help you make or confirm reservations, see the menu and specials, and even order.\n'
  while(True):
    user_response = input(comp_response)
    if(user_response == 'q'):
      break
    comp_response = reply(user_response)

