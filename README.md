# pharos-automation-bot
Pharos Automation Bot — Multi-module DeFi automation suite for Pharos Testnet ecosystem with 14 integrated bots, single-wallet configuration, token swapping, staking, liquidity provision, faucet claiming, multi-account proxy support, and Rich CLI for comprehensive testnet farming
<div align="center">

```
 _____  _                                         _                        _   _               ____   ____ _______ 
|  __ \| |                             /\        | |                      | | (_)             |  _ \ / __ \__   __|
| |__) | |__   __ _ _ __ ___  ___     /  \  _   _| |_ ___  _ __ ___   __ _| |_ _  ___  _ __  | |_) | |  | | | |   
|  ___/| '_ \ / _` | '__/ _ \/ __|   / /\ \| | | | __/ _ \| '_ ` _ \ / _` | __| |/ _ \| '_ \ |  _ <| |  | | | |   
| |    | | | | (_| | | | (_) \__ \  / ____ \ |_| | || (_) | | | | | | (_| | |_| | (_) | | | || |_) | |__| | | |   
|_|    |_| |_|\__,_|_|  \___/|___/ /_/    \_\__,_|\__\___/|_| |_| |_|\__,_|\__|_|\___/|_| |_||____/ \____/  |_|   
```

[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Web3](https://img.shields.io/badge/Web3.py-6.15.0-F16822?style=for-the-badge&logo=web3.js&logoColor=white)](https://web3py.readthedocs.io)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)
[![Pharos](https://img.shields.io/badge/Pharos-Testnet-blueviolet?style=for-the-badge)](https://testnet.pharosnetwork.xyz/)

**Multi-module automation suite for the entire Pharos Testnet DeFi ecosystem — 14 bots, one wallet, one config.**

[Features](#-features) · [Getting Started](#-getting-started) · [Configuration](#-configuration) · [Usage](#-usage) · [FAQ](#-faq)

</div>

---

## Registration & Official Links

| # | Resource | URL |
|:-:|----------|-----|
| 1 | Pharos Testnet Portal | https://testnet.pharosnetwork.xyz/ |
| 2 | Pharos Block Explorer | https://testnet.pharosscan.xyz/ |
| 3 | Pharos Documentation | https://docs.pharosnetwork.xyz/ |
| 4 | Pharos Faucet | https://testnet.pharosnetwork.xyz/ |
| 5 | FaroSwap DEX | https://faroswap.com/ |
| 6 | Gotchipus NFT | https://gotchipus.com/ |
| 7 | Pharos Name Service | https://pns.pharosnetwork.xyz/ |

> Pharos Network is an EVM-compatible Layer 1 blockchain targeting real-world asset (RWA) finance. The testnet processes transactions at ~0.5s block times with 77+ TPS. Mainnet launch is planned for Q1 2026.

---

## Features

<table>
<tr><td>

### DeFi & Swaps
| Status | Feature |
|:------:|---------|
| ✅ | Pharos BOT — core DeFi automation |
| ✅ | FaroSwap BOT — swap & liquidity pools |
| ✅ | Zenith Swap BOT — swap & liquidity |
| ✅ | R2 Pharos BOT — swap & liquidity |
| ✅ | Brokex BOT — faucet claims & trading |
| ✅ | OpenFi BOT — lending, borrowing, DeFi |
| ✅ | Bitverse BOT — trade, deposit, withdraw |

</td><td>

### NFT, Staking & Social
| Status | Feature |
|:------:|---------|
| ✅ | Gotchipus BOT — NFT minting & wearables |
| ✅ | AquaFlux BOT — standard & premium NFT mint |
| ✅ | Pharos Name Service BOT — .phrs domains |
| ✅ | Grandline BOT — claim all badges |
| ✅ | AutoStaking BOT — staking & faucet claims |
| ✅ | Spout Finance BOT — KYC, trades, accounts |
| ✅ | Primuslabs Send BOT — social tips via X |

</td></tr>
<tr><td>

### Infrastructure
| Status | Feature |
|:------:|---------|
| ✅ | Unified wallet across all 14 bots |
| ✅ | Three proxy modes (Free / Private / None) |
| ✅ | Auto-rotation for invalid proxies |
| ✅ | Multi-account testnet farming |

</td><td>

### Interface
| Status | Feature |
|:------:|---------|
| ✅ | Rich TUI launcher (cli.py) |
| ✅ | Run bots individually or in sequence |
| ✅ | Built-in settings editor |
| ✅ | One-click dependency installer |

</td></tr>
</table>

---

## Getting Started

### Prerequisites

| Requirement | Version | Notes |
|-------------|---------|-------|
| Python | 3.9+ | On Windows with Python 3.13+, install [Microsoft C++ Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/) |
| pip | latest | Ships with Python |
| Git | any | For cloning the repository |

### Installation — Windows (One-Click)

```bash
git clone https://github.com/shellgainer/pharos_automation_bot.git
cd pharos_automation_bot
py cli.py
# Select "1 - Install dependencies" from the menu
```

### Installation — Manual

```bash
git clone https://github.com/shellgainer/pharos_automation_bot.git
cd pharos_automation_bot
pip install -r requirements.txt
python cli.py
```

### Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| web3 | 6.15.0 | Blockchain RPC interaction |
| eth-account | 0.11.0 | Wallet & transaction signing |
| requests | latest | HTTP requests to APIs |
| colorama | latest | Cross-platform terminal colors |
| rich | latest | TUI panels, tables, menus |

> **Pinning note:** It is recommended to use exactly `web3==6.15.0` and `eth-account==0.11.0` to avoid ABI compatibility issues.

---

## Configuration

### `accounts.txt` — Private Keys

```
# One private key per line (without 0x prefix)
a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2
f6e5d4c3b2a1f6e5d4c3b2a1f6e5d4c3b2a1f6e5d4c3b2a1f6e5d4c3b2a1f6e5
```

### `proxy.txt` — Proxy List

```
# Supported formats:
127.0.0.1:8080
http://user:pass@192.168.1.100:3128
socks5://user:pass@10.0.0.1:1080
```

### `pools.json` — FaroSwap Liquidity Pools

```json
{
  "pools": [
    {
      "name": "PHRS-USDT Pool",
      "address": "0x1a2B3c4D5e6F7a8B9c0D1e2F3a4B5c6D7e8F9a0B",
      "token0": "PHRS",
      "token1": "USDT"
    },
    {
      "name": "PHRS-WETH Pool",
      "address": "0x9F8e7D6c5B4a3F2e1D0c9B8a7F6e5D4c3B2a1F0e",
      "token0": "PHRS",
      "token1": "WETH"
    }
  ]
}
```

---

## Usage

Launch the Rich TUI menu:

```bash
python cli.py
```

```
┌─────────────────────────────────────────────────────────┐
│                     Main Menu                           │
├─────┬──────────────────────┬────────────────────────────┤
│ Key │ Action               │ Description                │
├─────┼──────────────────────┼────────────────────────────┤
│  1  │ Install dependencies │ pip install requirements   │
│  2  │ Run bots             │ Launch bots menu           │
│  3  │ Settings             │ accounts / proxy / pools   │
│  4  │ About                │ Project information        │
│  Q  │ Quit                 │ Exit launcher              │
└─────┴──────────────────────┴────────────────────────────┘
```

### Direct Bot Execution

| Command | Bot |
|---------|-----|
| `python bot1.py` | Pharos BOT |
| `python bot2.py` | Gotchipus BOT |
| `python bot3.py` | OpenFi BOT |
| `python bot4.py` | Brokex BOT |
| `python bot5.py` | FaroSwap BOT |
| `python bot6.py` | AquaFlux BOT |
| `python bot7.py` | Zenith Swap BOT |
| `python bot8.py` | Pharos Name Service BOT |
| `python bot9.py` | Grandline BOT |
| `python bot10.py` | R2 Pharos BOT |
| `python bot11.py` | Bitverse BOT |
| `python bot12.py` | AutoStaking BOT |
| `python bot13.py` | Spout Finance BOT |
| `python bot14.py` | Primuslabs Send BOT |

---

## Project Structure

```
pharos_automation_bot/
├── cli.py              # Rich TUI launcher — main entry point
├── bots_common.py      # Shared bot scaffold (Rich panels)
├── bot1.py             # Pharos BOT — core DeFi automation
├── bot2.py             # Gotchipus BOT — NFT minting
├── bot3.py             # OpenFi BOT — lending/borrowing
├── bot4.py             # Brokex BOT — faucet & trades
├── bot5.py             # FaroSwap BOT — swap & LP
├── bot6.py             # AquaFlux BOT — NFT mint
├── bot7.py             # Zenith Swap BOT — swap & LP
├── bot8.py             # PNS BOT — .phrs domain mint
├── bot9.py             # Grandline BOT — badge claims
├── bot10.py            # R2 Pharos BOT — swap & LP
├── bot11.py            # Bitverse BOT — trade/deposit
├── bot12.py            # AutoStaking BOT — staking
├── bot13.py            # Spout Finance BOT — KYC/trades
├── bot14.py            # Primuslabs Send BOT — X tips
├── accounts.txt        # Private keys (one per line)
├── proxy.txt           # Proxy list
├── pools.json          # FaroSwap pool addresses
└── requirements.txt    # Python dependencies
```

---

## FAQ

<details>
<summary><b>Which Python version should I use?</b></summary>

Python 3.9 or higher. If you are on Windows with Python 3.13+, you must also install [Microsoft C++ Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/) before installing dependencies (required by native extensions in `web3`).
</details>

<details>
<summary><b>Can I run just one bot instead of all 14?</b></summary>

Yes. Use the "Run bots" menu option in `cli.py` and pick a specific bot by number, or launch any bot directly: `python bot5.py`. The "Run All (sequence)" option launches all bots one after another.
</details>

<details>
<summary><b>How do I configure proxies?</b></summary>

Add proxies to `proxy.txt`, one per line. Supported formats: `ip:port`, `http://user:pass@ip:port`, `socks5://ip:port`. You can also select "Free public" mode in settings for auto-rotated free proxies, or "No Proxy" to connect directly.
</details>

<details>
<summary><b>Do I need to add the 0x prefix to private keys?</b></summary>

No. Add raw hex keys to `accounts.txt` without the `0x` prefix, one key per line. The bot handles prefix normalization internally.
</details>

<details>
<summary><b>Is this safe for mainnet?</b></summary>

**No.** This suite is designed exclusively for the Pharos Testnet. Never use mainnet wallets or real funds. Always use burner wallets with no real assets.
</details>

<details>
<summary><b>Why do I get build errors installing web3?</b></summary>

On Windows with Python 3.13+, some C extensions require the MSVC compiler. Install Microsoft C++ Build Tools, restart your terminal, and try again. Alternatively, pin to the tested versions:

```bash
pip uninstall web3 eth-account
pip install web3==6.15.0 eth-account==0.11.0
```
</details>

---

## Disclaimer

> This software is provided for **educational and testnet purposes only**. It is designed to interact with the Pharos Testnet and should never be used with mainnet wallets containing real assets. Use burner wallets exclusively. Never share your private keys. The developers assume no liability for any loss or damage resulting from the use of this tool. Always review the source code before running. By using this software you accept full responsibility for your actions.

---

<div align="center">

**Support the Developers**

EVM: `0x3b94Ff1611773171E06047C0041099CccCFC609F`

If this project helped you, consider giving it a star!

[![Star](https://img.shields.io/github/stars/shellgainer/pharos_automation_bot?style=for-the-badge&color=yellow)](https://github.com/shellgainer/pharos_automation_bot)

Crafted by **CryptoDai3 x YetiDAO** · MIT License

</div>
