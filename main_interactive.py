
import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go
from chapter3_core import (
    calculate_arbitrage_potential,
    calculate_cannibalization_metrics,
    calculate_crowdfunding_efficiency,
    calculate_stability_margin
)

st.set_page_config(layout="wide", page_title="Renewables Migration Chapter 3 Proof Engine")

# Load book numbers (assuming book_numbers.csv is in the data folder)
try:
    book_numbers_df = pd.read_csv("data/book_numbers.csv")
    def get_book_number(metric_name):
        return book_numbers_df[book_numbers_df["metric"] == metric_name]["value"].iloc[0]
except FileNotFoundError:
    st.error("book_numbers.csv not found. Please ensure it's in the 'data' folder.")
    st.stop()

# --- Spy Mode Toggle ---
if 'spy_mode' not in st.session_state:
    st.session_state.spy_mode = False

if st.sidebar.button("Toggle Spy Mode"):
    st.session_state.spy_mode = not st.session_state.spy_mode

# --- Streamlit App Layout ---
st.title("Renewables Migration Chapter 3 Proof Engine")
st.subheader("The EEG \"Tax\": A Masterclass in Crowdfunding")

tabs = st.tabs([
    "Live Arbitrage Simulator",
    "Cannibalization Curve Explorer",
    "Protocol Dividend Projection",
    "Prove Every Equation",
    "Download Book Data"
])

with tabs[0]:
    st.header("Live Arbitrage Simulator")
    st.markdown("### The Spy on Negative Prices: The Fuel for Autonomous Markets")

    st.write("Adjust the parameters below to simulate the Protocol-Enabled Arbitrage Potential ($A_{MCP}$) during negative price events.")

    col1, col2 = st.columns(2)
    with col1:
        num_hours = st.slider("Number of hours with negative prices", 1, 1000, int(get_book_number("negative_price_hours_2025")))
        avg_negative_price = st.slider("Average negative price (€/MWh)", -200.0, -1.0, -20.0)
        avg_delta_load_agent = st.slider("Average additional load by MCP agents (GW)", 0.1, 10.0, 1.0)
        storage_efficiency = st.slider("Storage round-trip efficiency (eta_storage)", 0.5, 1.0, 0.9)

    # Simulate prices and delta_load_agent for calculation
    simulated_prices = np.full(num_hours, avg_negative_price)
    simulated_delta_load = np.full(num_hours, avg_delta_load_agent)

    amcp_simulated = calculate_arbitrage_potential(simulated_prices, simulated_delta_load, storage_efficiency)

    st.markdown(f"#### Simulated Arbitrage Potential ($A_{{MCP}}$): **{amcp_simulated:,.2f} €**")

    if st.session_state.spy_mode:
        st.info(f"**Book Claim:** Chapter 3 states that in 2025, negative price hours reached **{int(get_book_number('negative_price_hours_2025'))} hours**, costing taxpayers an estimated **€{get_book_number('redispatch_costs_2025'):,.1f} billion** in legacy subsidies. The Arbitrage Equation ($A_{{MCP}}$) turns this liability into an asset.")

with tabs[1]:
    st.header("Cannibalization Curve Explorer")
    st.markdown("### Visualizing the Price Cannibalization: The \"Protocol Pivot\"")

    st.write("Explore how increasing renewables capacity leads to cannibalization and how flexible demand can mitigate it.")

    col1, col2 = st.columns(2)
    with col1:
        renewables_capacity_slider = st.slider("Total Renewables Capacity (GW)", 50.0, 300.0, float(get_book_number("solar_capacity_gw")) + float(get_book_number("wind_capacity_gw")))
        flexible_demand_capacity_slider = st.slider("Flexible Demand Capacity (GW)", 0.0, 100.0, 30.0)

    cannibalization_metrics = calculate_cannibalization_metrics(renewables_capacity_slider, flexible_demand_capacity_slider)

    st.markdown(f"#### Cannibalized Capacity: **{cannibalization_metrics['cannibalized_capacity']:.2f} GW**")
    st.markdown(f"#### Recovered Capacity by Flexible Demand: **{cannibalization_metrics['recovered_capacity']:.2f} GW**")
    st.markdown(f"#### Net Impact: **{cannibalization_metrics['net_impact']:.2f} GW**")

    # Plotting a simplified cannibalization curve (conceptual)
    capacities = np.linspace(0, renewables_capacity_slider + 50, 100)
    cannibalized_curve = [calculate_cannibalization_metrics(c, 0)['cannibalized_capacity'] for c in capacities]
    recovered_curve = [calculate_cannibalization_metrics(renewables_capacity_slider, c)['recovered_capacity'] for c in capacities]

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=capacities, y=cannibalized_curve, mode='lines', name='Cannibalized Supply (Conceptual)', line=dict(color='blue')))
    fig.add_trace(go.Scatter(x=capacities, y=recovered_curve, mode='lines', name='MCP-Enabled Demand (Conceptual)', line=dict(color='green')))
    fig.update_layout(title='Conceptual Cannibalization Curve', xaxis_title='Capacity (GW)', yaxis_title='Impact (GW)')
    st.plotly_chart(fig, use_container_width=True)

    if st.session_state.spy_mode:
        st.info("**Book Claim:** Figure 3.1 illustrates the 'Cannibalization Curve', showing how renewables' zero-marginal block craters prices (blue) and how MCP-enabled flexible demand (green) 'claws back' value by shifting load into negative price zones.")

