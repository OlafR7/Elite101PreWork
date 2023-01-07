if __name__ == '__main__':
  comp_response = 'Hello, wellcome to the restaurant. If you want you can make a reservation. You can also ask about specials and the menu or you can just order if you\'re ready\n'
  while(True):
    user_response = input(comp_response)
    if(user_response == 'q'):
      break
    