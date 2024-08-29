using PricerServer.Builders.QuoteRequestBuilders;
using PricerServer.Models.QuoteRequests;

namespace PricerServer.Factories;

public interface IQuoteRequestFactory
{
    IQuoteRequest CreateQuoteRequest(string type, IQuoteRequest request);
}

public class QuoteRequestFactory : IQuoteRequestFactory
{
    public IQuoteRequest CreateQuoteRequest(string type, IQuoteRequest request)
    {
        var quoteType = Enum.Parse<QuoteType>(type);

        var incorrectFormatMessage = $"Request is not correctly formated as {quoteType}.";

        switch (quoteType)
        {
            case QuoteType.Option:
                if (request is not OptionQuoteRequest optionRequest)
                    throw new ArgumentException(incorrectFormatMessage);

                var optionBuilder = new OptionQuoteRequestBuilder()
                    .SetSpotPrice(optionRequest.SpotPrice)
                    .SetStrikePrice(optionRequest.StrikePrice)
                    .SetRiskFreeRate(optionRequest.RiskFreeRate)
                    .SetVolatility(optionRequest.Volatility)
                    .SetTimeToMaturity(optionRequest.TimeToMaturity);
                return optionBuilder.GetQuoteRequest();

            case QuoteType.Swap:
                if (request is not OptionQuoteRequest swapRequest)
                    throw new ArgumentException(incorrectFormatMessage);

                var swapBuilder = new SwapQuoteRequestBuilder()
                    .SetSpotPrice(swapRequest.SpotPrice)
                    .SetRiskFreeRate(swapRequest.RiskFreeRate)
                    .SetTimeToMaturity(swapRequest.TimeToMaturity);
                return swapBuilder.GetQuoteRequest();

            case QuoteType.Forward:
                if (request is not OptionQuoteRequest forwardRequest)
                    throw new ArgumentException(incorrectFormatMessage);

                var forwardBuilder = new SwapQuoteRequestBuilder()
                    .SetSpotPrice(forwardRequest.SpotPrice)
                    .SetRiskFreeRate(forwardRequest.RiskFreeRate)
                    .SetTimeToMaturity(forwardRequest.TimeToMaturity);
                return forwardBuilder.GetQuoteRequest();

            default:
                throw new ArgumentException("Invalid quote request type");
        }
    }
}