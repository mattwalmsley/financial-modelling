using Microsoft.AspNetCore.Mvc;
using PricerServer.Factories;
using PricerServer.Models.QuoteRequests;

namespace PricerServer.Controllers;

[Route("api/[controller]")]
[ApiController]
public class QuoteRequestController : ControllerBase
{
    private readonly IQuoteRequestFactory _quoteRequestFactory;

    public QuoteRequestController(IQuoteRequestFactory quoteRequestFactory)
    {
        _quoteRequestFactory = quoteRequestFactory;
    }

    [HttpPost("create-quote")]
    public ActionResult CreateQuote([FromQuery] string type, [FromBody] IQuoteRequest request)
    {
        var quoteRequest = _quoteRequestFactory.CreateQuoteRequest(type, request);
        var price = quoteRequest.GetPrice();

        return Ok(new
        {
            Details = quoteRequest.GetRequestDetails(),
            Price = price
        });
    }
}