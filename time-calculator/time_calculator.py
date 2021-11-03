def add_time(start, duration,day=str()):
  day=day.lower()


  time,s_half=start.split(" ")
  s_h,s_min=time.split(":")
  d_h,d_min=duration.split(":")
  d=0

  # calculate new time
  if s_half.lower()=='pm':
    s_h= int(s_h) + 12
  min=int(s_min) + int(d_min)
  h = int(s_h) + int(d_h) + min//60
  min %= 60
  if h > 24:
    d =h//24
    h %=24

  #change AM PM as necessary
  if h >= 12:
    AmPm = ' PM'
    h -= 12
  else:
    AmPm = ' AM'
  if h== 0:
    h+=12
  days = ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday',
            'sunday')
  # calulate end day
  output= str(h)+':'+ str(min).zfill(2)+ AmPm
  if day!='':
    start_day=days.index(day)
    end_day=(start_day + d)%7
    output= str(h)+':'+ str(min).zfill(2)+ AmPm + ', '+ days[end_day].title()

  
  nr_days = ()
  if d == 1:
    output= str(h)+':'+ str(min).zfill(2)+ AmPm + ' (next day)'
    if day!='':
      output= str(h)+':'+ str(min).zfill(2)+ AmPm +', ' +days[end_day].title() + ' (next day)'
  elif d > 1: 
    output= str(h)+':'+ str(min).zfill(2)+ AmPm + ' (' + str(d) + ' days later)'
    if day!='':
      output= str(h)+':'+ str(min).zfill(2)+ AmPm +', ' +days[end_day].title() + ' (' + str(d) + ' days later)'

  return output

