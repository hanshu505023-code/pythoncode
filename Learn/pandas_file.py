import pandas as pd

file = 'C://Users//Admin//PycharmProjects//Learn_python//names.xlsx'

df = pd.read_excel(str(file))

print(df['Name'].iloc["1","2","3"])


