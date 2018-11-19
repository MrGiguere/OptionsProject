class OptionsContract:
  def __init__ (self,ticker,strikePrice,contractPrice,underlyingPrice,daysToExpiration):
    self.ticker = ticker
    self.strikePrice = strikePrice
    self.contractPrice = contractPrice
    self.underlyingPrice = underlyingPrice
    self.daysToExpiration = daysToExpiration
    
  def quote(self):
    print("This is a $" + str(self.strikePrice)+" call for $"+self.ticker+".")
    print(self.ticker+" currently trades at $"+str(self.underlyingPrice)+" per share, and the contract is worth $"+str(self.contractPrice)+".")
    print("The option expires in "+str(self.daysToExpiration)+" days.")
    
  def changePrice(self,price):
    self.contractPrice = price

  def moneyness(self):
    if self.strikePrice > self.underlyingPrice:
      intrinsicValue = self.underlyingPrice-self.strikePrice
      print("The contract is in the money and has an intrinsic value of "+str(intrinsicValue)+'.')
      print("It's time value is "+str(self.contractPrice-intrinsicValue)+'.')
    else:
      print("The contract is out of the money and has a time value of"+str(self.contractPrice)+'.')
  
  def decay(self):
    self.daysToExpiration = self.daysToExpiration-1

  def weekly(self):
    if self.daysToExpiration <= 5:
      print("This contract is a weekly contract and will expire soon.")
    else:
      print("This is not a weekly contract.")

MU181123C00038500 = OptionsContract('MU', 38.5, 1.45, 39.44, 5)
MU181123C00038500.quote()
MU181123C00038500.moneyness()
MU181123C00038500.weekly()
MU181123C00038500.decay()
MU181123C00038500.quote()

MU200117C00090000 = OptionsContract('MU', 90, 0.45, 39.44, 428)
MU200117C00090000.quote()
MU200117C00090000.moneyness()
MU200117C00090000.weekly()

GE210115C00025000 = OptionsContract('GE', 25, 0.19, 8.02, 792)
GE210115C00025000.quote()
GE210115C00025000.moneyness()
GE210115C00025000.weekly()
