from pandas_datareader import data
import pandas,datetime
from bokeh.plotting import figure,show,output_file

start=datetime.datetime(2017,9,1)
end=datetime.datetime(2017,9,15)

df=data.DataReader(name="AAPL",data_source="yahoo",start=start,end=end)

print(df)

p=figure(x_axis_type="datetime",width=1000,height=300,responsive=True)
print(df.index[df.Close>df.Open])
CS="Candle Chart"
#p.title(CS)
p.grid.grid_line_alpha=0.3

hours=12*60*60*1000
p.rect(df.index[df.Close>=df.Open],(df.Open+df.Close)/2,hours,abs(df.Open-df.Close),fill_color="red",line_color="black")
p.rect(df.index[df.Close<df.Open],(df.Open+df.Close)/2,hours,abs(df.Open-df.Close),fill_color="blue",line_color="black")
p.segment(df.index,df.High,df.index,df.Low,color="Black")
output_file("cs.html")
show(p)