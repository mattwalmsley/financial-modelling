namespace Common.Utils;

public static class MathUtils
{
    // Standard normal cumulative distribution function
    public static double NormCdf(double value)
    {
        return (1.0 + Erf(value / Math.Sqrt(2.0))) / 2.0;
    }

    private static double Erf(double x)
    {
        // constants
        const double A1 = 0.254829592;
        const double A2 = -0.284496736;
        const double A3 = 1.421413741;
        const double A4 = -1.453152027;
        const double A5 = 1.061405429;
        const double P = 0.3275911;

        // Save the sign of x
        var sign = 1;
        if (x < 0)
            sign = -1;
        x = Math.Abs(x);

        // A&S formula 7.1.26
        var t = 1.0 / (1.0 + P * x);
        var y = 1.0 - ((((A5 * t + A4) * t + A3) * t + A2) * t + A1) * t * Math.Exp(-x * x);

        return sign * y;
    }
}