employees= [
{'id':'001','name':'Mary','pay_rate':15.00,'hours':40},
{'id':'002','name':'John','pay_rate':22.00,'hours':25},
{'id':'003','name':'Bob','pay_rate':35.00,'hours':4},
{'id':'004','name':'Mel','pay_rate':43.00,'hours':62}
]


for employee in employees:
	if employee['hours']>40:
	   salary=(40*employee['pay_rate'])+((employee['hours']-40)*(1.5*employee['pay_rate']))
	
	else:
		salary=employee['pay_rate']*employee['hours']
	#print()

	print(employee['name']+": $", salary )
	 