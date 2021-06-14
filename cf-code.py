from cloudant.client import Cloudant
from cloudant.error import CloudantException
from cloudant.result import Result, ResultByKey


def main(dict):
    res=""
    client = Cloudant.iam(dict['username'], dict['apikey'], connect=True)
   
   
    
    # if user is asking about account
    if (dict['action']=="account"):
        res= getAccount(dict, client)
        
    elif (dict['action']=="booking"):
        res= saveBooking(dict, client)
     
    #return response   
    return { 'response': res }
    
  

def getAccount(dict, client):
    databaseName = "users-db"
    myDb = client.create_database(databaseName)
    if myDb.exists():
        print("'{0}' successfully created.\n".format(databaseName))
    
    account_id = str(dict['accountID'])
    if account_id in myDb:
        doc = myDb[account_id]
        name = doc['name']
        balance = doc['balance']
   
        response="Welcome "+ name+"\nAccount No: "+account_id+ "\nCurrent Balance: "+ str(balance)+" Points"
        
    else:
        response= "Incorrect credentials"
     
    return  response

    
def saveBooking(dict, client):
   
    response= ""
    myDb = client.create_database("booking-db")
    if myDb.exists():
        print("successfully created")
        date = dict['booking_date']
        time= dict['booking_time']
        num_people = dict['num_people']
        phone = dict['booking_phone'] 
        
        data = {
            'num_people': num_people,
            'booking_time': time,
            'booking_date': date,
            'booking_phone': phone  
            }
    
        # Create a document using the Database API
        doc = myDb.create_document(data)

        # Check that the document exists in the database
        if doc.exists():
            print('SUCCESS!!')
            response= "Booking is confirmed on "+ date +" at "+ time + " for "+ str(num_people)+  " people.Thank you."
        else:
            response = "Something happened. Please try again"
      
    return response    
    
