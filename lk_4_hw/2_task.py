from datetime import datetime

data = 'Feb 12 2019 2:41PM'
convert_data = datetime.strptime(data, '%b %d %Y %I:%M%p')
print(convert_data)
