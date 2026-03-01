
import sys
sys.path.append('.')
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.graph_objects as go
from chapter3_core import calculate_cannibalization_metrics, calculate_arbitrage_potential

def generate_cannibalization_curve(renewables_capacity_max=300, flexible_demand_capacity_max=100, output_path="plots/cannibalization_curve.png"):
    """
    Reproduces Figure 3.1: The Cannibalization Curve.
    """
    capacities = np.linspace(0, renewables_capacity_max + 50, 100)
    cannibalized_curve = [calculate_cannibalization_metrics(c, 0)["cannibalized_capacity"] for c in capacities]
    # For the recovered curve, we'll assume a fixed renewables capacity and vary flexible demand
    fixed_renewables = renewables_capacity_max * 0.7 # Example fixed point
    recovered_curve = [calculate_cannibalization_metrics(fixed_renewables, c)["recovered_capacity"] for c in capacities]

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=capacities, y=cannibalized_curve, mode='lines', name='Cannibalized Supply (Conceptual)', line=dict(color='blue')))
    fig.add_trace(go.Scatter(x=capacities, y=recovered_curve, mode='lines', name='MCP-Enabled Demand (Conceptual)', line=dict(color='green')))
    fig.update_layout(
        title='Figure 3.1. The Cannibalization Curve',
        xaxis_title='Capacity Dispatched (GW)',
        yaxis_title='Impact (GW)'
    )
    fig.write_image(output_path)
    print(f"Generated {output_path}")

def generate_negative_price_arbitrage_plot(output_path="plots/negative_price_arbitrage.png"):
    """
    Reproduces a conceptual plot for negative price arbitrage (similar to Figure 3.2).
    """
    hours = np.arange(0, 24)
    # Simulate market prices (2025 - taxpayer disaster)
    prices_2025 = -20 * np.sin(hours / 24 * 2 * np.pi) - 10 # Example negative prices
    prices_2025[prices_2025 > 0] = 0 # Only show negative part

    # Simulate MCP agent load (2030 - free fuel)
    mcp_agent_load_2030 = np.zeros_like(hours, dtype=float)
    mcp_agent_load_2030[prices_2025 < 0] = np.abs(prices_2025[prices_2025 < 0]) * 5 # Scale load with price magnitude

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=hours, y=prices_2025, mode='lines', name='Market Price (2025) - Taxpayer Disaster', line=dict(color='blue')))
    fig.add_trace(go.Scatter(x=hours, y=mcp_agent_load_2030, mode='lines', name='MCP Agent Load (2030) - Free Fuel', line=dict(color='green')))
    fig.update_layout(
        title='Figure 3.2. The Negative Price Abyss: From Taxpayer Loss to Agentic Gain',
        xaxis_title='Hour of Day',
        yaxis_title='Value / Load (Conceptual)'
    )
    fig.write_image(output_path)
    print(f"Generated {output_path}")

def generate_protocol_dividend_projection(output_path="plots/protocol_dividend_projection.png"):
    """
    Generates a conceptual plot for Protocol Dividend Projection.
    """
    years = np.arange(2025, 2031)
    eeg_burden = np.array([2.9, 2.8, 2.5, 2.0, 1.5, 1.0]) # Conceptual decreasing EEG burden
    protocol_dividend = np.array([0.1, 0.5, 1.2, 2.0, 2.5, 3.0]) # Conceptual increasing dividend

    fig = go.Figure()
    fig.add_trace(go.Bar(x=years, y=eeg_burden, name='Legacy EEG Burden (€B)' , marker_color='red'))
    fig.add_trace(go.Bar(x=years, y=protocol_dividend, name='Protocol Dividend (€B)' , marker_color='green'))
    fig.update_layout(
        barmode='group',
        title='Conceptual Protocol Dividend Projection',
        xaxis_title='Year',
        yaxis_title='Value (€B)'
    )
    fig.write_image(output_path)
    print(f"Generated {output_path}")


if __name__ == '__main__':
    import os
    os.makedirs("plots", exist_ok=True)
    generate_cannibalization_curve()
    generate_negative_price_arbitrage_plot()
    generate_protocol_dividend_projection()
