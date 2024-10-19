# Financial Modelling

This repository is for educational purposes only and contains only my own work, open source code, and domain knowledge available online.

[License](license.txt)

## Documentation

- [Introduction](quant-library/documentation/finance/1_introduction.md)
- [Interest Rates](quant-library/documentation/finance/2_interest-rates.md)
- [Bonds](quant-library/documentation/finance/3_bonds.md)
- [Equities](quant-library/documentation/finance/4_equities.md)
- [Commodities](quant-library/documentation/finance/5_commodities.md)
  - [Commodity Derivatives](quant-library/documentation/finance/commodities/commodity_derivatives.md)
- [Arbitrage](quant-library/documentation/finance/6_arbitrage.md)
- [Forwards, Futures, and Swaps](quant-library/documentation/finance/7_forwards_futures_swaps.md)
- [Stochastic Processes](quant-library/documentation/finance/8_stochastic-processes.md)
- [Options](quant-library/documentation/finance/9_options.md)

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
