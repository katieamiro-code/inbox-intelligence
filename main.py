print ("Inbox Itelligence is starting...")
email_text=input("paste an email here:") 
print("Email received:", email_text)           
if "order" in email_text.lower():
    print("Category: Order/Shipping")      
     
elif "payment" in email_text.lower():
 print("category: Bill/Payment") 
elif "urgent" in email_text.lower():
 print("category: Urgent")
else:
  print("category: other")