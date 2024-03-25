import streamlit as st
import yfinance as yf
from datetime import datetime, timedelta
import plotly.graph_objects as go

def main():
    st.title('Stock Analysis')

    option = st.selectbox('Select Stock', ['Microsoft', 'Apple'])

    start_date = st.date_input('Start Date', datetime.today() - timedelta(days=30))
    end_date = st.date_input('End Date', datetime.today())

    if start_date < end_date:
        if option == 'Microsoft':
            msft = yf.Ticker("MSFT")
            df = msft.history(start=start_date, end=end_date).reset_index()

        elif option == 'Apple':
            apple = yf.Ticker("AAPL")
            df = apple.history(start=start_date, end=end_date).reset_index()

        fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                                             open=df['Open'],
                                             high=df['High'],
                                             low=df['Low'],
                                             close=df['Close'])])

        fig.update_layout(xaxis_rangeslider_visible=False,
                          title=f'{option} Stock Analysis from {start_date} to {end_date}',
                          yaxis_title=f'{option} Stock',
                          xaxis_title='Dates')

        st.plotly_chart(fig)
    else:
        st.error('Error: End date must fall after start date.')

if __name__ == '__main__':
    main()
