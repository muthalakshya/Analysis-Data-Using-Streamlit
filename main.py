import pandas as pd
import streamlit as st
import plotly.express as px

st.title("Hello Geeks: Welcome to visualization")

st.markdown('## Upload  File only in csv')
csv_path = st.file_uploader('Upload your image', type=['csv'])


if not csv_path:
    st.warning("Please upload file")
    st.stop()

df = pd.read_csv(csv_path)


st.title("Null Value")
st.write(df.isnull().sum())
df = df.dropna()

col=df.columns
typ=df.dtypes
sel = []

k=0
sel_dic={}
for i,j in typ.items():

    if(j=='int64' or j=='float64'):
        sel.append(i)
        sel_dic[i]=k
    k+=1



st.subheader('Select Any 2 column')
options = st.multiselect('Select your options:', options=sel, help='Choose One', max_selections=2)

if len(options)!=2:
    st.warning("Please upload file")
    st.stop()

select1 = options[0]
select2 = options[1]


st.dataframe(df)


st.title("Top 5 entry")
st.table(df.head())

st.title("Bottom 5 entry")
st.table(df.tail())



# Bar chart
bar_chart = px.bar(df, x=select1, y=select2, color=select1, title=f'Bar Chart: {select1} vs {select2}')
# Scatter plot
scatter_plot = px.scatter(df, x=select1, y=select2, color=select1, title=f'Scatter Plot: {select1} vs {select2}')

st.title(f'Visualizations for {select1} vs {select2}')


st.subheader('Bar Chart')
st.plotly_chart(bar_chart)

st.subheader('Scatter Plot')
st.plotly_chart(scatter_plot)


box_plot_trade = px.box(df, y=df[select1], title=f'Box Plot: {select1} ')

st.title(f'Box Plots for {select1}')
st.plotly_chart(box_plot_trade)

corr_matrix = df.iloc[:,[i for i in sel_dic.values()]].corr()

fig = px.imshow(corr_matrix, text_auto=True, aspect="auto", title="Heat Map of Correlation Matrix")

# Streamlit app
st.title('Heat Map')
st.plotly_chart(fig)