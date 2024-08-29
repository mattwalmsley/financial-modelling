namespace PricerServer.Models.QuoteRequests;

public enum QuoteType
{
    Forward,
    Swap,
    Option
}

public interface IQuoteRequest
{
    QuoteType QuoteType { get; set; }
    double SpotPrice { get; set; }
    double RiskFreeRate { get; set; }
    double TimeToMaturity { get; set; }
    string GetRequestDetails();
    double GetPrice();
}

public abstract class QuoteRequest : IQuoteRequest
{
    public QuoteType QuoteType { get; set; }
    public double SpotPrice { get; set; }
    public double RiskFreeRate { get; set; }
    public double TimeToMaturity { get; set; }
    public abstract string GetRequestDetails();
    public abstract double GetPrice();
}