with tabs[2]:
    st.header("Protocol Dividend Projection")
    st.markdown("### The Crowdfunded Empire’s Final Tally")

    st.write("Project the impact of Crowdfunding Efficiency ($\eta_{cf}$) and the Protocol Dividend.")

    col1, col2 = st.columns(2)
    with col1:
        eeg_transfer_slider = st.slider("Cumulative EEG Transfer (€B)", 100.0, 1000.0, get_book_number("cumulative_eeg_transfer"))
        gw_installed_slider = st.slider("Total GW Installed (Solar + Wind)", 50.0, 500.0, float(get_book_number("solar_capacity_gw")) + float(get_book_number("wind_capacity_gw")))
        projected_amcp = st.slider("Projected Annual AMCP (€B)", 0.0, 10.0, 2.0)

    eta_cf_simulated = calculate_crowdfunding_efficiency(eeg_transfer_slider, gw_installed_slider)

    st.markdown(f"#### Crowdfunding Efficiency ($\eta_{{cf}}$): **{eta_cf_simulated:.4f} GW/€B**")
    st.markdown(f"#### Projected Protocol Dividend (Annual): **€{projected_amcp:,.2f} Billion**")

    if st.session_state.spy_mode:
        st.info(f"**Book Claim:** The book mentions **€{get_book_number('cumulative_eeg_transfer'):,.0f}B cumulative EEG transfer** and a Crowdfunding Efficiency ($\eta_{{cf}}$) of approximately **{get_book_number('crowdfunding_efficiency_eta_cf'):.2f} GW/€B**. The Protocol Dividend represents the value captured by MCP-enabled markets.")

with tabs[3]:
    st.header("Prove Every Equation")
    st.markdown("### Step-by-Step Verification of Chapter 3 Equations")

    st.write("This section provides a direct, verifiable implementation of the key equations from Chapter 3. The Jupyter Notebook (`notebooks/01_Prove_Chapter3.ipynb`) offers a more detailed, interactive proof.")

    st.subheader("1. Arbitrage Equation ($A_{MCP}$)")
    st.latex(r"A_{MCP} = \sum_{t:P(t)<0} |P(t)| \cdot \Delta L_{agent}(t) \cdot \eta_{storage}")
    st.write("\(A_{MCP}\) represents the value captured by autonomous agents during negative price events.")
    st.markdown(f"**Book Value (contextual):** In 2025, negative price hours reached **{int(get_book_number('negative_price_hours_2025'))} hours**.")

    st.subheader("2. Crowdfunding Efficiency ($\eta_{cf}$)")
    st.latex(r"\eta_{cf} = \frac{\text{Total GW Installed}}{\text{Total EEG Transfer (€B)}}")
    st.write("\(\eta_{cf}\) measures the efficiency of the EEG in deploying renewable capacity.")
    st.markdown(f"**Book Value:** Cumulative EEG transfer: **€{get_book_number('cumulative_eeg_transfer'):,.0f}B**. Total GW installed (Solar + Wind): **{get_book_number('solar_capacity_gw') + get_book_number('wind_capacity_gw'):.0f} GW**.")
    st.markdown(f"**Calculated $\eta_{{cf}}$:** {calculate_crowdfunding_efficiency(get_book_number('cumulative_eeg_transfer'), get_book_number('solar_capacity_gw') + get_book_number('wind_capacity_gw')):.4f} GW/€B. **Book Claim:** $\eta_{{cf}} \approx {get_book_number('crowdfunding_efficiency_eta_cf'):.2f} GW/€B.")

    st.subheader("3. Stability Margin (Contextual from Chapter 1)")
    st.latex(r"\text{Stability Margin} = f(H_{sys}, \text{Latency}_{MCP}, \text{Flexibility}_{Agent})")
    st.write("As physical inertia ($H_{sys}$) falls, grid survival depends on minimizing MCP latency and maximizing agent flexibility.")
    st.markdown(f"**Book Claim (Chapter 1 context):** Continental Europe hit a record low of **130 GVA·s** inertia in critical hours.")

with tabs[4]:
    st.header("Download Book Data")
    st.markdown("### Raw Data for Verification")

    st.write("Download the exact numbers hardcoded from the book for independent verification.")

    st.dataframe(book_numbers_df)

    csv_data = book_numbers_df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="Download book_numbers.csv",
        data=csv_data,
        file_name="book_numbers.csv",
        mime="text/csv",
    )

    st.markdown("--- ")
    st.markdown("**Note:** `appendix_a_extract.csv` would contain triangulated technical constants from Appendix A.3 if available and extracted.")

