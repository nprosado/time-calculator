def add_time(start, duration, day=''):
  
  start_0 = start.split()[0]
  (start_hr, start_min) = start_0.split(':')
  (start_hr, start_min) = (int(start_hr), int(start_min))

  start_1 = start.split()[1]
  if start_1 == 'PM':
    start_hr = start_hr + 12

  (duration_hr, duration_min) = duration.split(':')
  (duration_hr, duration_min) = (int(duration_hr), int(duration_min))

  (new_hr, new_min) = (start_hr + duration_hr, start_min + duration_min)

  if new_min > 59:
    new_hr += 1
    new_min %= 60 
    
  week = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
  if day != '':
    day_index = week.index(day.casefold())  
    
  new_2 = ''
  new_3 = ''

  if new_hr >= 24:
    n = int(new_hr/24)
    new_hr %= 24
    
    if day != '':
      day_index += n
      
    if n == 1:
      new_3 = '(next day)'
    else:
      new_3 = '({} days later)'.format(n)
  
  if day != '':    
    day_index %= 7
    new_2 = week[day_index].capitalize()    
        
  if new_hr > 12:
    new_hr %= 12
    new_1 = 'PM'
  elif new_hr == 12:
    new_1 = 'PM'
  else:
    new_1 = 'AM'

  if new_hr == 0:
      new_hr += 12

  new_hr = str(new_hr)
  
  if new_min < 10:
    new_min = str(new_min)
    new_min = '0' + new_min
  else:
    new_min = str(new_min)

  new_time = ':'.join((new_hr, new_min))
  new_time = ' '.join((new_time, new_1))
  
  if new_2 != '':
    new_time = ', '.join((new_time, new_2))

  if new_3 != '':    
    new_time = ' '.join((new_time, new_3))

  return new_time