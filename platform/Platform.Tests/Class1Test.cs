using NUnit.Framework;

namespace Platform.Tests;

[TestFixture]
[TestOf(typeof(Class1))]
public class Class1Test
{
    [Test]
    public void SetOutput_ReturnsOutput()
    {
        const string testValue = "test";
        var output = new Class1(testValue);

        Assert.That(output.Output.Equals(testValue));
    }
}