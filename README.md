# Financial Modelling

This repository is for educational purposes only and contains only my own work, open source code, and domain knowledge available online.

[License](license.txt)

## Documentation

- [Introduction](quant-library/documentation/1_introduction.md)
- [Interest Rates](quant-library/documentation/2_interest-rates.md)
- [Bonds](quant-library/documentation/3_bonds.md)
- [Equities](quant-library/documentation/4_equities.md)
- [Commodities](quant-library/documentation/5_commodities.md)
- [Arbitrage](quant-library/documentation/6_arbitrage.md)
- [Forwards, Futures, and Swaps](quant-library/documentation/7_forwards_futures_swaps.md)
- [Stochastic Processes](quant-library/documentation/8_stochastic-processes.md)
- [Options](quant-library/documentation/9_options.md)

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
