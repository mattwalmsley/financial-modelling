# Financial Modelling

This repository is for educational purposes only and contains only my own work, open source code, and domain knowledge available online.

[License](license.txt)

## Documentation

- [Introduction](quantitative/documentation/finance/1_introduction.md)
- [Interest Rates](quantitative/documentation/finance/2_interest-rates.md)
- [Bonds](quantitative/documentation/finance/3_bonds.md)
- [Equities](quantitative/documentation/finance/4_equities.md)
- [Commodities](quantitative/documentation/finance/5_commodities.md)
  - [Commodity Derivatives](quantitative/documentation/finance/commodities/commodity_derivatives.md)
- [Arbitrage](quantitative/documentation/finance/6_arbitrage.md)
- [Forwards, Futures, and Swaps](quantitative/documentation/finance/7_forwards_futures_swaps.md)
- [Stochastic Processes](quantitative/documentation/finance/8_stochastic-processes.md)
- [Options](quantitative/documentation/finance/9_options.md)

## Reading List and References

- [1] J. Hull, Options, Futures and Other Derivatives. Pearson/Prentice Hall, 2009.
- [2] R. C. Martin and M. Martin, Agile Principles, Patterns, and Practices in C#. Pearson Education, 2006.

## Git Commands

View git remotes:

    git remote -v

Rename git remote:

    git remote rename <old_name> <new_name>

Git add second remote repo:

    git remote add <name> <url>

Git push to second remote repo:

    git push <remote_name> <branch_name>

If Git repo breaks run the following:

    find .git/objects/ -size 0 -exec rm -f {} \;

    git fetch origin
