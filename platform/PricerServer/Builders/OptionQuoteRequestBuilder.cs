using PricerServer.Models;

namespace PricerServer.Builders;

public class OptionQuoteRequestBuilder : QuoteRequestBuilder
{
    public OptionQuoteRequestBuilder()
    {
        QuoteRequest = new OptionQuoteRequest();
    }

    public override QuoteRequestBuilder SetSpotPrice(double spotPrice)
    {
        ((OptionQuoteRequest)QuoteRequest).SpotPrice = spotPrice;
        return this;
    }

    public override QuoteRequestBuilder SetStrikePrice(double strikePrice)
    {
        ((OptionQuoteRequest)QuoteRequest).StrikePrice = strikePrice;
        return this;
    }

    public override QuoteRequestBuilder SetRiskFreeRate(double riskFreeRate)
    {
        ((OptionQuoteRequest)QuoteRequest).RiskFreeRate = riskFreeRate;
        return this;
    }

    public override QuoteRequestBuilder SetVolatility(double volatility)
    {
        ((OptionQuoteRequest)QuoteRequest).Volatility = volatility;
        return this;
    }

    public override QuoteRequestBuilder SetTimeToMaturity(double timeToMaturity)
    {
        ((OptionQuoteRequest)QuoteRequest).TimeToMaturity = timeToMaturity;
        return this;
    }
}