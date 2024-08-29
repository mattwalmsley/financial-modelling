using PricerServer.Models.QuoteRequests;

namespace PricerServer.Builders.QuoteRequestBuilders;

public class OptionQuoteRequestBuilder : QuoteRequestBuilder<OptionQuoteRequest, OptionQuoteRequestBuilder>
{
    public OptionQuoteRequestBuilder SetStrikePrice(double strikePrice)
    {
        QuoteRequest.StrikePrice = strikePrice;
        return this;
    }

    public OptionQuoteRequestBuilder SetVolatility(double volatility)
    {
        QuoteRequest.Volatility = volatility;
        return this;
    }
}