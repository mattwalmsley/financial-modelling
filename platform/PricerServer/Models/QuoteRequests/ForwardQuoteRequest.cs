namespace PricerServer.Models.QuoteRequests;

public class ForwardQuoteRequest : QuoteRequest
{
    public ForwardQuoteRequest()
    {
        QuoteType = QuoteType.Forward;
    }

    public override string GetRequestDetails()
    {
        return
            $"{nameof(QuoteRequests.QuoteType)} = {QuoteType}:" +
            $" Spot Price = {SpotPrice}, Risk Free Rate = {RiskFreeRate}, Time to Maturity = {TimeToMaturity}";
    }

    public override double GetPrice()
    {
        return SpotPrice * Math.Exp(RiskFreeRate * TimeToMaturity);
    }
}