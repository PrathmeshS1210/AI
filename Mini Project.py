#Mini Project
print("Stock Market Trading Expert System")
trend = input("Is the stock trend Rising or Falling? ").lower()
news = input("Is the market news Positive or Negative? ").lower()
volume = input("Is the trading volume High or Low? ").lower()
pe_ratio = input("Is the P/E Ratio Undervalued or Overvalued? ").lower()
print("\n Trading Recommendation")
if trend == "rising" and news == "positive" and volume == "high" and pe_ratio == "undervalued":
    print("Recommendation: Strong Buy ")
elif trend == "rising" and news == "positive":
    print("Recommendation: Buy ")
elif trend == "falling" and news == "negative":
    print("Recommendation: Sell ")
elif pe_ratio == "overvalued":
    print("Recommendation: Consider Selling ")
else:
    print("Recommendation: Hold ")
