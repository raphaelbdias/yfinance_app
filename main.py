import streamlit as st
import yfinance as yf
import plotly.graph_objects as go
import json
from datetime import datetime, timedelta

def main():
    st.title('Stock Analysis')

    option = st.selectbox('Select Stock', ['Microsoft', 'Apple'])

    graphJSON = ''

    if option == 'Microsoft':
        d_30 = datetime.today() - timedelta(days=30)
        msft = yf.Ticker("MSFT")
        df = msft.history(start=d_30).reset_index()
        fig = go.Figure(data=[
            go.Candlestick(x=df['Date'],
                           open=df['Open'],
                           high=df['High'],
                           low=df['Low'],
                           close=df['Close'])
        ])
        fig.update_layout(
            xaxis_rangeslider_visible=False,
            title_text='Microsoft Stock Analysis for the last 30 days',
            yaxis_title='MSFT Stock',
            xaxis_title='Dates'
        )
        graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    elif option == 'Apple':
        d_30 = datetime.today() - timedelta(days=30)
        apple = yf.Ticker("AAPL")
        df = apple.history(start=d_30).reset_index()
        fig = go.Figure(data=[
            go.Candlestick(x=df['Date'],
                           open=df['Open'],
                           high=df['High'],
                           low=df['Low'],
                           close=df['Close'])
        ])
        fig.update_layout(
            xaxis_rangeslider_visible=False,
            title_text='Apple Stock Analysis for the last 30 days',
            yaxis_title='AAPL Stock',
            xaxis_title='Dates'
        )
        graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    st.plotly_chart(fig)

if __name__ == '__main__':
    main()
