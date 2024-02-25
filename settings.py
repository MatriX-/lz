from classes.Chains import Networks


# ==========================================================
#                       MAIN SETTINGS
# ==========================================================


class MainSettings:
    # Gwei control
    MAX_GAS = 75
    
    # Take the wallets in random order
    RANDOM_WALLETS = True 

    # Remove wallet from files after work
    REMOVE_WALLET = False

    # Proxy mode
    USE_PROXY = True

    # Period in seconds to run all wallets
    START_PERIOD_FROM = 1
    START_PERIOD_TO = 33

    # Module repetitions for each wallet
    REPEATS_PER_WALLET = 33

    # Sleeps after work
    SLEEP_AFTER_WORK_FROM = 150 # Seconds
    SLEEP_AFTER_WORK_TO = 400 # Seconds

    # Blockchain sender
    SEND_FROM = Networks.Polygon # Networks.(Chain) in Chain insert your chain
    
    # Withdraw from OKX before work or top up to Or top up to a certain value
    # Select withdraw or top up
    OKX_WITHDRAW = False
    OKX_TOP_UP = False


# =================================================================
#                       OKX WITHDRAW SETTINGS
# =================================================================


class OKXSettings:
    # You can find this data when withdrawing funds to OKX
    SYMBOL = 'MATIC'
    CHAIN = 'Polygon'
    FEE = 0.1
    
    # Withdrawal amount (For withdraw module)
    AMOUNT_FROM = 0.2
    AMOUNT_TO = 0.4
    
    # Amount for top up balance (For Top Up Module)
    MIN_AMOUNT = 0.1
    MAX_AMOUNT = 0.2
    DECIMALS = 2

    # Here you can get your api-key: https://www.okx.cab/ru/account/my-api
    SECRET_KEY = 'YOUR_DATA'
    API_KEY = 'YOUR_DATA'
    PASSPHRASE = 'YOUR_DATA'
    

# ===========================================================
#                       ROUTES SETTINGS
# ===========================================================


class RoutesSettings:

    class General:
        MIN_AMOUNT = 0.02
        MAX_AMOUNT = 0.05
        DECIMAL = 4
        USE_GENERAL_SETTINGS = True

    class Arbitrum:
        MIN_AMOUNT = 0.00005
        MAX_AMOUNT = 0.00009
        DECIMAL = 6
        USE_IN_RANDOM = False

    class ArbitrumNova:
        MIN_AMOUNT = 0.00005
        MAX_AMOUNT = 0.00009
        DECIMAL = 6
        USE_IN_RANDOM = False

    class Optimism:
        MIN_AMOUNT = 0.00005
        MAX_AMOUNT = 0.00009
        DECIMAL = 6
        USE_IN_RANDOM = False

    class ZkSync:
        MIN_AMOUNT = 0.00005
        MAX_AMOUNT = 0.00009
        DECIMAL = 6
        USE_IN_RANDOM = False

    class PolygonZkEvm:
        MIN_AMOUNT = 0.00005
        MAX_AMOUNT = 0.00009
        DECIMAL = 6
        USE_IN_RANDOM = False

    class Zora:
        MIN_AMOUNT = 0.00005
        MAX_AMOUNT = 0.00009
        DECIMAL = 6
        USE_IN_RANDOM = False

    class Scroll:
        MIN_AMOUNT = 0.00005
        MAX_AMOUNT = 0.00009
        DECIMAL = 6
        USE_IN_RANDOM = False

    class Polygon:
        MIN_AMOUNT = 0.00005
        MAX_AMOUNT = 0.00009
        DECIMAL = 6
        USE_IN_RANDOM = False

    class Moonbeam:
        MIN_AMOUNT = 0.00005
        MAX_AMOUNT = 0.00009
        DECIMAL = 6
        USE_IN_RANDOM = True

    class Moonriver:
        MIN_AMOUNT = 0.00005
        MAX_AMOUNT = 0.00009
        DECIMAL = 6
        USE_IN_RANDOM = False

    class Canto:
        MIN_AMOUNT = 0.00005
        MAX_AMOUNT = 0.00009
        DECIMAL = 6
        USE_IN_RANDOM = False

    class Harmony:
        MIN_AMOUNT = 0.00005
        MAX_AMOUNT = 0.00009
        DECIMAL = 6
        USE_IN_RANDOM = False

    class Kava:
        MIN_AMOUNT = 0.00005
        MAX_AMOUNT = 0.00009
        DECIMAL = 6
        USE_IN_RANDOM = False

    class Conflux:
        MIN_AMOUNT = 0.00005
        MAX_AMOUNT = 0.00009
        DECIMAL = 6
        USE_IN_RANDOM = False

    class Gnosis:
        MIN_AMOUNT = 0.01
        MAX_AMOUNT = 0.05
        DECIMAL = 6
        USE_IN_RANDOM = True

    class Coredao:
        MIN_AMOUNT = 0.00005
        MAX_AMOUNT = 0.00009
        DECIMAL = 6
        USE_IN_RANDOM = False

    class Fuse:
        MIN_AMOUNT = 0.00005
        MAX_AMOUNT = 0.00009
        DECIMAL = 6
        USE_IN_RANDOM = False

    class Klaytn:
        MIN_AMOUNT = 0.00005
        MAX_AMOUNT = 0.00009
        DECIMAL = 6
        USE_IN_RANDOM = True

    class Dfk:
        MIN_AMOUNT = 0.00005
        MAX_AMOUNT = 0.00009
        DECIMAL = 6
        USE_IN_RANDOM = False

    class Orderly:
        MIN_AMOUNT = 0.00005
        MAX_AMOUNT = 0.00009
        DECIMAL = 6
        USE_IN_RANDOM = False
        
    class Celo:
        MIN_AMOUNT = 0.00005
        MAX_AMOUNT = 0.00009
        DECIMAL = 6
        USE_IN_RANDOM = True