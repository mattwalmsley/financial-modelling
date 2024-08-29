using Common.Utils;

namespace PricerServer.Models.QuoteRequests;

public class OptionQuoteRequest : QuoteRequest
{
    public OptionQuoteRequest()
    {
        QuoteType = QuoteType.Option;
    }

    public double StrikePrice { get; set; }
    public double Volatility { get; set; }

    public override string GetRequestDetails()
    {
        return $"{nameof(OptionQuoteRequest)} Spot Price = {SpotPrice}, Strike Price = {StrikePrice}, " +
               $"Risk Free Rate = {RiskFreeRate}, Volatility = {Volatility}, " +
               $"Time to Maturity = {TimeToMaturity}";
    }

    public override double GetPrice()
    {
        // Example pricing model: Black-Scholes formula (simplified for demonstration purposes)
        // This is a placeholder and should be replaced with the actual pricing model.
        var d1 = (Math.Log(SpotPrice / StrikePrice) +
                  (RiskFreeRate + 0.5 * Math.Pow(Volatility, 2)) * TimeToMaturity) /
                 (Volatility * Math.Sqrt(TimeToMaturity));
        var d2 = d1 - Volatility * Math.Sqrt(TimeToMaturity);

        var optionPrice = SpotPrice * MathUtils.NormCdf(d1) -
                          StrikePrice * Math.Exp(-RiskFreeRate * TimeToMaturity) * MathUtils.NormCdf(d2);
        return optionPrice;
    }
}