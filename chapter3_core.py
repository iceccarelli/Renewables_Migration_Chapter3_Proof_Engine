
import numpy as np
import pandas as pd

def calculate_arbitrage_potential(prices, delta_load_agent, storage_efficiency):
    """
    Calculates the Protocol-Enabled Arbitrage Potential (AMCP).

    AMCP = sum(|P(t)| * Delta_L_agent(t) * eta_storage) for P(t) < 0

    Args:
        prices (np.array or list): Array of day-ahead prices at time t.
        delta_load_agent (np.array or list): Additional load triggered by MCP agents at time t.
        storage_efficiency (float): Round-trip efficiency of storage.

    Returns:
        float: The Protocol-Enabled Arbitrage Potential (AMCP).
    """
    prices = np.array(prices)
    delta_load_agent = np.array(delta_load_agent)

    negative_price_indices = np.where(prices < 0)

    amcp = np.sum(np.abs(prices[negative_price_indices]) *
                  delta_load_agent[negative_price_indices] *
                  storage_efficiency)
    return amcp

def calculate_cannibalization_metrics(renewables_capacity, flexible_demand_capacity, price_threshold=0):
    """
    Calculates metrics related to price cannibalization and MCP-enabled recovery.

    Args:
        renewables_capacity (float): Total renewables capacity (GW).
        flexible_demand_capacity (float): Total flexible demand capacity (GW).
        price_threshold (float): Price threshold for negative prices (e.g., 0 €/MWh).

    Returns:
        dict: A dictionary containing cannibalization metrics.
    """
    # Placeholder for more complex cannibalization logic
    cannibalized_capacity = renewables_capacity * 0.2 # Example
    recovered_capacity = flexible_demand_capacity * 0.8 # Example

    return {
        "cannibalized_capacity": cannibalized_capacity,
        "recovered_capacity": recovered_capacity,
        "net_impact": recovered_capacity - cannibalized_capacity
    }

def calculate_crowdfunding_efficiency(total_eeg_transfer_gb, total_gw_installed):
    """
    Calculates the Crowdfunding Efficiency (eta_cf).

    eta_cf = Total GW Installed / Total EEG Transfer (€B)

    Args:
        total_eeg_transfer_gb (float): Total EEG transfer in €B.
        total_gw_installed (float): Total GW installed due to EEG.

    Returns:
        float: Crowdfunding Efficiency (eta_cf).
    """
    if total_eeg_transfer_gb == 0:
        return 0
    return total_gw_installed / total_eeg_transfer_gb

def calculate_stability_margin(physical_inertia, mcp_latency, agent_flexibility):
    """
    Calculates the Stability Margin based on physical inertia, MCP latency, and agent flexibility.

    Stability Margin = f(Hsys, LatencyMCP, FlexibilityAgent)

    Args:
        physical_inertia (float): System physical inertia (Hsys).
        mcp_latency (float): MCP latency (ms).
        agent_flexibility (float): Agent flexibility.

    Returns:
        float: The calculated stability margin.
    """
    # Placeholder for a more complex function based on the book's implied relationship
    # This is a simplified representation.
    stability = physical_inertia / (mcp_latency * agent_flexibility)
    return stability


if __name__ == '__main__':
    # Example Usage and Verification
    print("--- Chapter 3 Core Logic Verification ---")

    # Arbitrage Equation
    sample_prices = np.array([10, 5, -10, -20, 0, -5, 15])
    sample_delta_load = np.array([0, 0, 100, 200, 0, 50, 0])
    sample_efficiency = 0.9
    amcp_result = calculate_arbitrage_potential(sample_prices, sample_delta_load, sample_efficiency)
    print(f"Arbitrage Potential (AMCP): {amcp_result:.2f} €")

    # Cannibalization Metrics
    renewables_cap = 100 # GW
    flexible_demand_cap = 30 # GW
    cannibalization_data = calculate_cannibalization_metrics(renewables_cap, flexible_demand_cap)
    print(f"Cannibalized Capacity: {cannibalization_data['cannibalized_capacity']:.2f} GW")
    print(f"Recovered Capacity: {cannibalization_data['recovered_capacity']:.2f} GW")
    print(f"Net Impact: {cannibalization_data['net_impact']:.2f} GW")

    # Crowdfunding Efficiency
    eeg_transfer = 580 # €B
    gw_installed = 117 + 78 # GW (Solar + Wind from book)
    eta_cf_result = calculate_crowdfunding_efficiency(eeg_transfer, gw_installed)
    print(f"Crowdfunding Efficiency (eta_cf): {eta_cf_result:.4f} GW/€B")

    # Stability Margin (from Chapter 1, but relevant for context)
    h_sys = 130 # GVA.s
    mcp_lat = 50 # ms
    agent_flex = 0.5 # dimensionless
    stability_margin_result = calculate_stability_margin(h_sys, mcp_lat, agent_flex)
    print(f"Stability Margin: {stability_margin_result:.2f}")
