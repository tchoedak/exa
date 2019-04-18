<p align="center"><img height="300" width="300" src="logo.png" /></p>

# Installation

Clone the repo and use pip to install the package
```bash
git clone https://github.com/tchoedak/exa.git
pip install exa/
```

# Usage

Find the exchange rate from 1 USD to EUR

```bash
exa --from USD --to EUR
```

Find the exchange rate from 1 USD to EUR and
report if EUR is below 1.3 EUR

```bash
exa --from USD --to EUR --threshold 1.3
```

Send an SMS alert if the exchange rate from
1 USD to EUR is below 1.3 EUR

```bash
exa --from USD --to EUR --threshold 1.3 --send-alerts
```

# Configuration

To configure your default `FROM` currency and `TO` currency,
edit the [config](exa/config.py') file and adjust `from_` and `to` variables
respectively.
