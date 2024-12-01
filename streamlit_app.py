from enum import Enum
from datetime import datetime, timedelta

# Third party imports
import streamlit as st

# Local package imports
from option_pricing import BlackScholesModel, MonteCarloPricing, BinomialTreeModel, Ticker

# Enum for different pricing models
class OPTION_PRICING_MODEL(Enum):
    BLACK_SCHOLES = 'Black Scholes Model'
    MONTE_CARLO = 'Monte Carlo Simulation'
    MARKOV_CHAIN = 'Markov Chain'

# Comment out caching for debugging
# @st.cache_data
def get_historical_data(ticker):
    """Fetches and caches historical stock data for the given ticker."""
    print(f"Fetching historical data for ticker: {ticker}")
    return Ticker.get_historical_data(ticker)

# Setting options to suppress warnings
# Note: This is now deprecated, so remove this line
# st.set_option('deprecation.showPyplotGlobalUse', False)
st.set_page_config(page_title="OptiWise", page_icon="📈")
# App Title
st.title('OptiWise - Option Pricing Models')
st.markdown(
    """
    <style>
    .top-bar {
        position: relative;
        display: flex;
        justify-content: flex-end;
        align-items: center;
        padding: 10px;
        background-color: transparent;
        height: 30px;
    }
    .portfolio-link {
        font-size: 16px;
        font-weight: bold;
        color: #007bff;
        text-decoration: none;
    }
    .portfolio-link:hover {
        text-decoration: underline;
    }
    </style>
    <div class="top-bar">
        <a class="portfolio-link" href="https://your-portfolio-link.com" target="_blank">Portfolio</a>
    </div>
    """,
    unsafe_allow_html=True
)

# Sidebar for model selection
pricing_method = st.sidebar.radio('Select Option Pricing Method:', options=[model.value for model in OPTION_PRICING_MODEL])

st.subheader(f'Pricing Method: {pricing_method}')
def display_common_inputs():
    ticker = st.text_input('Ticker Symbol', 'AAPL')
    strike_price = st.number_input('Strike Price', min_value=1.0, value=300.0)
    risk_free_rate = st.slider('Risk-Free Rate (%)', 0.0, 10.0, 1.0)
    sigma = st.slider('Volatility (Sigma, %)', 0.0, 100.0, 20.0)
    exercise_date = st.date_input('Exercise Date', min_value=datetime.today() + timedelta(days=1), value=datetime.today() + timedelta(days=365))
    return ticker, strike_price, risk_free_rate / 100, sigma / 100, (exercise_date - datetime.now().date()).days

if pricing_method == OPTION_PRICING_MODEL.BLACK_SCHOLES.value:
    ticker, strike_price, risk_free_rate, sigma, days_to_maturity = display_common_inputs()
    
    if st.button(f'Calculate Option Price for {ticker}'):
        # Debugging: Print input values
        print(f"Inputs - Ticker: {ticker}, Strike Price: {strike_price}, Risk-Free Rate: {risk_free_rate}, Sigma: {sigma}, Days to Maturity: {days_to_maturity}")

        data = get_historical_data(ticker)
        
        if data is not None and not data.empty:
            st.write(data.tail())
            Ticker.plot_data(data, ticker, 'Adj Close')

            # Updated Plotting to Pass Figure Directly
            spot_price = Ticker.get_last_price(data, 'Adj Close')
            # spot_price = 231.12
            bsm = BlackScholesModel(spot_price, strike_price, days_to_maturity, risk_free_rate, sigma)
            
            call_price = bsm.calculate_option_price('Call Option')
            put_price = bsm.calculate_option_price('Put Option')

            st.subheader(f'Call Option Price: {call_price:.2f}')
            st.subheader(f'Put Option Price: {put_price:.2f}')
        else:
            print(f"Failed to retrieve data for ticker: {ticker}. Check if the ticker is valid or if there are network issues.")
            st.error("Failed to retrieve historical data. Please check the ticker symbol.")
