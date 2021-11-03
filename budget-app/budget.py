class Category:
      def __init__(self, category: str):
        self.name = category
        self.ledger = list()
        self.runningBalance = 0

      def deposit(self,amount,description=""):
        self.ledger.append({"amount": amount, "description": description}) 
        self.runningBalance=self.runningBalance+amount   
      def check_funds(self,amount):
        if amount > self.runningBalance:
          return(False)
        else:
          return(True)

      def withdraw(self, amount, description=""):
        if self.check_funds(amount)==True:
          self.ledger.append({"amount": amount * -1, "description": description})
          self.runningBalance=self.runningBalance-amount
          return(True)
        else:
          return(False)

      def get_balance(self):
        return(self.runningBalance)

      def transfer(self, amount, destination):
        if self.check_funds(amount) == True:           
          self.withdraw(amount, str( "Transfer to " + destination.name ))
          destination.deposit( amount,str("Transfer from " + self.name) )
          return(True)
        else: 
          return (False)

      def __str__(self):
        title=self.name.center(30,'*')

        running_title=str()
        for item in self.ledger:
          a=str(item['description'])
          b=item['amount']
          if len(a)>23:
            a=a[0:23]
          filler=30-len(a)
          b="{:.2f}".format(b)
          b=b.rjust(filler)
          running_title=running_title+'\n'+a+b

        total="{:.2f}".format(self.runningBalance)
        total_line= "\nTotal: "+total

        
        return(title+running_title+total_line)


def create_spend_chart(input):
  import pandas as pd
  import math
  percent=[]
  names=[]
  for categories in input:
    names.append(categories.name)
    df = pd.DataFrame(categories.ledger)
    df1=df['amount'].astype(float)
    #sum_pos = df1[df1>0].sum(0)
    sum_neg = df1[df1<0].sum(0)
    #percent.append(sum_neg/sum_pos)
    #print(sum_pos,sum_neg)
    #percent.append(abs(round((sum_neg/sum_pos)*100,-1)))
    percent.append(sum_neg)

  pec_total=sum(percent)
  print(pec_total,percent)
  percentage=[]
  for i in percent:
    percentage.append(abs(math.floor((i/pec_total)*100)))

    #number / 10) * 10

  percent= percentage
  
  
  


  title="Percentage spent by category\n"
 
  curr_line=str()
  
  total_len=len(percent)*3+1
  for n in range(100,-1,-10):
    temp=[i for i,v in enumerate(percent) if v >= n]
    line=total_len*" "
    line1 = list(line)
    for i in temp:
      line1[i*3+1]='o'
    
    line = ''.join(line1)  
    curr_line=curr_line+str(n).rjust(3)+"|"+line+'\n'

  max_length,longest_element = max([(len(x),x) for x in names])
  ax_names=[]
  for n in names:
    ax_names.append(n.ljust(max_length))

  test=[]
  for i in range(0,max_length):
    test.append('     ')
    for j in ax_names:
    
      test.append(j[i]+'  ')
    test.append('\n')


  ax_out=''.join(test)
  output=title+curr_line+4*" "+total_len*"-"+'\n' + ax_out

  return(output[:-1])
