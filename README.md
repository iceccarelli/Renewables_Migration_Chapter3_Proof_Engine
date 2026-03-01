# Renewables_Migration_Chapter3_Proof_Engine

## Chapter 3: The EEG "Tax": A Masterclass in Crowdfunding

This repository contains the **Renewables Migration Chapter 3 Proof Engine**, a production-ready Python package designed to brutally verify every claim, equation, number, graph, and curve presented in Chapter 3 of "The Renewables Migration" by Vincenzo Grimaldi.

### Mission Statement
Our mission is to provide a transparent, reproducible, and verifiable framework for the technical and economic assertions made in Chapter 3. Any engineer, student, or policymaker can clone, run, and verify the entire chapter's findings in under 60 seconds.

### Key Features
- **`chapter3_core.py`**: Contains the core mathematical models and functions, including:
    - The Arbitrage Equation ($A_{MCP}$)
    - Crowdfunding Efficiency ($\eta_{cf}$)
    - Cannibalization Curve logic
    - Stability Margin calculation (contextual from Chapter 1)
- **`main_interactive.py`**: A Streamlit dashboard for interactive exploration of Chapter 3's concepts, featuring:
    - "Live Arbitrage Simulator"
    - "Cannibalization Curve Explorer"
    - "Protocol Dividend Projection"
    - "Spy Mode" to highlight exact book claims like "The Spy on the €580B EEG" and "The Spy on Negative Prices."
- **`data/book_numbers.csv`**: Hardcoded exact book values such as:
    - €580B cumulative EEG transfer
    - $\eta_{cf} \approx 0.32$ GW/€B
    - 573 negative price hours in 2025
    - Cannibalization metrics
- **`data/appendix_a_extract.csv`**: Technical constants triangulated from Appendix A.3 of the book.
- **`notebooks/01_Prove_Chapter3.ipynb`**: A Jupyter notebook providing a step-by-step, line-by-line proof of every equation and claim, complete with interactive sliders for key variables.
- **`plots/`**: Directory for generated static plots, including:
    - `cannibalization_curve.png` (matching Figure 3.1)
    - `negative_price_arbitrage.png`
    - `protocol_dividend_projection.png`
- **`tests/test_book_numbers.py`**: A `pytest` suite that *fails* if any hardcoded book number or derived calculation does not precisely match the book's claims. Achieving 100% pass rate confirms "Chapter 3 100% proven against book."
- **`utils/generate_book_figures.py`**: Script to reproduce Figure 3.1 and other introductory manifolds exactly as presented in the book.
- **`LICENSE`**: MIT License for open-source use.

### Installation and Verification (in under 60 seconds)

1.  **Clone the repository:**
    ```bash
    git clone git@github.com:iceccarelli/Renewables_Migration_Chapter3_Proof_Engine.git
    cd Renewables_Migration_Chapter3_Proof_Engine
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the automated proof suite:**
    ```bash
    pytest
    ```
    *Expected output: "Chapter 3 100% proven against book" with all tests passing.*

4.  **Launch the interactive Streamlit dashboard:**
    ```bash
    streamlit run main_interactive.py
    ```
    Explore the tabs to interact with the models and visualize the book's claims live.

5.  **Explore the Jupyter Notebook:**
    ```bash
    jupyter notebook notebooks/01_Prove_Chapter3.ipynb
    ```
    Delve into the step-by-step mathematical derivations and proofs.

### Brutal Honesty and Reproducibility
This engine is built with zero-tolerance for half-measures. Every line of code is commented to explain its direct correlation to the book's content. If a claim is made, it is mathematically and programmatically verified here. If a number is stated, it is hardcoded and tested.

--- 
**Book**: The Renewables Migration, Chapter 3 by Vincenzo Grimaldi
**Date**: March 1, 2026
