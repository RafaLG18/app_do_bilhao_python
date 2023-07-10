import streamlit as st
import yfinance as yf
import plotly.graph_objects as go
import numpy as np

# Título do App
st.title('Stock History App')
st.sidebar.title('Selecione o stock')

ticker_symbol=st.sidebar.text_input('stock','AAPL',max_chars=10)

# Baixando os dados
data=yf.download(ticker_symbol,start='2020-01-01',end='2023-06-26')

# Implementando RSI

data['PriceDiff'] = data['Close'].diff()

data['Gain'] = np.where(data['PriceDiff'] > 0, data['PriceDiff'], 0)
data['Loss'] = np.where(data['PriceDiff'] < 0, abs(data['PriceDiff']), 0)

data['AvgGain'] = data['Gain'].rolling(window=30).mean()
data['AvgLoss'] = data['Loss'].rolling(window=30).mean()

data['RS'] = data['AvgGain'] / data['AvgLoss']
data['RSI'] = 100 - (100 / (1 + data['RS']))

# Exibindo os dados
st.subheader('HIstorico')
st.dataframe(data)

# Plot o grafico
fig=go.Figure()
fig.add_trace(go.Scatter(x=data.index,y= data['Close'],name= 'Fechamento'))
fig.update_layout(title=f"{ticker_symbol}",xaxis_title = "Date", yaxis_title = "Preço")
st.plotly_chart(fig)

# Adicionando mais uma figura
fig=go.Figure()
fig.add_trace(go.Scatter(x=data.index,y= data['RSI'],name= 'RSI'))
fig.update_layout(title="RSI",xaxis_title = "Date")
st.plotly_chart(fig)