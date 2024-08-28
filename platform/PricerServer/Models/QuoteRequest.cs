namespace PricerServer.Models;

public abstract class QuoteRequest
{
    public string Type { get; set; }
    public abstract string GetRequestDetails();
    public abstract double GetPrice();
}