import pandas as pd

# Question 1
# Average growth of GDP in 2023
df = pd.read_csv("dataset/gdpc1.csv")
previous_df = df.shift(periods=4)

result_df = df.join(previous_df, rsuffix="_prev")
result_df.columns = [column.lower() for column in result_df.columns]
result_df['date'] = pd.to_datetime(result_df['date'])
result_df["growth_rate"] = (result_df["gdpc1"] / result_df["gdpc1_prev"] - 1) * 100

print(result_df[result_df['date'].dt.year == 2023]['growth_rate'].mean())

# Question 2
# Inverse Treasury Yield
dgs10 = pd.read_csv("dataset/dgs10.csv")
dgs2 = pd.read_csv("dataset/dgs2.csv")

dgs10 = dgs10[dgs10['DATE'].notnull() == True].set_index('DATE')
dgs2 = dgs2[dgs2['DATE'].notnull() == True].set_index('DATE')
dgs_df = dgs10.join(dgs2, rsuffix="_2")

dgs_df['DGS10'] = pd.to_numeric(dgs_df['DGS10'], errors='coerce')
dgs_df['DGS2'] = pd.to_numeric(dgs_df['DGS2'], errors='coerce')
dgs_df["diff"] = dgs_df['DGS10'] - dgs_df['DGS2']

print(dgs_df[~dgs_df['diff'].isna()]['diff'].min())

# Question 3
start_date = "2019-04-09"
end_date = "2024-04-09"

sp500 = yf.download("^GSPC", start=start_date, end=end_date)["Adj Close"]
ipc_mexico = yf.download("^MXX", start=start_date, end=end_date)["Adj Close"]

# Calculate 5-year growth percentages
sp500_growth = ((sp500[-1] / sp500[0]) - 1) * 100
ipc_mexico_growth = ((ipc_mexico[-1] / ipc_mexico[0]) - 1) * 100

# Identify the largest growth
largest_growth = max(sp500_growth, ipc_mexico_growth)

# Question 4
start_date = "2023-01-01"
end_date = "2023-12-31"
sar = yf.download("2222.SR", start=start_date, end=end_date)["Adj Close"]
brkb = yf.download("BRK-B", start=start_date, end=end_date)["Adj Close"]
aapl = yf.download("AAPL", start=start_date, end=end_date)["Adj Close"]
msft = yf.download("MSFT", start=start_date, end=end_date)["Adj Close"]
goog = yf.download("GOOG", start=start_date, end=end_date)["Adj Close"]
jpm = yf.download("JPM", start=start_date, end=end_date)["Adj Close"]

sar_ratio = (sar.max() - sar.min()) / sar.max()
brkb_ratio = (brkb.max() - brkb.min()) / brkb.max()
aapl_ratio = (aapl.max() - aapl.min()) / aapl.max()
msft_ratio = (msft.max() - msft.min()) / msft.max()
goog_ratio = (goog.max() - goog.min()) / goog.max()
jpm_ratio = (jpm.max() - jpm.min()) / jpm.max()
print([sar_ratio, brkb_ratio, aapl_ratio, msft_ratio, goog_ratio, jpm_ratio].max())

# Question 5
sar_div = yf.Ticker("2222.SR").dividends
brkb_div = yf.Ticker("BRK-B").dividends
aapl_div = yf.Ticker("AAPL").dividends
msft_div = yf.Ticker("MSFT").dividends
goog_div = yf.Ticker("GOOG").dividends
jpm_div = yf.Ticker("JPM").dividends

sar_y = (sar_div[sar_div.index.year == 2023].sum() / sar.iloc[-1]) * 100
brkb_y = (brkb_div[brkb_div.index.year == 2023].sum() / brkb.iloc[-1]) * 100
aapl_y = (aapl_div[aapl_div.index.year == 2023].sum() / aapl.iloc[-1]) * 100
msft_y = (msft_div[msft_div.index.year == 2023].sum() / msft.iloc[-1]) * 100
goog_y = (goog_div[goog_div.index.year == 2023].sum() / goog.iloc[-1]) * 100
jpm_y = (jpm_div[jpm_div.index.year == 2023].sum() / jpm.iloc[-1]) * 100

print(round(max([sar_y, brkb_y, aapl_y, msft_y, goog_y, jpm_y]), 1))
