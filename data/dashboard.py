import streamlit as st
import pandas as pd
import plotly.express as px

st.title('FMCG Sales Analytics Dashboard')

df=pd.read_csv('FMCG_2022_2024.csv')
df['date']=pd.to_datetime(df['date'])

region_filter=st.selectbox('Select Region',options=['All']+list(df['region'].unique()))

if region_filter!='All':
   df=df[df['region']==region_filter]


st.write('Dataset preview:')

df['month']=df['date'].dt.month
df['year']=df['date'].dt.year


monthly_sales = df.groupby(['year', 'month'])['units_sold'].sum().reset_index()


monthly_sales['date_label'] = monthly_sales['year'].astype(str) + '-' + monthly_sales['month'].astype(str)


st.dataframe(monthly_sales.head())
f1=px.line(monthly_sales,x='date_label',y='units_sold',title='Monthly Units Sold')
st.plotly_chart(f1)

cat=df.groupby('category')['units_sold'].sum().reset_index()
f2=px.bar(cat,x='category',y='units_sold',title='Sales by Category')
st.plotly_chart(f2)

cat3=df.groupby('promotion_flag')['units_sold'].mean().reset_index()
cat3['promotion_flag']=cat3['promotion_flag'].map({0:'No promotion',1:'promotion'})
f3=px.bar(cat3,x='promotion_flag',y='units_sold',title='promotion')
st.plotly_chart(f3)




