using PricerServer.Models.QuoteRequests;

namespace PricerServer.Builders.QuoteRequestBuilders;

public abstract class QuoteRequestBuilder<TQuoteRequest, TBuilder>
    where TQuoteRequest : QuoteRequest, new()
    where TBuilder : QuoteRequestBuilder<TQuoteRequest, TBuilder>
{
    protected TQuoteRequest QuoteRequest { get; } = new();

    public TQuoteRequest GetQuoteRequest()
    {
        return QuoteRequest;
    }

    public TBuilder SetSpotPrice(double spotPrice)
    {
        QuoteRequest.SpotPrice = spotPrice;
        return (TBuilder) this;
    }

    public TBuilder SetRiskFreeRate(double riskFreeRate)
    {
        QuoteRequest.RiskFreeRate = riskFreeRate;
        return (TBuilder) this;
    }

    public TBuilder SetTimeToMaturity(double timeToMaturity)
    {
        QuoteRequest.TimeToMaturity = timeToMaturity;
        return (TBuilder) this;
    }
}