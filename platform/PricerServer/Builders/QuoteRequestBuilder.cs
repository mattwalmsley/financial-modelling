using PricerServer.Models;

namespace PricerServer.Builders;

public abstract class QuoteRequestBuilder
{
    protected QuoteRequest QuoteRequest;

    public QuoteRequest GetQuoteRequest()
    {
        return QuoteRequest;
    }

    public abstract QuoteRequestBuilder SetSpotPrice(double spotPrice);
    public abstract QuoteRequestBuilder SetStrikePrice(double strikePrice);
    public abstract QuoteRequestBuilder SetRiskFreeRate(double riskFreeRate);
    public abstract QuoteRequestBuilder SetVolatility(double volatility);
    public abstract QuoteRequestBuilder SetTimeToMaturity(double timeToMaturity);
}