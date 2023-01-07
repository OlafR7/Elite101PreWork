def reply(string):
  string = string.lower()
  if 'reservation' in string:
    input('Okay can you give a name for the reservation.')
    input('Now I just need the time.')
    return 'Thank you for your cooperation. Is there anything else you need?'
  if 'specials' in string:
    return'Our specials include a steak dinner for a lower price along with a drink of your choice.'
  if 'menu' in string:
    return 'Our menu include a collections of meals including burgers, steak, a collection of soft drinks and more.'
  if 'order' in string:
    input('Okay what would you like to order.')
    return 'Okay that will be out to you soon. Do you need anything else?'

  return 'Do you need anything else?'

  
if __name__ == '__main__':
  comp_response = 'Hello, wellcome to the restaurant. If you want you can make a reservation. You can also ask about specials and the menu or you can just order if you\'re ready\n'
  while(True):
    user_response = input(comp_response)
    if(user_response == 'q'):
      break
    reply(user_response)

