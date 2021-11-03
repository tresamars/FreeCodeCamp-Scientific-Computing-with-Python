def arithmetic_arranger(input,show_output=False): 

  temp=[]
  problem_top=str()
  problem_bottom=str()
  lines=str()
  res_line=str()
  
  problems=input
  if len(input)>1:
    if input[1]==True:
      show_output=input[1]
      problems=input[0]
  else:
    problems=input[0]

  if len(problems)>5:
    return ("Error: Too many problems.")
  
  for item in problems:

    temp=item.split(" ")
    max_length,longest_element = max([(len(x),x) for x in temp])
    
        #raise error is temp[0] or [2] contains non digits, or more than 4
    if not (temp[0].isdigit() and temp[2].isdigit()):
      return("Error: Numbers must only contain digits.")
    if (max_length>4):
      return("Error: Numbers cannot be more than four digits.")
    x,y=int(temp[0]),int(temp[2])
    if temp[1]=='+':
      z=x+y
    elif temp[1] =='-':
      z=x-y
    else:
      return("Error: Operator must be '+' or '-'.")

  #make sure that there is min 1 space between the symbol and the digits
    if longest_element==temp[2]:
      
      problem_top=problem_top+(temp[0].rjust(max_length+2)) +4*' '
      problem_bottom=problem_bottom+temp[1]+' '+(temp[2].rjust(max_length)) +4*' '
      lines=lines+(max_length+2)*'-'+4*' '
      res_line= res_line + str(z).rjust(max_length+2) + 4*' '

    elif max_length<(len(temp[1]+temp[2])+1):
      
      problem_top=problem_top+(temp[0].rjust(max_length+2)) +4*' '
      problem_bottom=problem_bottom+temp[1]+(temp[2].rjust(max_length+1)) +4*' '
      lines=lines+(max_length+2)*'-'+4*' '
      res_line= res_line + str(z).rjust(max_length+2) + 4*' '
    else:
      
      problem_top=problem_top+(temp[0].rjust(max_length+2)) +4*' '
      problem_bottom=problem_bottom+temp[1]+(temp[2].rjust(max_length+1)) +4*' '
      lines=lines+(max_length+2)*'-'+4*' '
      res_line= res_line + str(z).rjust(max_length+2) + 4*' '

  result=problem_top[:-4]+'\n'+problem_bottom[:-4]+'\n'+lines[:-4]
  if show_output==True:
    result=problem_top[:-4]+'\n'+problem_bottom[:-4]+'\n'+lines[:-4]+'\n'+res_line[:-4]
  return(result)

