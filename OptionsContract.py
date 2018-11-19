class OptionsContract:
  def __init__ (self,ticker,strikePrice,contractPrice,underlyingPrice,daysToExpiration):
    self.ticker = ticker
    self.strikePrice = strikePrice
    self.contractPrice = contractPrice
    self.underlyingPrice = underlyingPrice
    self.daysToExpiration = daysToExpiration
    
  def quote(self):
    print("This is a $" + str(self.strikePrice)+" for $"+self.ticker+".")
    print(self.ticker+" currently trades at $"+str(self.underlyingPrice)+" per share, and the contract is worth $"+str(self.contractPrice)+".")
    print("The option expires in "+str(self.daysToExpiration)+" days.")

  
  def moneyness(self):
    if self.strikePrice > self.underlyingPrice:
      intrinsicValue = self.underlyingPrice-self.strikePrice
      print("The contract is in the money and has an intrinsic value of "+str(intrinsicValue)+'.')
      print("It's time value is "+str(self.contractPrice-intrinsicValue)+'.')
    else:
      print("The contract is out of the money and has a time value of"+str(self.contractPrice)+'.')
  
  def decay(self):
    self.daystoExpiration = self.daystoExpiration-1

  def weekly(self):
    if self.daystoExpiration <= 5:
      print("This contract is a weekly contract and will expire soon.")
    else:
      print("This is not a weekly contract.")
      
