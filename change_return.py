def change_return(m, c):
	m_c = m-c
	result = []
	last_result = []
	changes = [200, 100, 50, 20, 10, 5, 1, 0.5, 0.25, 0.10, 0.5, 0.01]

	#converts total change to changes which user will return
	for change in changes: 
		if m_c // change > 0:
			number_of_changes = m_c // change 
			m_c = m_c - number_of_changes * change
			result.append([number_of_changes, "x", change]) 
	
	#Now we know how many changes we need. But we still need to make it readable by user
	for inner_list in result:

		inner_list[0] = str(int(inner_list[0])) #number_of_changes is float number. we  convert it to int then convert to str for joining
		
		if inner_list[2] < 1: 
			inner_list[2] = inner_list[2] * 100 #now we convert 0.xx TRY to xx kuruş
			inner_list[2] = str(int(inner_list[2]))
			inner_list.append(" kuruş")
		else:
			inner_list[2] = str(int(inner_list[2]))
			inner_list.append(" TRY")


		last_result.append("".join(inner_list)) #Did you know changing inner_list won't change result list at all? I didn't


	return "You need to give back " + " ".join(last_result)
	


money = float(input("Type given money: "))
cost= float(input("Type total cost: "))

print(change_return(money,cost))
