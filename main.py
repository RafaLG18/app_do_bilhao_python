import streamlit as st
import yfinance as yf
import plotly.graph_objects as go

# Título do App
st.title('Stock History App')
st.sidebar.title('Selecione o stock')

ticker_symbol=st.sidebar.text_input('stock','AAPL',max_chars=10)

# Baixando os dados
data=yf.download(ticker_symbol,start='2020-01-01',end='2023-06-26')

# Exibindo os dados
st.subheader('HIstorico')
st.dataframe(data)

# Plot o grafico
fig=go.Figure()
fig.add_trace(go.Scatter(x=data.index,y= data['Close'],name= 'Fechamento'))
fig.update_layout(title=f"{ticker_symbol}",xaxis_title = "Date", yaxis_title = "Preço")
st.plotly_chart(fig)