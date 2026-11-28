# shooping card management
class shoppingcart:
   def init (self):
     self.customer_name = ""
     self.product_name = ""
     self.price = 0
     self.quantity = 0
     self.total = 0
     self.discount = 0
     self.final_bill =0

   def set_details(self): 
      self.customer_name = input("mansi chavan")
      self.product_name = input ("lenovo")
      self.price = 56000
      self.quantity = 5

   def calculate_total(self):
      self.total=self.price * self.quantity
      print("total amount:",self.total)

   def apply_discount(Self):
       if self.total > 5000:
         self.discount =self.total* 0.10
       else: 
          self.discount = 0 

       self.final_bill = self.total - self.discount    

   def display_bill(self):
      print("----shopping bill-----")  
      print("customer name:",self.customer_name) 
 