elif pricing_method == OPTION_PRICING_MODEL.MONTE_CARLO.value:
    # Parameters for Monte Carlo simulation
    ticker = st.text_input('Ticker symbol', 'AAPL')
    strike_price = st.number_input('Strike price', 300)
    risk_free_rate = st.slider('Risk-free rate (%)', 0, 100, 10)
    sigma = st.slider('Sigma (%)', 0, 100, 20)
    exercise_date = st.date_input('Exercise date', min_value=datetime.today() + timedelta(days=1), value=datetime.today() + timedelta(days=365))
    number_of_simulations = st.slider('Number of simulations', 100, 100000, 10000)
    num_of_movements = st.slider('Number of price movement simulations to be visualized ', 0, int(number_of_simulations/10), 100)

    if st.button(f'Calculate option price for {ticker}'):
        data = get_historical_data(ticker)
        if data is None or data.empty:
            st.error("Failed to retrieve historical data. Please check the ticker symbol.")

        spot_price = Ticker.get_last_price(data, 'Adj Close')

        if spot_price is None:
            st.warning("Spot price could not be determined. Please input manually.")
            spot_price = st.number_input("Enter Spot Price Manually", min_value=1.0, value=100.0)
        st.write(data.tail())
        fig = Ticker.plot_data(data, ticker, 'Adj Close')
        if fig:
            st.pyplot(fig)

        # Format simulation parameters
        spot_price = Ticker.get_last_price(data, 'Adj Close') 
        risk_free_rate = risk_free_rate / 100
        sigma = sigma / 100
        days_to_maturity = (exercise_date - datetime.now().date()).days

        # Simulating stock movements
        MC = MonteCarloPricing(spot_price, strike_price, days_to_maturity, risk_free_rate, sigma, number_of_simulations)
        MC.simulate_prices()

        # Get the figure and pass it to st.pyplot
        fig = MC.plot_simulation_results(num_of_movements)
        st.pyplot(fig)

        # Calculating call/put option price
        call_option_price = MC.calculate_option_price('Call Option')
        put_option_price = MC.calculate_option_price('Put Option')

        # Displaying call/put option price
        st.subheader(f'Call option price: {call_option_price}')
        st.subheader(f'Put option price: {put_option_price}')

elif pricing_method == OPTION_PRICING_MODEL.MARKOV_CHAIN.value:
    # Parameters for Binomial-Tree model
    ticker = st.text_input('Ticker symbol', 'AAPL')
    strike_price = st.number_input('Strike price', 300)
    risk_free_rate = st.slider('Risk-free rate (%)', 0, 100, 10)
    sigma = st.slider('Sigma (%)', 0, 100, 20)
    exercise_date = st.date_input('Exercise date', min_value=datetime.today() + timedelta(days=1), value=datetime.today() + timedelta(days=365))
    number_of_time_steps = st.slider('Number of time steps', 5000, 100000, 15000)

    if st.button(f'Calculate option price for {ticker}'):
         # Getting data for selected ticker
        data = get_historical_data(ticker)
        st.write(data.tail())
        fig = Ticker.plot_data(data, ticker, 'Adj Close')
        if fig:
            st.pyplot(fig)

        # Formating simulation parameters
        spot_price = Ticker.get_last_price(data, 'Adj Close') 
        risk_free_rate = risk_free_rate / 100
        sigma = sigma / 100
        days_to_maturity = (exercise_date - datetime.now().date()).days

        # Calculating option price
        BOPM = BinomialTreeModel(spot_price, strike_price, days_to_maturity, risk_free_rate, sigma, number_of_time_steps)
        call_option_price = BOPM.calculate_option_price('Call Option')
        put_option_price = BOPM.calculate_option_price('Put Option')

        # Displaying call/put option price
        st.subheader(f'Call option price: {call_option_price}')
        st.subheader(f'Put option price: {put_option_price}')
