using Microsoft.AspNetCore.Mvc;
using PricerServer.Builders;
using PricerServer.Models;

namespace PricerServer.Controllers;

[Route("api/[controller]")]
[ApiController]
public class QuoteRequestController : ControllerBase
{
    [HttpPost("create-option")]
    public ActionResult CreateOptionQuote([FromBody] OptionQuoteRequest request)
    {
        var builder = new OptionQuoteRequestBuilder()
            .SetSpotPrice(request.SpotPrice)
            .SetStrikePrice(request.StrikePrice)
            .SetRiskFreeRate(request.RiskFreeRate)
            .SetVolatility(request.Volatility)
            .SetTimeToMaturity(request.TimeToMaturity);

        var quoteRequest = builder.GetQuoteRequest();
        var price = quoteRequest.GetPrice();

        return Ok(new
        {
            Details = quoteRequest.GetRequestDetails(),
            Price = price
        });
    }
}
