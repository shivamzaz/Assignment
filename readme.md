# Assignment Solution:

##Step 1

First of all i made a pivot table, where i store the product and respective price corresponding to the Userid like this format:

{
 Userid : 
    {
      Product : Price
    }
}

Note: i'll save the data corresponding to the command line user inputs (for products) in the pivot table

Example data format: for example user gives products (In command line arguments): "teddy_bear baby_powder" then it'll only sum the targeted value(User Input) and store in another list (which'll store in format of tuple (User_id: sum_Of_Given_Product_Price))

{
   '1': 
      {
      	'teddy_bear': ' 4.00',
      	'baby_powder': ' 8.00'
      },
   '3': 
      {
      	'johnson_wipes': ' 8.00', 
      	'pampers_diapers': ' 4.00'
      }, 
   '2': 
      {
      	'teddy_bear': ' 5.00', 
      	'baby_powder': ' 6.50'
      },
   '5': 
      {
      	'bath_towel': ' 4.00', 
      	'scissor': ' 8.00'
      },
   '4':
      {
      	'johnson_wipes': ' 5.00', 
      	'cotton_buds': ' 2.50'
      },
   '6': 
      {
      	'powder_puff': ' 6.00', 
      	'scissor': ' 5.00', 
      	'cotton_balls': ' 6.00', 
      	'bath_towel': ' 6.00'
      }
}

## Step 2 our final list will store the data in this format:   {user_id : sum}



{
   '1': 
      {
      	12
      },
   '3': 
      {
      	12
      }, 
   '2': 
      {
      	11.5
      },
   '5': 
      {
      	12
      },
   '4':
      {
      	7.50
      },
   '6': 
      {
      	23
      }
}
In above i'm making the list of tuples where i'll store the sum corresponding to the User_id, then will pick the min value from that(only if the user given(input) products exists in the existing data.csv )


##Step 3
In the final Step i'll find the minimum value from the list based of value (key,value). 



		
